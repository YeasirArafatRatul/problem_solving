import tkinter as tk
from tkinter import filedialog
a = tk.Tk()
a.title("FileOpener")
def file():
    c = filedialog.askopenfilename()
    
    
    file = c.name
    f = open(file)
    label2 = label(text = f.read()).pack()
button = tk.Button(text ="Choose file",width=30,command = file).pack()
a.mainloop()
