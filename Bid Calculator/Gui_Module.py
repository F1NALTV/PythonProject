#Jordan 
#Note to self just wanna kill myself because this was put off to last minute because no one knew what was going on yay!
import tkinter as tk

def addWorkerScreen():
    w = tk.Toplevel()
    test = tk.Button(w, text = "test")
    test.pack()

def eScreen():
    window = tk.Toplevel(root)
    addWorkerB = tk.Button(window, text ="Add Worker", command = addWorkerScreen())
    addWorkerB.pack()
def jScreen():
    window = tk.Toplevel(root)
    label = tk.Label(window, text = "Drywall:")
    label.pack()
root = tk.Tk()
createJButt = tk.Button(root, text ="Create Job", command = jScreen)
EButt = tk.Button(root, text ="Edit Employee", command = eScreen)
EButt.pack()
createJButt.pack()
root.mainloop()
