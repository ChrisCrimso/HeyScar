import os
import tkinter as tk
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


# Initialize the speech engine
engine = pyttsx3.init()
recognizer = sr.Recognizer() #This is so it can recognize my voice
crimson_red = '#DC143C'

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for commands
def listen():
    with sr.Microphone() as source: #The key of the computer listening to commands
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("User said " + command)
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you say that again?")
            return listen()
        except sr.RequestError:
            speak("Sorry, there seems to be a network issue.")
            return ""
        return command


# Functions for Crimson browser


def open_application():
    speak("Which application would you like to open?")
    app_name = listen().lower()  # Use the listen method to capture the app name
    if "notepad" in app_name:
        os.startfile("notepad.exe")
    elif "calculator" in app_name:
        os.startfile("calc.exe")
    elif "browser" in app_name or "chrome" in app_name:
        os.startfile("chrome.exe")  # Example for opening Chrome
    elif "word" in app_name:
        os.startfile("winword.exe")  # Example for opening Microsoft Word
    elif "excel" in app_name:
        os.startfile("excel.exe")  # Example for opening Microsoft Excel
    elif "powerpoint" in app_name:
        os.startfile("powerpnt.exe")
    elif "firefox" in app_name:
        os.startfile("firefox.exe")
    elif "outlook" in app_name:
        os.startfile("outlook.exe")
    elif "files" in app_name:
        os.startfile(".exe")
    else:
        speak(f"Sorry, I can't find the application {app_name}.")

# Function to set a reminder
def set_reminder(): #This is to set reminders to users
    speak("What should I remind you about?")
    reminder = listen()
    speak("When should I remind you? Please say the time in hours and minutes.")
    reminder_time = listen()
    with open("reminders.txt", "a") as file:
        file.write(f"Reminder: {reminder} at {reminder_time}\n")
    speak(f"Reminder set for {reminder_time}")

def open_Crimson():
    speak("Opening up Crimson")
    crimson_page = tk.Tk()
    crimson_page.title("Crimson King")
    crimson_page.geometry("800x1000")
    crimson_page.configure(bg=crimson_red)


    crimson_label = tk.Label(text="YOUR BOND IS CANCELLED!", fg='white', bg='black', font=("Times new roman", 16))
    crimson_label.place(x=250, y= 250)

    



    crimson_page.mainloop()




# Function to create a to-do list
def create_todo():
    speak("What task would you like to add to your to-do list?")
    task = listen()
    with open("todo.txt", "a") as file:
        file.write(f"Task: {task}\n")
    speak(f"Task '{task}' added to your to-do list.")

# Function to search the web
def search_web(): #The computer searches based on what you tell it to search
    speak("What do you want to search for?")
    query = listen() #It listens to what you tell it
    url = f"https://www.google.com/search?q={query}" #It will use google to search what you tell it to search
    webbrowser.open(url) #The url depends on what you tell the computer
    speak(f"Here are the results for {query}")

def get_time(): # This will get the current time
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The time is {current_time}")
def get_date(): #This will get the current date
    date_now = datetime.date.today()
    current_date = date_now.today()
    speak(f"The date is {current_date}.")


# Main function to handle commands
def handle_command(command): #The handle_command is responsible for executing the request
    if "reminder" in command:
        set_reminder()
    elif "to-do" in command or "task" in command:
        create_todo()
    elif "search" in command:
        search_web()
    elif "time" in command:
        get_time()
    elif "date" in command:
        get_date()
    elif "open" in command:
        open_application()
    elif "crimson" in command:
        open_Crimson()
    else:
        speak("Sorry, I can only help with setting reminders, creating to-do lists, and searching the web.")

# Main loop
def main():
    speak("Hello, I am Crimson, how can I assist you today?")
    while True:
        command = listen()
        if "exit" in command or "stop" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            handle_command(command)

if __name__ == "__main__":
    main()
