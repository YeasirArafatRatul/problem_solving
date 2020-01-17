from tkinter import*
import tkinter

counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(100,count)
    count()
root = Tk()
root.title("COUNTER")
root.geometry("500x500")
label = tkinter.Label(root,fg ="red",font=50)
label.pack()
counter_label(label)
button = tkinter.Button(root,text="Stop",width = 40,command = root.destroy)
button.pack()
root.mainloop()
