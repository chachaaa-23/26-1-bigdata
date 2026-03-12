import turtle


# Draw a square by repeating the same move four times.
def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)


t = turtle.Turtle()
t.shape("turtle")

draw_square(t, 100)

# Keep the turtle window open.
turtle.mainloop()
