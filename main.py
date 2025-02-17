import tkinter as tk
import time
import random
from random import randint

idle_num =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #12
sleep_num = [19, 20, 21, 22, 23, 24, 25] #26
walk_left = [13, 14, 15]
walk_right = [16, 17, 18]

class Ket:
    def __init__(self):
        self.window=tk.Tk()

        self.idle=[tk.PhotoImage(file='assets/idle1.png'), tk.PhotoImage(file='assets/idle2.png'), tk.PhotoImage(file='assets/idle3.png'), tk.PhotoImage(file='assets/idle4.png')]

        self.idle_to_sleeping=[tk.PhotoImage(file='assets/sleeping1.png'), tk.PhotoImage(file='assets/sleeping2.png'), tk.PhotoImage(file='assets/sleeping3.png'), tk.PhotoImage(file='assets/sleeping4.png'), tk.PhotoImage(file='assets/sleeping5.png'), tk.PhotoImage(file='assets/sleeping6.png')]

        self.sleeping=[tk.PhotoImage(file='assets/zzz1.png'), tk.PhotoImage(file='assets/zzz2.png'), tk.PhotoImage(file='assets/zzz3.png'), tk.PhotoImage(file='assets/zzz4.png')]

        self.sleeping_to_idle=[tk.PhotoImage(file='assets/sleeping6.png'), tk.PhotoImage(file='assets/sleeping5.png'), tk.PhotoImage(file='assets/sleeping4.png'), tk.PhotoImage(file='assets/sleeping3.png'), tk.PhotoImage(file='assets/sleeping2.png'), tk.PhotoImage(file='assets/sleeping1.png')]

        self.walking_left=[tk.PhotoImage(file='assets/walkingleft1.png'), tk.PhotoImage(file='assets/walkingleft2.png'), tk.PhotoImage(file='assets/walkingleft3.png'), tk.PhotoImage(file='assets/walkingleft4.png')]

        self.walking_right=[tk.PhotoImage(file='assets/walkingright1.png'), tk.PhotoImage(file='assets/walkingright2.png'), tk.PhotoImage(file='assets/walkingright3.png'), tk.PhotoImage(file='assets/walkingright4.png') ]

        self.x= 1600
        self.y= 975

        self.i_frame=0
        self.state=1
        self.event_number=randint(1, 3)

        self.frame=self.idle[0]

        self.window.config(highlightbackground='black')
        self.label = tk.Label(self.window,bd=0,bg='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor','black')

        self.label.pack()

        self.window.after(1, self.update, self.i_frame, self.state, self.event_number, self.x)
        self.window.mainloop()


    def event(self, i_frame, state, event_number, x): ## add some global timer for each animation
        if self.event_number in idle_num: ## if the current idle timer > the allotted time 
            self.state=0
            self.window.after(400, self.update, self.i_frame, self.state, self.event_number, self.x)
        elif self.event_number==12:
            self.state=1
            self.window.after(100, self.update, self.i_frame, self.state, self.event_number, self.x)
        elif self.event_number in walk_left:
            self.state=4
            self.window.after(100, self.update, self.i_frame, self.state, self.event_number, self.x)
        elif self.event_number in walk_right:
            self.state=5
            self.window.after(100, self.update, self.i_frame, self.state, self.event_number, self.x)
        elif self.event_number in sleep_num:
            self.state=2
            self.window.after(400,self.update, self.i_frame, self.state, self.event_number, self.x)
        elif self.event_number == 26:
            self.state = 3
            self.window.after(100, self.update, self.i_frame, self.state, self.event_number, self.x)

        

    def animate(self, i_frame, array, event_number, a, b):
        if self.i_frame<len(array)-1:
            self.i_frame+=1
        else:
            self.i_frame=0
            self.event_number=randint(a, b)
        return self.i_frame, self.event_number

    def update(self, i_frame, state, event_number, x):
    
        if self.state == 0:
            self.frame=self.idle[self.i_frame]
            self.i_frame, self.event_number=self.animate(self.i_frame, self.idle, self.event_number, 1, 18)
        elif state == 1:
            self.frame = self.idle_to_sleeping[self.i_frame]
            self.i_frame, self.event_number = self.animate(self.i_frame, self.idle_to_sleeping, self.event_number,19, 19)
        elif self.state == 2:
            self.frame = self.sleeping[self.i_frame]
            self.i_frame, self.event_number = self.animate(self.i_frame, self.sleeping, self.event_number, 19, 26)
        elif self.state == 3:
            self.frame = self.sleeping_to_idle[self.i_frame]
            self.i_frame, self.event_number=self.animate(self.i_frame, self.sleeping_to_idle, self.event_number, 1, 1)
        elif self.state == 4 and self.x>0:
            self.frame=self.walking_left[self.i_frame]
            self.i_frame, self.event_number=self.animate(self.i_frame, self.walking_left, self.event_number, 1, 18)
            self.x-=3
        elif self.state == 5:
            self.frame=self.walking_right[self.i_frame]
            self.i_frame, self.event_number=self.animate(self.i_frame, self.walking_right, self.event_number, 1, 18)
            self.x+=3

        self.window.geometry('72x64+'+str(self.x)+'+'+str(self.y))
        self.label.configure(image=self.frame)
        self.window.after(1, self.event, self.i_frame, self.state, self.event_number, self.x)

ket=Ket()      
