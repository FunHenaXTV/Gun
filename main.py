import tkinter as tk
from random import randint
from math import tan

class Ball():
    def __init__(self):
        self.ball = canvas.create_oval(10, 10, 80, 80, outline='#fff', fill='#fff')


class Gun():
    def __init__(self):
        self.gun = canvas.create_line(0, 500, 100, 450, width=5, fill='green')
        self.length = 100

    def motion(self, event):
        self.event_motion = event
        tg = tan((500-event.y)/event.x)
        x = (self.length**2/(1+tg**2))**0.5
        y = tg * (self.length**2/(1+tg**2))**0.5
        canvas.coords(self.gun, 0, 500, x, 500-y)

    def handler1(self, event):
        self.event_scale_up = event
        self.scale_up()

    def handler2(self, event):
        self.event_cancel_scale_up = event
        self.cancel_scale_up()

    def scale_up(self):
        self.length += 0.1
        tg = tan((500-self.event_motion.y)/self.event_motion.x)
        x = (self.length**2/(1+tg**2))**0.5
        y = tg * (self.length**2/(1+tg**2))**0.5
        canvas.coords(self.gun, 0, 500, x, 500-y)
        self.loop = root.after(5, self.scale_up)

    def cancel_scale_up(self):
        root.after_cancel(self.loop)
        self.length = 100
        tg = tan((500-self.event_motion.y)/self.event_motion.x)
        x = (self.length**2/(1+tg**2))**0.5
        y = tg * (self.length**2/(1+tg**2))**0.5
        canvas.coords(self.gun, 0, 500, x, 500-y)        



root = tk.Tk()
root.geometry('500x500')
canvas = tk.Canvas(root, width=500, height=500, bg='#fff')
canvas.pack()
gun = Gun()

root.bind('<Motion>', gun.motion)
root.bind('<Button-1>', gun.handler1)
root.bind('<ButtonRelease-1>', gun.handler2)

root.mainloop()

