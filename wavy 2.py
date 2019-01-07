from math import pi, sin, cos

import pgzrun

# Screen size
WIDTH = 800
HEIGHT = 800

# Scaling
scale_x = 50
scale_y = 200


def offset(point):
    # Offset (0, 0) to the center of the screen
    return point[0] + WIDTH / 2, -point[1] + HEIGHT / 2


def draw():

    # Draw the x and y axis
    screen.draw.line(offset((-350, 0)) , offset((350, 0)), 'white')
    screen.draw.line(offset((0, 350)), offset((0, -350)), 'white')

    # Write a legend
    screen.draw.text('Sine function', (20, 20), color='red')
    screen.draw.text('Cosine function', (600, 20), color='yellow')

    screen.draw.text('0', offset((10, 20)), color='white')
    screen.draw.text('90', offset((88, 20)), color='white')
    screen.draw.text('180', offset((160, 20)), color='white')
    screen.draw.text('270', offset((242, 20)), color='white')
    screen.draw.text('360', offset((320, 20)), color='white')

    screen.draw.text('-90', offset((-70, 20)), color='white')
    screen.draw.text('-180', offset((-158, 20)), color='white')
    screen.draw.text('-270', offset((-236, 20)), color='white')
    screen.draw.text('-360', offset((-304, 20)), color='white')

    screen.draw.text('1', offset((10, 210)), color='white')
    screen.draw.text('-1', offset((10, -200)), color='white')

    # This is where to start
    x = -2 * pi * scale_x
    start_point_sin = (x, sin(x) * scale_y)
    start_point_cos = (x, cos(x) * scale_y)

    # Repeat for a set of points (.5 is a tweak to get to 360 degrees)
    while x <= .5 + 2 * pi * scale_x:

        # Calculate the values of sin and cos at each point
        y_sin = sin(x / scale_x) * scale_y
        y_cos = cos(x / scale_x) * scale_y

        end_point_sin = x, y_sin
        end_point_cos = x, y_cos

        # Draw a line segment
        screen.draw.line(offset(start_point_sin), offset(end_point_sin), 'red')
        screen.draw.line(offset(start_point_cos), offset(end_point_cos), 'yellow')

        start_point_sin = end_point_sin
        start_point_cos = end_point_cos

        print('angle(degrees) = {:.1f} : sine = {:.4f} : cosine = {:.4f}'.
              format(180 * x / scale_x / pi, start_point_sin[1] / scale_y, start_point_cos[1] / scale_y))

        # Move to the next point
        x += pi /4


pgzrun.go()