from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape('turtle')
the_turtle.color('green')

def designer():
    the_turtle.speed(10)
    for i in range(4):
        the_turtle.forward(100)
        the_turtle.right(90)
        
    for x in range(4):
        the_turtle.forward(100)
        the_turtle.left(90)
        
    for x in range(4):
        the_turtle.forward(200)
        the_turtle.left(90)

    for i in range(4):
        the_turtle.forward(200)
        the_turtle.right(90)
        
    for i in range(4):
        the_turtle.forward(300)
        the_turtle.right(90)
        
    for x in range(4):
        the_turtle.forward(300)
        the_turtle.left(90)



def lado_direito():
    designer()

def lado_esquerdo():
    the_turtle.left(180)
    designer()
    

lado_direito()
lado_esquerdo()

screen = Screen()
screen.exitonclick()