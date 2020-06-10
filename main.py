from tkinter import Tk, Canvas, PhotoImage
from random import randint


class Main():
    def __init__(self):
        # Screen, Canvas, etc...
        self.root = Tk()
        self.c = Canvas(self.root, width=self.width, height=self.height)
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.title("Don't die")
        self.bowlyattack2 = 0
        self.c.pack()
        # initiation of variables
        self.youhavewon = False
        self.electricity = 100
        self.electricity2 = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.usage = 0
        self.death = False
        self.camson = False
        self.rdoor_closed = False
        self.ldoor_closed = False
        self.left = True
        self.hour = 12
        # Usefull variables
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.wd = self.width / 1920
        self.hd = self.width / 1080
        # Image references `yay'
        self.bowlybodyB = PhotoImage(file="bowly_chains.png")
        # Unused line /\
        #             |
        #             |
        self.bowlyheadB = PhotoImage(file="bowly_head.png")
        # Images, text, etc...
        self.background = self.c.create_rectangle(0, 0, self.width,
                                                  self.height, fill="#606060",
                                                  outline="#606060")
        self.ldoor = self.c.create_polygon(30, 100, 230, 150, 230,
                                           self.height - 150,
                                           30, self.height - 100,
                                           fill="#000000")
        self.rdoor = self.c.create_polygon(self.width - 30, 100,
                                           self.width - 230, 150,
                                           self.width - 230, self.height - 150,
                                           self.width - 30, self.height - 100,
                                           fill="#000000")
        self.bowlyhead = self.c.create_image(self.width / 2, self.height / 2,
                                             anchor="c", image=self.bowlyheadB,
                                             state="hidden")
        self.camm = PhotoImage(file="cammap.png")
        self.cama = PhotoImage(file="camA.png")
        self.bowlycama = PhotoImage(file="camAbowly.png")
        self.currentcam = self.c.create_image(0, 0, anchor="nw",
                                              image=self.cama, state="hidden")
        self.electext = self.c.create_text(15, 45, anchor="nw", text="100%")
        self.text = self.c.create_text(15, 15, anchor="nw", text="12:00")
        self.cammap = self.c.create_image(self.width - 200, self.height - 200,
                                          anchor="se", image=self.camm,
                                          state="hidden")
        self.icon = PhotoImage(file="camera_icon.png")
        self.camicon = self.c.create_image(self.width - (self.width / 6),
                                           self.height - self.height / 9,
                                           anchor="se", image=self.icon,
                                           state="normal")
        self.c.tag_bind(self.camicon, "<Enter>", self.cams_on)
        self.incama = False
        self.c.tag_bind(self.camicon, "<Leave>", self.cams_off)
        self.root.bind("<Motion>", self.motion)
        self.root.bind("a", self.closeleft)
        self.root.bind("d", self.closeright)
        self.root.bind("<Escape>", self.kr)
        self.root.after(10, self.eachcsec)
        self.root.mainloop()

    def closeleft(self, event=None):
        if not self.ldoor_closed:
            self.ldoor_closed = True
            self.c.itemconfig(self.ldoor, fill="#505050")
            self.usage += 1
        else:
            self.ldoor_closed = False
            self.c.itemconfig(self.ldoor, fill="#000000")
            self.usage -= 1

    def closeright(self, event=None):
        if not self.rdoor_closed:
            self.rdoor_closed = True
            self.c.itemconfig(self.rdoor, fill="#505050")
            self.usage += 1

        else:
            self.rdoor_closed = False
            self.c.itemconfig(self.rdoor, fill="#000000")
            self.usage -= 1

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
                self.usage += 1
                self.camson = True
            else:
                self.c.itemconfig(self.currentcam, state="hidden")
                self.c.itemconfig(self.cammap, state="hidden")
                self.usage -= 1
                self.camson = False

    def eachcsec(self):
        self.sec += 1
        self.electricity2 += 1
        if self.sec % 187 == 0:
            self.min += 15
        if self.min % 60 == 0:
            self.hour += int(self.min / 60)
            self.min = 0
        self.c.itemconfig(self.text,
                          text="{0}:{1}".format(self.hour, self.min))
        self.c.itemconfig(self.electext,
                          text="{0}%   :    {1} U".format(self.electricity,
                                                          self.usage))
        self.bowlyattack = randint(0, 825)
        if self.bowlyattack == 5:
            self.c.itemconfig(self.currentcam, image=self.bowlycama)
            self.incama = True
        if self.incama:
            self.bowlyattack2 = randint(0, 675)
        if (self.incama and self.bowlyattack2 == 5 and not self.rdoor_closed)\
                or self.death:
            self.c.itemconfig(self.currentcam, state="hidden")
            self.c.itemconfig(self.cammap, state="hidden")
            self.c.itemconfig(self.bowlyhead, state="normal")
            self.root.after(3000, self.game_over_screen)
        elif self.rdoor_closed and self.bowlyattack2 == 5:
            self.incama = False
            self.c.itemconfig(self.currentcam, image=self.cama)
        if not self.youhavewon:
            self.root.after(10, self.eachcsec)
        if self.hour == 24:
            self.WIN()

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
        self.root.after(500, self.kr)

    def WIN(self, event=None):
        self.youhavewon = True
        self.c.create_rectangle(0, 0, self.width, self.height, fill="#000000")
        self.c.tag_unbind(self.camicon, "<Enter>")
        self.c.tag_unbind(self.camicon, "<Leave>")
        self.c.create_text(self.width / 2, self.height / 2, anchor="c",
                           fill="#ffffff", text="24:00",
                           font=("Helvetica", 500))
        self.root.after(10000, self.kr)

        def hour_add(self):
            self.hour += 1
            self.c.itemconfig()


game = Main()
