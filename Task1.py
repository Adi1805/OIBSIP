import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to get the current time
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

# Function to get the current date
def tell_date():
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

# Function to search Wikipedia for a query
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("The topic is too ambiguous. Please be more specific.")
    except Exception as e:
        speak("I couldn't find information on that topic.")

# Main function to process voice commands
def process_command(command):
    command = command.lower()
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "search" in command:
        search_query = command.replace("search", "").strip()
        search_wikipedia(search_query)
    else:
        speak("I'm sorry, I don't understand that command.")

# Function to listen to the user's voice and process it
def listen_and_respond():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            process_command(command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            speak("Sorry, the speech service is unavailable.")

# Run the assistant
if __name__ == "__main__":
    speak("Voice assistant is activated.")
    while True:
        listen_and_respond()
