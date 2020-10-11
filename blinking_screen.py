import turtle

turtle.pensize(600)
turtle.speed(0)
for i in range(100):
  for colours in ["yellow","red","cyan","blue","black","green","white"]:
    turtle.color(colours)
    turtle.circle(100)
    turtle.left(10)
turtle.hideturtle()
