import turtle

# my_turtle=turtle.Turtle()

turtle.speed(1)
turtle.color("green")
turtle.fillcolor("red")
# tuple.shape("turtle")  not works sometime

turtle.forward(90)
turtle.right(90)
turtle.penup()
turtle.hideturtle()
turtle.forward(50)
turtle.pendown()
turtle.forward(90)
turtle.showturtle()

turtle.goto(1,58)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()


turtle.exitonclick()
turtle.done()
