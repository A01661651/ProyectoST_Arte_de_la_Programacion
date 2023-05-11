"""
Snake, classic arcade game.

Ejercicios.

1. La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana

2. Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, 
pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0,0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aimf= vector(0, 1)
#############################################################
#Parte que sirve para color random de serpiente y alimento
azar1=randrange(5)
azar2=randrange(5)
if azar1==azar2:
    azar1 =randrange(5)
if azar1==0:
    pintura="blue"
if azar1==1:
    pintura="black"
if azar1==2:
    pintura="green"
if azar1==3:
    pintura="magenta"
if azar1==4:
    pintura="yellow"
if azar2==0:
    pintura2="blue"
if azar2==1:
    pintura2="black"
if azar2==2:
    pintura2="green"
if azar2==3:
    pintura2="magenta"
if azar2==4:
    pintura2="yellow"

###########################################################################
def moveFood():
    if randrange(50)==0:
        y=randrange(-150,150)
        x=randrange(-150,150)
        food = vector(x,y)

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def changef(x1,y1):
    aimf.x=x1
    aimf.y=y1



def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190
######################################################################
def inside(food):
    """Parte para revisar si la comida está dentro de la pantalla"""
    return -200 < food.x < 190 and -200 < food.y < 190
########################################################################


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
#############################################################################
#Parte para hacer que la comida se mueva paso a paso 
    if head != food:
        if randrange(20)==0:
            changef(5,0)
        if randrange(20)==0:
            changef(-5,0)
        if randrange(20)==0:
            changef(0,5)
        if randrange(20)==0:
            changef(0,-5)
        food.move(aimf)
        if not inside(food):
            if food.x<-200:
                food.x=190
            if food.x>190:
                food.x=-200
            if food.y<-200:
                food.y=190
            if food.y>190:
                food.y=-200


############################################################################
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, pintura)

    square(food.x, food.y, 9, pintura2)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()