import tkinter as tk
from random import randint
from math import tan
from tkinter import messagebox as mb
from computation import fast_tanh


class Bullet():
    def __init__(self, x, y, power):
        self.bullet = canvas.create_oval(x, y, x+20+power/3, y-20-power/3, fill='#'+gun.color)
        self.r = 10 + power/6
        self.speed = 2000/power
        self.speed_x = 3 + power/100
        if y < 250:
            self.speed_y = -3 + power/100
        else:
            self.speed_y = 3 - power/100
        self.collision_amount = 0
        self.move()



    def move(self):
        canvas.move(self.bullet, self.speed_x, self.speed_y)
        self.speed_y += 0.1
        self.collision()
        
        if self.collision_amount == 4:
            self.delete()

        self.loop = root.after(int(self.speed), self.move)

    def delete(self):
        root.after_cancel(self.loop)
        canvas.delete(self.bullet)
        del gun.bullets[gun.bullets.index(self)]
        self.speed = 1100000

    def collision(self):
        if 500 - canvas.coords(self.bullet)[2] < 0.01 or canvas.coords(self.bullet)[0] < 0.01 :
            self.speed_x = -self.speed_x
            self.collision_amount += 1

        if 500 - canvas.coords(self.bullet)[3] < 0.01 or canvas.coords(self.bullet)[1] < 0.01:
            self.speed_y = -self.speed_y
            self.collision_amount += 1



class Target():
    def __init__(self):
        self.y = []
        self.r = []
        self.targets = []
        self.score = 0
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
            canvas.move(self.targets[i], 0, self.speed[i]*10)
        self.wall_collision()
        self.bullet_collision()
        if self.score == 5:
            game_over()
        root.after(10, self.move)

    def wall_collision(self):
        for i in range(0, 5):
            if self.targets[i] != 'DELETED':
                if canvas.coords(self.targets[i])[1] < 2 or canvas.coords(self.targets[i])[3] > 498:
                    self.speed[i] = -self.speed[i]

    def bullet_collision(self):
        for i in range(0, 5):
            for j in range(0, len(gun.bullets)):
                if (self.targets[i] != 'DELETED'):
                    x1 = canvas.coords(self.targets[i])[0] + self.r[i]
                    y1 = canvas.coords(self.targets[i])[3] + self.r[i]
                    x2 = canvas.coords(gun.bullets[j].bullet)[0] + gun.bullets[j].r
                    y2 = canvas.coords(gun.bullets[j].bullet)[3] + gun.bullets[j].r                  

                    if ((x1 - x2)**2 + (y1 - y2)**2)**0.5 - self.r[i] - gun.bullets[j].r < 3.5:
                        self.delete(i)
                        self.score += 1


    def delete(self, i):
        canvas.delete(self.targets[i])
        self.targets[i] = 'DELETED'


class Gun():
    def __init__(self):
        self.create_random_color()
        self.gun = canvas.create_line(0, 250, 50, 150, width=5, fill='#000')
        self.length = 100
        self.bullets = []
        self.end_game_position = 0
        self.bullet_amount = 0

    def motion(self, event):
        self.event_motion = event
        try:
            s = fast_tanh(event.x, event.y, self.length)
            x = s // 10000
            y = s % 1000
            canvas.coords(self.gun, 0, 250, x, y)
        except:
            pass

    def create_random_color(self):
        self.color = ''
        for i in range(0, 6):
            a = randint(0, 15)
            if a == 10:
                a = 'A'
            elif a == 11:
                a = 'B'
            elif a == 12:
                a = 'C'
            elif a == 13:
                a = 'D'
            elif a == 14:
                a = 'E'
            elif a == 15:
                a = 'F'
            self.color += str(a)

    def handler1(self, event):
        self.event_scale_up = event
        self.scale_up()

    def handler2(self, event):
        self.event_cancel_scale_up = event
        self.cancel_scale_up()

    def scale_up(self):
        canvas.itemconfig(self.gun, fill='#'+self.color)
        self.length += 0.3
        try:
            s = fast_tanh(self.event_motion.x, self.event_motion.y, self.length)
            x = s // 10000
            y = s % 1000
            canvas.coords(self.gun, 0, 250, x, y)
        except:
            pass
        self.loop = root.after(5, self.scale_up)

    def cancel_scale_up(self):
        root.after_cancel(self.loop)
        canvas.itemconfig(self.gun, fill='#000')
        try:
            s = fast_tanh(self.event_motion.x, self.event_motion.y, self.length)
            x = s // 10000
            y = s % 1000
            canvas.coords(self.gun, 0, 250, x, y)
        except:
            pass
        if self.end_game_position == 0:
            self.bullets.append(Bullet(x, y, self.length))
            self.bullet_amount += 1
        self.create_random_color()
        self.length = 100
        try:
            s = fast_tanh(self.event_motion.x, self.event_motion.y, self.length)
            x = s // 10000
            y = s % 1000
            canvas.coords(self.gun, 0, 250, x, y)
        except:
            pass

    def end_game(self):
        self.end_game_position = 1

def game_over():
    canvas.delete(gun.gun)
    gun.end_game()
    for i in range(0, len(gun.bullets)):
        if gun.bullets[i] != 'DELETED':
            canvas.delete(gun.bullets[i])
    length = gun.bullet_amount
    if length == 1:
        text = canvas.create_text(250, 250, text='Вы уничтожили все цели за ' + str(gun.bullet_amount) + ' выстрел', font='Ubuntu 16')
    elif length >= 2 and length <= 4:
        text = canvas.create_text(250, 250, text='Вы уничтожили все цели за ' + str(gun.bullet_amount) + ' выстрела', font='Ubuntu 16')
    else:
        text = canvas.create_text(250, 250, text='Вы уничтожили все цели за ' + str(gun.bullet_amount) + ' выстрелов', font='Ubuntu 16')


score = 0
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

