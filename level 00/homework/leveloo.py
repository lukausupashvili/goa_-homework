from turtle import *


#we want paint a hause

#step 1; draw a square
speed(5)
color("blue")
width(7)
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawving a door



forward(70) 
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(20,140)
pendown()

left(120)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)

penup()
goto(180,140)
pendown()

right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)


exitonclick()