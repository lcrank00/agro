import tkinter as tk
import speech_recognition as sr

# Function to capture user voice input
def capture_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak your question:")
        audio = r.listen(source)
    try:
        user_input = r.recognize_google(audio)
        print("You said: " + user_input)
        return user_input
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to simulate voice bot response (replace with actual logic)
def handle_user_input(user_input):
    response = ""
    if user_input.lower() == "hi":
        response = "Hello there!  This is AGRO VOICE BOT !!. How can I help you today?"
    elif user_input.lower() == "what crops can i grow":
        response = "The crops you can grow depend on your region's climate. Would you like me to find information about crops suitable for your district?"
    # Add more questions and responses here
    return response

# Create the main window
root = tk.Tk()
root.title("AGRO - Voice Chat")

# Text area for conversation history
chat_history = tk.Text(root)
chat_history.pack(padx=10, pady=10)

# Input field for user (can be text or voice)
user_input_field = tk.Entry(root)
user_input_field.pack(padx=10, pady=10)

# Button to submit user input (can be text or voice button)
voice_button = tk.Button(root, text="Speak", command=lambda: handle_chat(user_input_field, capture_voice()))
voice_button.pack(padx=10, pady=10)

def handle_chat(input_field, capture_func):
    user_input = capture_func()  # Capture voice input
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    voice_bot_response = handle_user_input(user_input)  # Simulate voice bot response
    chat_history.insert(tk.END, "Voice Bot: " + voice_bot_response + "\n")
    input_field.delete(0, tk.END)  # Clear input field

root.mainloop()
voi