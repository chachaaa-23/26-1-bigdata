import turtle


class MyTurtle:
    # All turtle objects share the same angle.
    shared_angle = 45

    def __init__(self, color):
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color(color)

    def walk(self, distance):
        self.t.forward(distance)
        self.t.right(MyTurtle.shared_angle)


t1 = MyTurtle("red")
t2 = MyTurtle("blue")
t3 = MyTurtle("green")

for _ in range(100):
    t1.walk(80)
    t2.walk(60)
    t3.walk(40)

# Keep the turtle window open.
turtle.mainloop()
