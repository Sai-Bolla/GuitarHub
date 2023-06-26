
#GUI creation

import tkinter as tk

def createMainWindow():
    window = tk.Tk()

    window.title('Guitar Hub')
    window.geometry("300x200+10+20")

    #Header
    label = tk.Label(text="GuitarHub")
    label.pack()

    #list of buttons
    Metronomebutton = tk.Button(text="Metronome")
    Metronomebutton.pack()

    Guessingbutton = tk.Button(text="Guessing Game")
    Guessingbutton.pack()

    Randombutton = tk.Button(text="Random note/chord")
    Randombutton.pack()
    window.mainloop()


if __name__ == "__main__":
    createMainWindow()