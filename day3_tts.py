import pyttsx3

# Load a sample chunk manually (for Day 3)
sample_text = """
Manpreet Walia is a B.Tech Computer Science student with experience
in IoT systems, machine learning, and backend development.
"""

engine = pyttsx3.init()

engine.setProperty('rate', 170)   # speaking speed
engine.setProperty('volume', 1.0) # volume (0.0 to 1.0)

engine.say(sample_text)
engine.runAndWait()

print("Audio playback completed")

