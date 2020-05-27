from tkinter import Tk, Canvas, PhotoImage
from random import randint


class Main():
    def __init__(self):
        self.root = Tk()
        self.death = False
        self.camson = False
        self.left = True
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.c = Canvas(self.root, width=self.width, height=self.height)
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.title("Don't die")
        self.bowlyattack2 = 0
        self.c.pack()
        self.bowlybodyB = PhotoImage(file="bowly_chains.png")
        self.bowlyheadB = PhotoImage(file="bowly_head.png")
        self.c.create_rectangle(0, 0, self.width, self.height, fill="#606060",
                                outline="#606060")
        self.bowlyhead = self.c.create_image(self.width / 2, self.height / 2,
                                             anchor="c", image=self.bowlyheadB,
                                             state="hidden")
        self.wd = self.width / 1920
        self.hd = self.width / 1080
        self.camm = PhotoImage(file="cammap.png")
        self.text = self.c.create_text(0, 0, anchor="nw", text="")
        self.text2 = self.c.create_text(0, 15, anchor="nw", text="")
        self.cama = PhotoImage(file="camA.png")
        self.bowlycama = PhotoImage(file="camAbowly.png")
        self.currentcam = self.c.create_image(0, 0, anchor="nw",
                                              image=self.cama, state="hidden")
        self.cammap = self.c.create_image(self.width - 200, self.height - 200,
                                          anchor="se", image=self.camm,
                                          state="hidden")
        self.icon = PhotoImage(file="camera_icon.png")
        self.camicon = self.c.create_image(self.width - 100, self.height - 100,
                                           anchor="se", image=self.icon,
                                           state="normal")
        self.c.tag_bind(self.camicon, "<Enter>", self.cams_on)
        self.incama = False
        self.c.tag_bind(self.camicon, "<Leave>", self.cams_off)
        self.root.bind("<Motion>", self.motion)
        self.root.bind("d", self.die)
        self.root.bind("<Escape>", self.kr)
        self.root.after(10, self.eachcsec)
        self.root.mainloop()

    def die(self, event=""):
        self.death = True

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
        if self.bowlyattack == 5:
            self.c.itemconfig(self.currentcam, image=self.bowlycama)
            self.c.itemconfig(self.text, text=self.bowlyattack)
            self.incama = True
        if self.incama:
            self.bowlyattack2 = randint(0, 999)
        if (self.incama and self.bowlyattack2 == 5) or self.death:
            self.c.itemconfig(self.currentcam, state="hidden")
            self.c.itemconfig(self.cammap, state="hidden")
            self.c.itemconfig(self.bowlyhead, state="normal")
            self.root.after(5000, self.game_over_screen)
        self.root.after(10, self.eachcsec)

    def cams_off(self, event=None):
        self.left = True

    def motion(self, event):
        self.x = event.x
        self.y = event.y

    def game_over_screen(self):
        self.c.create_rectangle(0, 0, self.width, self.height,
                                fill="red", outline="red")
        self.c.create_text(self.width / 2, self.height / 2, text="Game Over",
                           anchor="c", fill="#000000", font=("Helvetica", 100))
        self.root.after(2000, self.kr)


game = Main()
