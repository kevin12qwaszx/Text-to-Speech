import pyttsx3
import tkinter

#pip install speechrecognition
#pip install pyttsx3 --user


# Defining main function

def main():
    
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

        
    root = tkinter.Tk()

    root.title("Text To Speech")
    
    # Create a button with active background and foreground colors
    button = tkinter.Button(root, text="Submit text", command=text_To_Speech_entry)
    button.pack()
    
    # Create an Entry widget with selection colors
    entry = tkinter.Entry(root)
    entry.pack()
    
    #Create the Frame of the container
    frame = tkinter.Frame(root, width=200, height=100)
    frame.pack()

    root.mainloop()
    
    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
