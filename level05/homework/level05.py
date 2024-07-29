import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a turtle for drawing the palace
palace = turtle.Turtle()
palace.speed(3)
palace.color("brown")

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

# Draw the main part of the palace
palace.penup()
palace.goto(-100, -100)
palace.pendown()
draw_rectangle(palace, 200, 100)

# Draw the roof
palace.penup()
palace.goto(-120, 0)
palace.pendown()
palace.color("red")
draw_triangle(palace, 240)

# Draw the door
palace.penup()
palace.goto(-30, -100)
palace.pendown()
palace.color("brown")
draw_rectangle(palace, 60, 80)

# Draw windows
palace.penup()
palace.goto(-80, -40)
palace.pendown()
palace.color("blue")
draw_square(palace, 30)

palace.penup()
palace.goto(20, -40)
palace.pendown()
draw_square(palace, 30)

# Create turtles for the king and queen
king = turtle.Turtle()
king.shape("turtle")
king.color("blue")
king.penup()
king.goto(-50, 100)

queen = turtle.Turtle()
queen.shape("turtle")
queen.color("pink")
queen.penup()
queen.goto(50, 100)

# Add decorations
def draw_circle(t, radius):
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw the sun
palace.penup()
palace.goto(-200, 200)
palace.pendown()
palace.color("yellow")
draw_circle(palace, 40)

# Draw some flowers
palace.penup()
palace.goto(-200, -150)
palace.pendown()
palace.color("red")
draw_circle(palace, 10)

palace.penup()
palace.goto(-180, -140)
palace.pendown()
palace.color("yellow")
draw_circle(palace, 10)

palace.penup()
palace.goto(-160, -150)
palace.pendown()
palace.color("red")
draw_circle(palace, 10)

palace.penup()
palace.goto(180, -150)
palace.pendown()
palace.color("yellow")
draw_circle(palace, 10)

palace.penup()
palace.goto(160, -140)
palace.pendown()
palace.color("red")
draw_circle(palace, 10)

palace.penup()
palace.goto(140, -150)
palace.pendown()
palace.color("yellow")
draw_circle(palace, 10)

# Hide the drawing turtle
palace.hideturtle()

# Keep the window open
screen.mainloop()