import turtle
import time

# --- Setup ---
t = turtle.Turtle()
turtle.title("Heart Shape")
turtle.setup(width=600, height=600) # Set a fixed window size
turtle.bgcolor("black")
t.pensize(3) # A slightly smaller pen size looks cleaner
t.speed(8)  # Increase speed for faster drawing (1 is very slow)
t.color("red")

# --- 1. Draw and Fill the Heart ---
t.begin_fill()
t.fillcolor("red")
t.left(150)
t.forward(180)
t.circle(-90, 180)
t.setheading(60) # Note: setheading(60) correctly points the turtle for the second curve
t.circle(-90, 180)
t.forward(180)
t.end_fill()
t.hideturtle()

# --- 2. Write the Message ---
# Move the pen to a specific position for the text
t.penup()
t.goto(0, -100) # Move to the center bottom of the heart
t.pendown()
t.color("white") # Change color for visibility on a black background
msg="I LOVE YOU, BATAAAAA"
t.write(
    msg,
    align="center", # Center the text under the heart
    font=("Arial", 20, "bold") # Use "bold" instead of "italic" and "bold"
)

# --- 3. Keep the window open ---
turtle.done()