import tkinter as tk

class MetronomeWindow(tk.Toplevel):

    def openMetWindow():

        window = tk.Tk()

        window.title('Guitar Hub')
        window.geometry("300x200+10+20")

        #Header
        label = tk.Label(text="GuitarHub")
        label.pack()

        #list of buttons
        Metronomebutton = tk.Button(text="Start")
        Metronomebutton.pack()


        window.mainloop()

    #add more functions for the timer etc.



if __name__ == "__main__":
    MetronomeWindow.openMetWindow()