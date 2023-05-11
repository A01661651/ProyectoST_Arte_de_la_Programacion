"""Paint, for drawing shapes.
 Ejercicios

1. Un color nuevo
2. Dibujar un círculo
El otro compañero añadirá:
3. Completar el rectángulo
4. Completar el triángulo
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def circle(start, end):

    #Recibe una longitud en start, la cual interpretamos como el diámetro
    up()

    #Se procede a ir a la ubicación del centro del circulo, la cual es d/2
    goto(start.x/2, start.y)
    down()

    #Se inicia el relleno del circúlo
    begin_fill()

    #Se determina el diámetro como el final de x menos el inicio de x 
    diametro=end.x -start.x

    #Se dibuja un punto en el centro requerido, con diametro definido y color a cargo del fill
    dot(diametro)

    end_fill()


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()





def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')

# Para agregar un color nuevo solo se copió el codigo de los colores existentes y se cambió a uno standard nuevo
onkey(lambda: color('magenta'), 'M')

onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()
