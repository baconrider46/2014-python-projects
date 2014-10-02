from turtle import Turtle
from random import random

def random_color():
    return(random(),random(),random())

nibles = Turtle()
nibles.pensize(7)
nibles.speed(0)
for counter in range(1,200):
    nibles.pencolor(random_color())
    nibles.right(10)
    nibles.left(20)
    nibles.backward(1)
    nibles.forward(10)
    nibles.right(100)
    nibles.left(100)
