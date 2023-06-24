import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the properties for the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index to select different voice

# Decrease the speech rate
rate = engine.getProperty('rate')   # Get the current speech rate
engine.setProperty('rate', rate-80) # Decrease the speech rate by 50 units

# Speak the text
while True:
    x = input("Enter what you want me to speak:")
    text = {x}
    engine.say(text)
    engine.runAndWait()
    
