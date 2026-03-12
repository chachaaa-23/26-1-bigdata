import turtle

# Create one turtle for drawing and writing.
t = turtle.Turtle()
t.shape("turtle")

# Write a short message.
t.write("Hello", move=False, align="left", font=("Arial", 12, "normal"))

# Change the turtle color and move to another position.
t.color("blue")
t.goto(100, 100)

# Keep the turtle window open.
turtle.mainloop()
