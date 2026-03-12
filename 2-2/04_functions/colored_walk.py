import turtle


# Walk with matching colors and distances.
def colored_walk(t, colors, distances):
    steps = min(len(colors), len(distances))

    for i in range(steps):
        t.color(colors[i])
        t.forward(distances[i])
        t.right(90)


t = turtle.Turtle()
t.shape("turtle")

colors = ["red", "blue", "green", "orange"]
distances = [50, 80, 40, 60]

colored_walk(t, colors, distances)

# Keep the turtle window open.
turtle.mainloop()
