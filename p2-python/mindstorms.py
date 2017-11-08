import turtle

def draw_square(paint):
    for i in range(4):
        paint.forward(100)
        paint.right(90)

def draw_pic():
    window  = turtle.Screen()
    window.bgcolor('red')
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(5)
    for i in range(36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_pic()
