from turtle import *

print("Hello, first commit!")
print("Second commit!")

pensize(10)

right(90)

for i in range(90):
    forward(2)
    left(2)

penup()
goto(40,40)
pendown()
forward(30)

penup()
goto(80,40)
pendown()
forward(30)

exitonclick()
