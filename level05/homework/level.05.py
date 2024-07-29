import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a turtle for drawing the castle
castle = turtle.Turtle()
castle.speed(10)
castle.color("black")

def draw_rectangle(t, width, height):
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_square(t, size):
    draw_rectangle(t, size, size)

def draw_triangle(t, size):
    t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()

def draw_door(t, width, height):
    t.color("brown")
    draw_rectangle(t, width, height)
    t.color("black")

def draw_window(t, size):
    t.color("lightblue")
    draw_square(t, size)
    t.color("black")

# Draw the main part of the castle
castle.penup()
castle.goto(-100, -100)
castle.pendown()
castle.color("gray")
draw_rectangle(castle, 200, 150)

# Draw the towers
tower_width = 40
tower_height = 100
castle.penup()
castle.goto(-140, 50)
castle.pendown()
draw_rectangle(castle, tower_width, tower_height)

castle.penup()
castle.goto(100, 50)
castle.pendown()
draw_rectangle(castle, tower_width, tower_height)

# Draw the roofs of the towers
castle.color("red")
castle.penup()
castle.goto(-140, 150)
castle.pendown()
draw_triangle(castle, tower_width)

castle.penup()
castle.goto(100, 150)
castle.pendown()
draw_triangle(castle, tower_width)

# Draw the door
castle.penup()
castle.goto(-30, -100)
castle.pendown()
draw_door(castle, 60, 80)

# Draw windows
castle.penup()
castle.goto(-80, -40)
castle.pendown()
draw_window(castle, 30)

castle.penup()
castle.goto(50, -40)
castle.pendown()
draw_window(castle, 30)

# Create turtles for the king and queen
king = turtle.Turtle()
king.shape("turtle")
king.color("blue")
king.penup()
king.goto(-50, 200)

queen = turtle.Turtle()
queen.shape("turtle")
queen.color("pink")
queen.penup()
queen.goto(50, 200)

# Add decorations
def draw_circle(t, radius):
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw the sun
castle.penup()
castle.goto(-250, 200)
castle.pendown()
castle.color("yellow")
draw_circle(castle, 40)

# Draw some flowers
castle.color("red")
for x in range(-200, 201, 40):
    castle.penup()
    castle.goto(x, -160)
    castle.pendown()
    draw_circle(castle, 10)

# Hide the drawing turtle
castle.hideturtle()

# Keep the window open
screen.mainloop()