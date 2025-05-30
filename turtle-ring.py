import turtle

def draw_triangle(x):
  for i in range(1000):
    turtle.speed(0)
    turtle.forward(x)
    turtle.left(120)
    turtle.left(3.14159)
    
draw_triangle(200)