from objects import Building
from tkinter import Tk, Label, Button, Frame, Canvas
from time import sleep

class MainMenu:
    def __init__(self,name="Billionaire Business"):
        width,height = 512,256
        self.mainMenuWindow = Tk()
        self.mainMenuWindow.title(name)
        self.mainMenuWindow.geometry("{}x{}".format(width,height))
        self.startCanvas = Canvas(
            master=self.mainMenuWindow,
            width=width,
            height=height
        )
        Button(
            master=self.startCanvas,
            text="Start/Resume",
            command=self.Start,
            width=10,
            height=3,
        ).pack()
        self.startCanvas.pack()

        self.mainMenuWindow.mainloop()
    
    def Start(self):
        Label(
            master=self.startCanvas,
            text="Game is Loading!"
        ).pack()
        self.startCanvas.update()
        sleep(1.5)
        self.mainMenuWindow.destroy()



class MainGame():
    def __init__(self,name="tk  das"):
