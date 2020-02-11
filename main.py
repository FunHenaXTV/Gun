import tkinter as tk
from random import randint
from math import tan

class Bullet():
    def __init__(self, x, y, power):
        self.ball = canvas.create_oval(x, y, x+30+power/3, y-30-power/3, outline='red', fill='#fff', width=5)
        self.speed = 2000/power
        self.speed_x = 3
        self.speed_y = -3
        self.move()



    def move(self):
        canvas.move(self.ball, self.speed_x, self.speed_y)
        self.collision()
        root.after(int(self.speed), self.move)

    def collision(self):
        if 500 - canvas.coords(self.ball)[2] < 0.01 or canvas.coords(self.ball)[0] < 0.01 :
            self.speed_x = -self.speed_x

        if 500 - canvas.coords(self.ball)[3] < 0.01 or canvas.coords(self.ball)[1] < 0.01:
            self.speed_y = -self.speed_y



class Target():
    def __init__(self):
        self.y = []
        self.r = []
        self.targets = []
        rand_y = randint(100, 400)
        self.y.append(rand_y)
        rand_r = randint(10, 40)
        self.r.append(rand_r)
        self.speed = []
        rand_speed = randint(100, 400)/1000
        self.speed.append(rand_speed)
        for i in range(0, 5):
            while rand_y in self.y:
                rand_y = randint(100, 400)
            else:
                self.y.append(rand_y)

            while rand_r in self.r:
                rand_r = randint(10, 40)
            else:
                self.r.append(rand_r)

            while rand_speed in self.speed:
                rand_speed = randint(100, 400)/1000
            else:
                self.speed.append(rand_speed)

        for i in range(0, 5):
            self.targets.append(canvas.create_oval(400, self.y[i], 400+2*self.r[i], self.y[i]-2*self.r[i], outline='green', width=3))

        self.move()

    def move(self):
        for i in range(0, 5):
            canvas.move(self.targets[i], 0, self.speed[i])
        self.collision()
        root.after(1, self.move)

    def collision(self):
        for i in range(0, 5):
            if canvas.coords(self.targets[i])[1] < 2 or canvas.coords(self.targets[i])[3] > 498:
                self.speed[i] = -self.speed[i]

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
        tg = tan((500-self.event_motion.y)/self.event_motion.x)
        x = (self.length**2/(1+tg**2))**0.5
        y = tg * (self.length**2/(1+tg**2))**0.5
        bullet = Bullet(x, 500-y, self.length)
        self.length = 100
        x = (self.length**2/(1+tg**2))**0.5
        y = tg * (self.length**2/(1+tg**2))**0.5
        canvas.coords(self.gun, 0, 500, x, 500-y)




root = tk.Tk()
root.geometry('500x500')
canvas = tk.Canvas(root, width=500, height=500, bg='#fff')
canvas.pack()
gun = Gun()
target = Target()
root.bind('<Motion>', gun.motion)
root.bind('<Button-1>', gun.handler1)
root.bind('<ButtonRelease-1>', gun.handler2)

root.mainloop()

