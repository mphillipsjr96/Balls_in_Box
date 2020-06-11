from vpython import *
import random
import string
box = box(size = vector(100,100,100), pos = vector(0,0,0), color = color.blue, opacity = 0.2)

class Ball:
    def __init__(self, mouseP):
        self.ball = sphere(pos = mouseP, radius = random.randrange(1,5), color = color.red, emissive = True)
        self.g = vector(0,-9.8,0)
        self.mass = self.ball.radius * 2

        self.ball.p = vector(random.randrange(-10,10),random.randrange(-10,10),random.randrange(-10,10))
        self.name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(4)])
    def update(self,dt,balls):
        self.ball.p = self.ball.p + self.g*dt
        self.ball.pos = self.ball.pos + (self.ball.p/self.mass)*dt
        if not (box.size.x/2 > self.ball.pos.x > -box.size.x/2):
            self.ball.p.x = -self.ball.p.x
        if not (box.size.y/2 > self.ball.pos.y > -box.size.y/2):
            self.ball.p.y = -self.ball.p.y
        if not (box.size.z/2 > self.ball.pos.z > -box.size.z/2):
            self.ball.p.z = -self.ball.p.z
        for ball in balls:
            if ball.name == self.name:
                continue
            if mag(self.ball.pos - ball.ball.pos) < (self.ball.radius+ball.ball.radius):
                self.ball.color = color.green
                ball.ball.color = color.green
                self.ball.p.z = -self.ball.p.z
                self.ball.p.y = -self.ball.p.y
                self.ball.p.x = -self.ball.p.x
                ball.ball.p.z = -ball.ball.p.z
                ball.ball.p.y = -ball.ball.p.y
                ball.ball.p.x = -ball.ball.p.x

balls = []

dt = 0.01
while True:
    rate(500)
    for ball in balls:
        ball.update(dt, balls)
    if random.randrange(0,1000,1) >= 999:
        balls.append(Ball(vector(random.randrange(-40,40),random.randrange(-40,40),random.randrange(-40,40))))