import tkinter as tk
from random import randint
from math import tan

class Ball():
	def __init__(self):
		self.ball = canvas.create_oval(10, 10, 80, 80, outline='#fff', fill='#fff')


class Gun():
	def __init__(self):
		self.gun = canvas.create_line(0, 500, 100, 450, width=5, fill='green')


	def motion(self, event):
		tg = tan((500-event.y)/event.x)
		l = 100
		x = (l**2/(1+tg**2))**0.5
		y = tg * (l**2/(1+tg**2))**0.5
		canvas.coords(self.gun, 0, 500, x, 500-y)


root = tk.Tk()
root.geometry('500x500')
canvas = tk.Canvas(root, width=500, height=500, bg='#fff')
canvas.pack()
gun = Gun()

root.bind('<Motion>', gun.motion)

root.mainloop()

