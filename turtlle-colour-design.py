import turtle
import colors
import random
import math

turtle.shape("turtle")
turtle.speed(0)
turtle.fillcolor("yellow") 
turtle.pencolor("red") 
turtle.begin_fill()
for _ in range(36):  
  turtle.forward(200)
  turtle.left(170)
turtle.end_fill()
turtle.done()
