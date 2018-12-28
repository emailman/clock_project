from math import cos, sin, pi
from time import sleep

import pgzrun

# Screen size
WIDTH = 400
HEIGHT = 400

center = (0, 0)

# List of end points
end_points = []

for angle in range(90, -270, -6):
    x = cos(angle * pi / 180) * 150
    y = sin(angle * pi / 180) * 150
    end_point = (x, y)
    end_points.append(end_point)


def offset(point):
    # Offset (0, 0) to the center of the screen
    return point[0] + WIDTH / 2, -point[1] + HEIGHT / 2


def draw():

    # Draw lines
    for each_point in end_points:
        screen.draw.line(offset(center), offset(each_point), 'white')


pgzrun.go()