#Importing the necessary libraries for the project
import tkinter as tk
from tkinter import *
import base64


#Setting up the Window and adding titles and window size
root = Tk()
root.geometry('350x400')
root.title("Python Message Encoder")

#----------------------------------------Brains-------------------------------------------------------------------------
#Encode function - This function changes the input text using the utf-8 encoding module.
def encodeInput():
    eCode = inputEntry.get()
    conversion = eCode.encode('utf-8')
    result = base64.b64encode(conversion)
    mainOutput.insert(1.0, result)
#Decode function - This function changes encoded text back into regular text that can be understood.
def decodeInput():
    dCode = outputEntry.get()
    result = base64.b64decode(dCode)
    mainOutput.insert(1.0, result)

#----------------------------------------Beauty-------------------------------------------------------------------------

#Buttons - the command attributes run the function located in the "Brains" section of the code.
encodeButton = tk.Button(root, command=encodeInput, text="Encode!").grid(row=3, column=2, pady=10)
decodeButton = tk.Button(root, command=decodeInput, text="Decode!").grid(row=5, column=2, pady=10)

#Textboxes I/O - These allow for user input in order to have content to run the functions
inputEntry = tk.Entry(root)
inputEntry.grid(row=2, column=2)
outputEntry = tk.Entry(root)
outputEntry.grid(row=4, column=2)
mainOutput = tk.Text(root, width=30, height=5)
mainOutput.grid(row=8, column=1, columnspan=5, padx=50)

#Labels Section - Guide the user
mainLabel = tk.Label(root, text="KEEP MESSAGES SECURE").grid(row=0, column=2)
subLabel = tk.Label(root, text="ENCODE NOW!").grid(row=1, column=2)

emptyLabel1 = tk.Label(root, text="                  ").grid(row=0, column=1)
emptyLabel2 = tk.Label(root, text="         ").grid(row=0, column=3)

#Labels in the window - Show the user where to put text
regularLabel = tk.Label(root, text="Regular Text: ").grid(row=2, column=1)
encodedLabel = tk.Label(root, text="Encoded Text: ").grid(row=4, column=1)

#mainloop() allows the window to appear by looping the code until an event happens like clicking a button.
root.mainloop()
