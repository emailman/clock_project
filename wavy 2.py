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
    last_point_sin = (x, sin(x) * scale_y)
    last_point_cos = (x, cos(x) * scale_y)

    # Repeat for a set of points
    while x <= 2 * pi * scale_x:

        # Calculate the values of sin and cos at each point
        y_sin = sin(x / scale_x) * scale_y
        y_cos = cos(x / scale_x) * scale_y

        next_point_sin = x, y_sin
        next_point_cos = x, y_cos

        # Draw a line segment
        screen.draw.line(offset(last_point_sin), offset(next_point_sin), 'red')
        screen.draw.line(offset(last_point_cos), offset(next_point_cos), 'yellow')

        last_point_sin = next_point_sin
        last_point_cos = next_point_cos

        # Move to the next point
        x += pi


pgzrun.go()