__author__ = 'ajtutor'
import turtle

t = turtle.Turtle()

class Sierpinski:

    def __init__(self, size=400, turtle=t, color1="#000000", color2="#FFFFFF"):
        self.size = size
        self.turtle = turtle
        self.color1 = color1
        self.color2 = color2
        self.turtle.color(self.color1, self.color2)


    def drawTriangle(self, size=0, shade=None):
        if size==0:
            size=self.size

        if shade is None:
            shade = self.color2

        self.turtle.fillcolor(shade)
        self.turtle.begin_fill()
        for i in range(3):
            self.turtle.forward(size)
            self.turtle.left(120)
        self.turtle.end_fill()



    def clear(self):
        self.turtle.clear()

    def sierpinski(self):
        self.doSierpinski(self.size)

    def doSierpinski(self, size, count=5):
        if count>0:
            half = size/2
            self.drawTriangle(size)
            self.doSierpinski(half, count-1)
            self.turtle.forward(half)
            self.doSierpinski(half, count-1)
            self.turtle.left(60)
            self.drawTriangle(half, self.color1)
            self.turtle.left(60)
            self.turtle.forward(half)
            self.turtle.right(120)
            self.doSierpinski(half, count-1)
            self.turtle.left(60)
            self.turtle.back(half)
            self.turtle.right(60)