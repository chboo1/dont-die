from __future__ import division
from tkinter import Tk, Canvas, PhotoImage
from random import randint


class Main():
    def __init__(self):
        # Screen, Canvas, etc...
        self.root = Tk()
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.wd = self.width / 1920
        self.hd = self.width / 1080
        self.c = Canvas(self.root, width=self.width, height=self.height)
        self.root.geometry("{0}x{1}".format(self.width, self.height))
        self.root.title("Don't die")
        self.bowlyattack2 = 0
        self.c.pack()
        # initiation of variables
        self.powergenerator = False
        self.youhavewon = False
        self.electricity = 100
        self.electricity2 = 0
        self.sec = 0
        self.min = 0
        self.hour = 0
        self.usage = 0
        self.dead = False
        self.camson = False
        self.rdoor_closed = False
        self.ldoor_closed = False
        self.fdoor_closed = False
        self.left = True
        self.hour = 12
        self.attackTimer = 0
        self.currentcamvar = "A"
        # Image references 'yay'
        self.bowlybodyB = PhotoImage(file="bowly_chains.png")
        # Unused line /\
        #             |
        #             |
        self.bowlyheadB = PhotoImage(file="bowly_head.png")
        self.camm = PhotoImage(file="cammap.png")
        self.cama = PhotoImage(file="camA.png")
        self.bowlycama = PhotoImage(file="camAbowly.png")
        self.camb = PhotoImage(file="camB.png")
        self.camTransferImg = PhotoImage(file="camTransfer.png")
        self.bowlyTimer = 0
        self.levelBowly = 1
        # Sound references
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
        self.fdoor = self.c.create_rectangle(self.width / 2 - 100, 150, self.width / 2 + 100, self.height - 100, fill="#000000", outline="#000000")
        self.bowlyhead = self.c.create_image(self.width / 2, self.height / 2,
                                             anchor="c", image=self.bowlyheadB,
                                             state="hidden")
        self.currentcam = self.c.create_image(0, 0, anchor="nw",
                                              image=self.cama, state="hidden")
        self.electext = self.c.create_text(15, 45, anchor="nw", text="100%")
        self.text = self.c.create_text(15, 15, anchor="nw", text="12:00")
        self.cammap = self.c.create_image(900, self.height,
                                          anchor="se", image=self.camm,
                                          state="hidden")
        self.icon = PhotoImage(file="camera_icon.png")
        self.camicon = self.c.create_image(self.width - (self.width / 6),
                                           self.height - self.height / 9,
                                           anchor="se", image=self.icon,
                                           state="normal")
        self.camaicon = self.c.create_rectangle(740, 880, 830, 940,
                                                fill="#808080",
                                                outline="#000000",
                                                activeoutline="#ffffff",
                                                state="hidden")
        self.cambicon = self.c.create_rectangle(160, 880, 250, 940,
                                                fill="#808080",
                                                outline="#000000",
                                                activeoutline="#ffffff",
                                                state="hidden")
        self.c.tag_bind(self.camicon, "<Enter>", self.cams_on)
        self.incama = False
        self.c.tag_bind(self.camicon, "<Leave>", self.cams_off)
        self.root.bind("<space>", lambda e: self.cams_on(e))
        self.root.bind("<Motion>", self.motion)
        self.root.bind("s", self.solarpanel)
        self.root.bind("a", self.closeleft)
        self.root.bind("d", self.closeright)
        self.root.bind("w", self.closefront)
        self.root.bind("<Escape>", self.kr)
        self.root.bind("<Button-1>", self.click)
        self.c.tag_bind(self.camaicon, "<Button-1>",
                        lambda e: self.camTransfer("A"))
        self.c.tag_bind(self.cambicon, "<Button-1>",
                        lambda e: self.camTransfer("B"))
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

    def closefront(self, event=None):
        if not self.fdoor_closed:
            self.fdoor_closed = True
            self.c.itemconfig(self.fdoor, fill="#505050", outline="#505050")
            self.usage += 1
        else:
            self.fdoor_closed = False
            self.c.itemconfig(self.fdoor, fill="#000000", outline="#000000")
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
                self.c.itemconfig(self.camaicon, state="normal")
                self.c.itemconfig(self.cambicon, state="normal")
                self.usage += 1
                self.camson = True
            else:
                self.c.itemconfig(self.currentcam, state="hidden")
                self.c.itemconfig(self.cammap, state="hidden")
                self.c.itemconfig(self.camaicon, state="hidden")
                self.c.itemconfig(self.cambicon, state="hidden")
                self.usage -= 1
                self.camson = False
            self.cams_off()

    def eachcsec(self):
        if self.incama is True:
            self.attackTimer += 1
        self.sec += 1
        self.electricity2 += 1
        if self.electricity2 % \
                int((150 + self.powergenerator) / ((self.usage * 2) + 1)) == 0:
            self.electricity -= 1
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
        self.bowlyTimer += 1
        if self.bowlyTimer == 150:
            self.bowlyTimer = 0
            _bowlyTimer = randint(0, 11 - self.levelBowly)
            _bowlyTimer2 = randint(0, 6 - max(0, self.levelBowly))
            if not self.incama:
                if _bowlyTimer == 5:
                        if self.currentcamvar == "A":
                            self.c.itemconfig(self.currentcam, image=self.bowlycama)
                        self.incama = True
            else:
                if _bowlyTimer == 2:
                    if not self.rdoor_closed:
                        self.c.itemconfig(self.currentcam, state="hidden")
                        self.c.itemconfig(self.camaicon, state="hidden")
                        self.c.itemconfig(self.cambicon, state="hidden")
                        self.c.itemconfig(self.cammap, state="hidden")
                        self.c.itemconfig(self.bowlyhead, state="normal")
                        self.root.after(3000, self.game_over_screen)
                    else:
                        self.incama = False
                        if self.currentcamvar == "A":
                            self.c.itemconfig(self.currentcam, image=self.cama)
        if self.electricity < 0 or self.electricity > 120:
            self.youhavewon = True
            if self.electricity >= 120:
                self.flash = self.c.create_rectangle(0, 0,
                                                     self.width, self.height,
                                                     fill="#ff0000")
                i = 1
                while i < 20:
                    self.c.itemconfig(self.flash, fill="#ffffff")
                    self.c.update()
                    i += 1
                    self.c.itemconfig(self.flash, fill="#ff0000")
                    self.c.update()
                self.c.itemconfig(self.flash, fill="#ffffff")
                self.c.update()
                self.c.itemconfig(self.flash, fill="#ff0000")
                self.c.update()
                self.c.itemconfig(self.flash, fill="#ffffff")
                self.c.update()
                self.c.itemconfig(self.flash, fill="#ff0000")
                self.c.update()
                self.c.itemconfig(self.flash, fill="#ffffff")
                self.c.update()
                self.c.itemconfig(self.flash, fill="#ff0000")
                self.c.update()
                self.c.itemconfig(self.flash, fill="#000000")
                self.c.update()
            self.c.itemconfig(self.electext)
            self.rdoor_closed = True
            self.ldoor_closed = True
            self.closeleft(event=None)
            self.closeright(event=None)
            self.c.itemconfig(self.electext,
                              text="0%    :    0 U")
            self.root.after(20000, self.death)
        if not self.youhavewon:
            self.root.after(10, self.eachcsec)

        if self.hour == 24:
            self.WIN()

    def cams_off(self, event=None):
        self.left = True

    def motion(self, event):
        self.x = event.x
        self.y = event.y

    def death(self):
        self.c.itemconfig(self.currentcam, state="hidden")
        self.c.itemconfig(self.cammap, state="hidden")
        self.c.itemconfig(self.bowlyhead, state="normal")
        self.c.tag_unbind(self.camicon, "<Enter>")
        self.c.tag_unbind(self.camicon, "<Leave>")
        self.root.after(3000, self.game_over_screen)

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

    def solarpanel(self, event=None):
        if self.powergenerator == 0:
            self.powergenerator = 100
        else:
            self.powergenerator = 0

    def click(self, event=None):
        pass

    def changeCamera(self, camera):
        if camera == "A":
            self.currentcamvar = "A"
            if self.incama:
                self.c.itemconfig(self.currentcam, image=self.bowlycama)
            else:
                self.c.itemconfig(self.currentcam, image=self.cama)
        elif camera == "B":
            self.currentcamvar = "B"
            self.c.itemconfig(self.currentcam, image=self.camb)

    def camTransfer(self, camera):
        self.c.itemconfig(self.currentcam, image=self.camTransferImg)
        self.c.update()
        self.root.after(100, lambda: self.changeCamera(camera))


game = Main()
