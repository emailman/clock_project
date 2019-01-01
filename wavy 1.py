from math import sin, pi

import pgzrun

# Screen size
WIDTH = 800
HEIGHT = 800


def offset(point):
    # Offset (0, 0) to the center of the screen
    return point[0] + WIDTH / 2, -point[1] + HEIGHT / 2


def draw():
    x = -100 * pi
    last_point = (x, 0)

    screen.draw.line(offset((-350, 0)) , offset((350, 0)), 'white')
    screen.draw.line(offset((0, 350)), offset((0, -350)), 'white')

    while x <= 100 * pi:
        y = sin(x / 50) * 200
        next_point = x, y
        print(last_point, next_point)

        screen.draw.line(offset(last_point), offset(next_point), 'yellow')
        x += pi
        last_point = next_point



pgzrun.go()