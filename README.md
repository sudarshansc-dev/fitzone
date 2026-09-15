# NOVA — AI Voice Assistant for Windows 11

NOVA is a personal laptop voice assistant inspired by JARVIS. It listens for
the wake phrase **"Hey Nova"**, understands natural commands, speaks replies,
and controls your Windows computer — opening apps, searching the web, taking
screenshots, reading system info, and more.

## Features

- **Wake word activation** — say "Hey Nova" or "Nova" to wake it up
- **Keyboard hotkey** — press `Ctrl + Space` to activate without speaking
- **Natural language commands** — "open Chrome", "launch VS Code", "start YouTube" all work
- **Voice response** — NOVA speaks back using Windows text-to-speech
- **Conversation memory** — short-term context so follow-ups like "search for Python" work
- **Local preference memory** — remembers your name and other facts
- **System control** — open/close apps, open websites, web search, open folders, create folders & files, volume, lock, screenshot, file search
- **System info** — CPU, RAM, disk, battery, Windows version, network status
- **Safety gates** — shutdown / restart / destructive actions require spoken confirmation
- **Futuristic GUI** — dark interface with an animated listening orb, conversation history, start/stop, settings, and minimize-to-tray
- **Offline AI layer** — understands intents locally with fuzzy matching; optional OpenAI integration for richer chat

---

## Installation (Windows 11)

### 1. Install Python 3.10 or 3.11

Download from https://www.python.org/downloads/ and check **"Add Python to PATH"**
during installation.

Verify:
```powershell
python --version
```

### 2. Install dependencies

Open PowerShell in the NOVA folder and run:

```powershell
pip install -r requirements.txt
```

**PyAudio note:** if `PyAudio` fails to install, install the prebuilt wheel:

```powershell
pip install pipwin
pipwin install pyaudio
```

or download a matching wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
and install it with `pip install PyAudio‑0.2.14‑cp311‑cp311‑win_amd64.whl`
(adjust the filename for your Python version).

### 3. (Optional) Better Windows voices

NOVA uses the default Windows SAPI voices. For more natural voices:

- Open **Settings → Time & Language → Speech → Manage voices**
- Click **Add voices** and install ones you like (e.g. "Microsoft Zira", "Microsoft George")

Set which voice NOVA uses in `config.py` → `TTS_VOICE_INDEX` (0 or 1).

### 4. (Optional) Enable GPT-powered chat

By default NOVA runs fully offline. To use OpenAI for richer conversation:

1. `pip install openai`
2. Set `USE_OPENAI = True` in `config.py`
3. Set your API key: `setx OPENAI_API_KEY "sk-..."` (restart your terminal after)

Without this, NOVA uses its built-in local reasoning — no key needed.

---

## Run NOVA

```powershell
python main.py
```

The NOVA window appears with the animated orb. Say **"Hey Nova"** or press
**`Ctrl + Space`**, then give a command.

---

## Voice Commands

NOVA understands many phrasings. Examples:

| You say | NOVA does |
|---|---|
| "Hey Nova … open Chrome" | Opens Google Chrome |
| "Nova, launch VS Code" | Opens VS Code |
| "Open YouTube" | Opens youtube.com |
| "Search Google for Python tutorials" | Opens a Google search |
| "Search for Python voice assistant tutorial" | Continues from prior context |
| "Open Downloads" | Opens the Downloads folder |
| "Create a folder called Projects" | Creates it on your Desktop |
| "Create a file called notes" | Creates notes.txt on your Desktop |
| "Take a screenshot" | Saves a screenshot to `data/screenshots/` |
| "What time is it?" / "What's the date?" | Speaks the current time/date |
| "Set volume to 50" / "Volume up" / "Mute" | Adjusts system volume |
| "How much RAM am I using?" | Reports RAM usage |
| "Battery status" | Reports battery level |
| "Lock the computer" | Locks Windows |
| "Shut down the computer" | Asks for confirmation, then shuts down |
| "Restart the computer" | Asks for confirmation, then restarts |
| "Search files for resume" | Searches your user folder for matching files |
| "My name is Alex" | Remembers your name |
| "What's my name?" | Recalls your name |
| "Forget my name" | Deletes that memory |
| "Train my voice" | Records a voice sample for recognition |
| "Enable voice recognition" | Turns on speaker identification |
| "Disable voice recognition" | Turns off speaker identification |
| "Clear my voice" | Deletes the stored voice profile |

If a command is ambiguous, NOVA keeps conversation context. Example:

```
You: "Nova, open Chrome."
NOVA: "Opening Chrome."
You: "Search for Python."
NOVA: "What would you like me to search for?"
You: "Python voice assistant tutorial."
NOVA: "Searching for Python voice assistant tutorial."
```

---

## Project Structure

```
NOVA/
├── main.py                 # entry point — launches GUI + assistant
├── config.py               # all settings (voice, wake word, hotkey, AI)
├── requirements.txt
├── core/
│   ├── assistant.py        # orchestrator: wake -> stt -> brain -> action -> tts
│   ├── command_processor.py# intent detection with fuzzy matching
│   ├── memory.py           # local persistent memory (data/memory.json)
│   └── security.py         # destructive-action confirmation gate
├── voice/
│   ├── speech_to_text.py   # Google Web Speech via SpeechRecognition
│   ├── text_to_speech.py   # offline TTS via pyttsx3
│   ├── wake_word.py        # wake-word detection / fallback continuous listen
│   └── voice_profile.py    # optional speaker recognition (NOT a security system)
├── actions/
│   ├── applications.py     # open / close apps
│   ├── browser.py          # open websites, web search
│   ├── system.py           # power, lock, volume, system info
│   ├── files.py            # folders, files, file search
│   └── screenshot.py       # screenshot capture
├── ai/
│   └── brain.py            # reasoning layer (local + optional OpenAI)
├── gui/
│   └── interface.py        # futuristic PyQt5 desktop UI + tray
└── data/
    └── memory.json         # preferences + conversation context
```

---

## How It Works (pipeline)

1. **Wake word** — continuously listens until it hears "Nova"
2. **Speech-to-text** — captures your command (Google Web Speech)
3. **Command processing** — fuzzy intent detection maps phrasings to actions
4. **AI reasoning** — ambiguous input gets a conversational reply
5. **Security check** — destructive actions require spoken confirmation
6. **Action execution** — the matched action runs on your computer
7. **Text-to-speech** — NOVA speaks the result
8. **Memory** — the exchange is saved for short-term context

---

## Safety

- Destructive actions (shutdown, restart, delete) **always** require a spoken "yes" confirmation
- NOVA opens apps and websites via safe system calls — it never auto-runs downloaded files
- Unknown commands produce "I didn't understand that" rather than crashing
- If an app isn't installed, NOVA says so instead of failing

### Voice Recognition (optional, NOT a security system)

NOVA can learn to recognize your voice. Say **"Train my voice"** or click the
**Train Voice** button in the GUI — NOVA records ~5 seconds of speech and stores
a lightweight feature profile locally in `data/voice_profile.json`. After
enrollment, say **"Enable voice recognition"** (or toggle it in Settings).

When enabled, NOVA reports voice confidence on each command. However, **voice
recognition is not treated as a security boundary**: even if your voice is not
recognized, commands still execute — and destructive actions still require
spoken confirmation. For truly sensitive operations, rely on Windows
authentication (lock screen, UAC), not on NOVA's voice match.

To remove the profile, say **"Clear my voice"** or delete `data/voice_profile.json`.

---

## Settings

Edit `config.py` to change:

- Wake words and timeout
- Voice speed, volume, and which voice to use
- Search engine (Google / Bing / DuckDuckGo)
- Activation hotkey
- Whether to require confirmation for destructive actions
- Whether to use OpenAI for chat
- Voice profile enable/disable and similarity threshold

You can also change most of these from the **Settings** button in the GUI.

---

## Troubleshooting

**"No module named PyAudio"** — install with `pipwin install pyaudio` (see above).

**Microphone not working** — make sure your mic is set as default in
Windows **Settings → System → Sound → Input**. Also check app mic permissions
under **Privacy & security → Microphone**.

**NOVA doesn't hear you** — try speaking the wake word more clearly, or increase
the mic sensitivity by lowering `RECOGNIZER_ENERGY_THRESHOLD` in `config.py`.

**Voice sounds robotic** — install additional Windows SAPI voices (see step 3),
or enable OpenAI chat for smarter (still-spoken) replies.
