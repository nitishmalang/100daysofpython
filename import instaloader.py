#import instaloader

#run = instaloader.Instaloader()

#acc = 'sachintendulkar'

#run.download_profile(acc, profile_pic_only = True)

import turtle

turtle.speed(3)

turtle.pensize(3)

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color('black', 'red')

turtle.begin_fill()

turtle.left(140)
turtle.forward(111.65)

func()
turtle.left(120)
func()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
turtle.done()