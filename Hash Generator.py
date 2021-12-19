import tkinter as tk
from tkinter import *
import hashlib
#-----------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("Hash Generator")
root.geometry("1000x300")
#----------------------------------------------FUNCTIONS----------------------------------------------------------------
def generate():
    message = inputEntry.get().encode()
    output.set(hashlib.sha224(message).hexdigest())
    output1.set(hashlib.sha256(message).hexdigest())
    output2.set(hashlib.sha384(message).hexdigest())
    output3.set(hashlib.sha512(message).hexdigest())
    output4.set(hashlib.sha3_224(message).hexdigest())
    output5.set(hashlib.sha3_256(message).hexdigest())
    output6.set(hashlib.sha3_384(message).hexdigest())
    output7.set(hashlib.sha3_512(message).hexdigest())

#---------------------------------------------INPUTS--------------------------------------------------------------------
inputEntry = tk.Entry(root, width = 50)
inputEntry.grid(column = 2, row = 1)
#---------------------------------------------ENTRY---------------------------------------------------------------------
inputButton = tk.Button(root, text = "Generate", command = generate).grid(column = 3, row = 1)
#---------------------------------------------LABELS--------------------------------------------------------------------
inputLabel = tk.Label(root, text="Input your message here:").grid(column = 1, row = 1, sticky = "w")
output = StringVar()
output1 = StringVar()
output2 = StringVar()
output3 = StringVar()
output4 = StringVar()
output5 = StringVar()
output6 = StringVar()
output7 = StringVar()

outputLabel1 = tk.Label(root, text = "SHA224:").grid(column = 1, row = 3, sticky = "w")
outputLabel2 = tk.Label(root, text = "SHA256:").grid(column = 1, row = 4, sticky = "w")
outputLabel3 = tk.Label(root, text = "SHA384:").grid(column = 1, row = 5, sticky = "w")
outputLabel4 = tk.Label(root, text = "SHA512:").grid(column = 1, row = 6, sticky = "w")
outputLabel5 = tk.Label(root, text = "SHA3-224:").grid(column = 1, row = 7, sticky = "w")
outputLabel6 = tk.Label(root, text = "SHA3-256:").grid(column = 1, row = 8, sticky = "w")
outputLabel7 = tk.Label(root, text = "SHA3-384:").grid(column = 1, row = 9, sticky = "w")
outputLabel8 = tk.Label(root, text = "SHA3-512:").grid(column = 1, row = 10, sticky = "w")

outputLabel224 = tk.Label(root, textvariable = output).grid(column = 2, row = 3, sticky = "w")
outputLabel256 = tk.Label(root, textvariable = output1).grid(column = 2, row = 4, sticky = "w")
outputLabel384 = tk.Label(root, textvariable = output2).grid(column = 2, row = 5, sticky = "w")
outputLabel512 = tk.Label(root, textvariable = output3).grid(column = 2, row = 6, sticky = "w")
outputLabel3224 = tk.Label(root, textvariable = output4).grid(column = 2, row = 7, sticky = "w")
outputLabel3256 = tk.Label(root, textvariable = output5).grid(column = 2, row = 8, sticky = "w")
outputLabel3384 = tk.Label(root, textvariable = output6).grid(column = 2, row = 9, sticky = "w")
outputLabel3512 = tk.Label(root, textvariable = output7).grid(column = 2, row = 10, sticky = "w")
#-----------------------------------------------------------------------------------------------------------------------


root.mainloop()
