# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

# Your code here.
def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')
    
    brad = turtle.Turtle()
    
    for _ in range(24): 
        for __ in range(4):
            brad.forward(100)
            brad.right(90)
        brad.left(15)
    
    '''
    deeper = turtle.Turtle()
    deeper.shape('arrow')
    deeper.color('yellow')
    for _ in range(4):
        deeper.left(120)
        deeper.forward(100)
    
    leelee = turtle.Turtle()
    leelee.shape('turtle')
    leelee.color('white')
    leelee.circle(100)
    '''
    window.exitonclick()
    
draw_square()