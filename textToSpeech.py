import pyttsx3
import tkinter

#pip install speechrecognition, pyaudio, pyttsx3 --user

import speech_recognition as sr
import pyttsx3

def main():
    # Initialize the recognizer 
    r = sr.Recognizer() 

    # Function to convert text to
    # speech
    def SpeakText(command):
        
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command) 
        engine.runAndWait()
        
    def text_To_Speech_entry():
        value = entry.get()
        print("Entry value:", value)
        
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        engine.setProperty('volume', 0.8)  # Volume (0.0 to 1.0)

        # Say something
        text = value
        engine.say(text)

        # Run and wait for the speech to finish
        engine.runAndWait()
    
    
    def start_loop():
        #Allow this object run in the backgroun
        global running
        
        running = True
            # Loop infinitely for user to
            # speak
        while running:
            
            # Exception handling to handle
            # exceptions at the runtime
            try:
                
                # use the microphone as source for input.
                with sr.Microphone() as source2:
                    
                    # wait for a second to let the recognizer
                    # adjust the energy threshold based on
                    # the surrounding noise level 
                    r.adjust_for_ambient_noise(source2, duration=0.2)
                    
                    #listens for the user's input 
                    audio2 = r.listen(source2)
                    
                    # Using google to recognize audio
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    print(MyText)
                    SpeakText(MyText)
                    
            except sr.RequestError as e:
                pass
                
            except sr.UnknownValueError:
                pass
            root.update()  # Allow Tkinter to process events
            if not running:
                break
    
    #Stop the loop of active voice in tkinter event
    def stop_loop():
        global running
        running = False
    
    root = tkinter.Tk()
    #title
    root.title("Text To Speech")
    
    
    # Create a button with active text_To_Speech_entry
    button = tkinter.Button(root, text="Submit text", command=text_To_Speech_entry)
    button.pack()
    
    # Create an Entry widget for input text
    entry = tkinter.Entry(root)
    entry.pack()
    
    #Lebel
    l = tkinter.Label(root, text = "Trun on/off active_Live")
    l.pack()
    
    # Create a button with active_Live
    start_button = tkinter.Button(root, text="On", command=start_loop)
    start_button.pack()

    stop_button = tkinter.Button(root, text="Off", command=stop_loop)
    stop_button.pack()
    
    
    #Create the Frame of the container
    frame = tkinter.Frame(root, width=200, height=100)
    frame.pack()
    root.mainloop()

if __name__=="__main__":
    main()
