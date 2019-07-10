import tkinter as tk

root = tk.Tk()
bouton = tk.Button(root, text="hello")


def bouton_action():
    print("hello world")

bouton["command"] = bouton_action

bouton.pack()

root.mainloop()