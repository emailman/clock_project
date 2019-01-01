from math import cos, sin, pi
from time import sleep

import pgzrun

# Screen size
WIDTH = 400
HEIGHT = 400

# List index
index = 0

# Create an empty list for the end points
end_points = []

# Create a loop to calculate 60 end points
# clockwise around a circle
for angle in range(90, -270, -6):

    # Calculate the x and y values
    x = cos(angle * pi / 180) * 150
    y = sin(angle * pi / 180) * 150

    # Create a point using x and y values
    end_point = (x, y)

    # Add the point to the list
    end_points.append(end_point)

print(len(end_points), 'items on the list')


def offset(point):
    # Offset (0, 0) to the center of the screen
    # and invert the value of y
    return (point[0] + WIDTH / 2, -point[1] + HEIGHT / 2)


def draw():
    screen.draw.filled_circle(offset((0, 0)), 15, 'white')


def update():
    global index

    screen.clear()

    screen.draw.line(offset((0, 0)), offset(end_points[index]), 'green')

    # Increase index by one, same as "index = index + 1"
    index += 1

    # Loop back to zero at the end of the list
    if index == 60:
        index = 0

    # Tic
    sleep(1)

pgzrun.go()
