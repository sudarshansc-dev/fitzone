"""NOVA — entry point.

Run:  python main.py
"""

import os
import sys

# ensure local packages import cleanly on Windows
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Python 3.12+ removed distutils, which PyAudio relies on. Import setuptools
# early so distutils is available before speech_recognition/PyAudio load.
try:
    import setuptools  # noqa: F401  - import side-effect: provides distutils
    import distutils  # noqa: F401  - verify it's available
except ImportError:
    print("[NOVA] Warning: setuptools is not installed. Install it with: pip install setuptools")

from PyQt5.QtWidgets import QApplication

from config import DATA_DIR
from gui.interface import NovaWindow
from core.assistant import NovaAssistant


def ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)


def main():
    ensure_dirs()

    app = QApplication(sys.argv)
    app.setApplicationName("NOVA")
    app.setQuitOnLastWindowClosed(False)  # keep running in tray when minimized

    assistant = NovaAssistant()
    window = NovaWindow(assistant)
    window.show()

    # wire assistant events -> GUI
    assistant.on_status = window.update_status
    assistant.on_response = window.append_response
    assistant.on_command = window.append_command
    assistant.on_listening = window.set_listening
    assistant.on_log = window.append_history
    assistant.on_voice_status = window.update_voice_status

    # start the assistant loop in a worker thread
    assistant.start()

    code = app.exec_()
    assistant.stop()
    sys.exit(code)


if __name__ == "__main__":
    main()
