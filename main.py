from tkinter import Tk, Canvas, PhotoImage
from random import randint


class Main():
    def __init__(self):
        self.root = Tk()
        self.camson = False
        self.left = True
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.c = Canvas(self.root, width=self.width, height=self.height)
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.title("Don't die")
        self.c.pack()
        self.camm = PhotoImage(file="cammap.png")
        self.text = self.c.create_text(0, 0, anchor="nw", text="")
        self.cammap = self.c.create_image(self.width - 200, self.height - 200, anchor="se", image=self.camm, state="hidden")
        self.cama = PhotoImage(file="camA.png")
        self.bowlycama = PhotoImage(file="camAbowly.png")
        self.currentcam = self.c.create_image(0, 0, anchor="nw", image=self.cama, state="hidden")
        self.icon = PhotoImage(file="camera_icon.png")
        self.camicon = self.c.create_image(self.width - 100, self.height - 100, anchor="se", image=self.icon, state="normal")
        self.c.tag_bind(self.camicon, "<Enter>", self.cams_on)
        self.incama = False
        self.c.tag_bind(self.camicon, "<Leave>", self.cams_off)
        self.root.bind("<Motion>", self.motion)
        self.root.bind("<Escape>", self.kr)
        self.root.after(10, self.eachcsec)
        self.root.mainloop()

    def kr(self, event=None):
        self.root.destroy()

    def cams_on(self, event=None):
        if self.left:
            self.left = False
            if not self.camson:
                self.c.itemconfig(self.cammap, state="normal")
                self.c.itemconfig(self.currentcam, state="normal")
                self.camson = True
            else:
                self.c.itemconfig(self.currentcam, state="hidden")
                self.c.itemconfig(self.cammap, state="hidden")
                self.camson = False

    def eachcsec(self):
        self.bowlyattack = randint(0, 500)
        self.bowlyattack2 = randint(0, 1000)
        self.c.itemconfig(self.text, text=self.bowlyattack)
        if self.bowlyattack == 5:
            self.c.itemconfig(self.currentcam, image=self.bowlycama)
            self.c.itemconfig(self.text, text=self.bowlyattack)
            self.incama = True
        self.root.after(10, self.eachcsec)
        if self.incama and self.bowlyattack2 == 1000:
            pass

    def cams_off(self, event=None):
        self.left = True

    def motion(self, event):
        self.x = event.x
        self.y = event.y


game = Main()
