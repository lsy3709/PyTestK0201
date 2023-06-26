import turtle

# Create a screen and set it up
screen = turtle.Screen()
screen.title("Python Turtle Image")
screen.bgcolor("white")

# Load the image
image_path = "라바1.gif"
screen.register_shape(image_path)

# Create a turtle and set its shape to the image
image_turtle = turtle.Turtle()
image_turtle.shape(image_path)

# Move the turtle to a specific position on the screen
image_turtle.penup()
image_turtle.goto(0, 0)
image_turtle.pendown()

# Hide the turtle so it doesn't obstruct the image
image_turtle.hideturtle()

# Exit on click
screen.exitonclick()
