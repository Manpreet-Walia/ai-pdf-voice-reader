import pyttsx3

# Initialize engine (macOS native)
engine = pyttsx3.init('nsss')

# -------- USER CONTROLS --------
SPEECH_SPEED = "slow"   # options: slow, normal, fast
VOICE_INDEX = 1           # change this to try different voices
# --------------------------------

# Set speech speed
if SPEECH_SPEED == "slow":
    engine.setProperty('rate', 130)
elif SPEECH_SPEED == "fast":
    engine.setProperty('rate', 210)
else:
    engine.setProperty('rate', 170)  # normal

# List available voices
voices = engine.getProperty('voices')

print("Available voices:")
for i, v in enumerate(voices):
    print(f"{i}: {v.name}")

# Set selected voice
engine.setProperty('voice', voices[VOICE_INDEX].id)

# Sample text (short on purpose)
text = (
    "This is an AI-powered PDF reader. "
    "The user can control speech speed and select different voice accents."
)

engine.say(text)
engine.runAndWait()

print("Voice playback completed")

