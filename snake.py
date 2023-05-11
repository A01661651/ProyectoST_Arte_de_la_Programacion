"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
aimf= vector(0, 1)


def change(x, y):
    """CCambia la dirección de la Serpiente."""
    aim.x = x
    aim.y = y


def changef(x1,y1):
    aimf.x=x1
    aimf.y=y1


def moveFood():
    """Se define el rango, y cada vez que sea 0 el número aleatorio, procederá el if el cual hará que la comida se mueva aleatoriamente"""
    if randrange(50)==0:        
        x=randrange(-150,150)
        y=randrange(-150,150)

        """Aparecera la comida en el puesto aleatorio que se le asigno arriba"""
        food = vector(x,y)      


def inside(head):
    """Regresa True si la cabeza esta dentro de los límites"""
    return -200 < head.x < 190 and -200 < head.y < 190

def inside(food):
    """Parte para revisar si la comida está dentro de la pantalla"""
    return -200 < food.x < 190 and -200 < food.y < 190


def move():
    """Mueve la serpiente un segmento."""
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
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
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
