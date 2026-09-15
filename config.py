"""NOVA configuration. Edit values here to customize your assistant."""

import os

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")

# --- Wake word ---
WAKE_WORDS = ["hey nova", "nova"]
WAKE_WORD_TIMEOUT = 10  # seconds to wait for a command after wake word
CONTINUOUS_LISTEN = True  # fallback: continuously listen and detect "nova" in speech

# --- Voice / TTS ---
TTS_RATE = 175  # words per minute
TTS_VOLUME = 1.0  # 0.0 - 1.0
TTS_VOICE_INDEX = 0  # 0 = first available voice (often male), 1 = second

# --- Speech recognition ---
RECOGNIZER_ENERGY_THRESHOLD = 300
RECOGNIZER_DYNAMIC_ENERGY = True
PHRASE_TIME_LIMIT = 8  # max seconds for a command
MIC_DEVICE_INDEX = None  # None = default mic, or an integer index

# --- Behavior ---
CONFIRM_DESTRUCTIVE = True  # require confirmation for shutdown/restart/delete
SEARCH_ENGINE = "google"  # google, bing, duckduckgo
DEFAULT_BROWSER = "default"  # "default" uses system default browser

# --- AI ---
# Uses a local rule-based + fuzzy matcher by default (no API key needed).
# Set USE_OPENAI to True and add OPENAI_API_KEY to enable GPT reasoning.
USE_OPENAI = False
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
OPENAI_MODEL = "gpt-4o-mini"

# --- Keyboard shortcut to activate NOVA ---
# Uses pynput. Set to None to disable.
HOTKEY = "<ctrl>+<space>"

# --- Conversation ---
MAX_HISTORY = 20  # number of exchanges to keep in short-term memory

# --- Voice profile (optional speaker recognition) ---
# NOT a security system — destructive actions always require confirmation
# regardless of voice match. Enroll via "train my voice" or the GUI button.
VOICE_PROFILE_ENABLED = False  # set True after enrollment
VOICE_PROFILE_THRESHOLD = 0.72  # cosine similarity 0.0-1.0; lower = more lenient
