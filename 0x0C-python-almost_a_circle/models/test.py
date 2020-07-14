#!/usr/bin/python3
import turtle
import tkinter
from tkinter import *       
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x * 1.2)
   my_pen.left(75)
