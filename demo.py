from math import cos, sin, pi
from time import sleep

import pgzrun

# List of end points
end_points = []

# Screen size
WIDTH = 400
HEIGHT = 400

center = (0, 0)

second_counter = 0 # 0 - 59
second_hand_length = 150
second_hand_color = 'red'

minute_counter = 0 # 0 - 59
minute_hand_length = 150
minute_hand_color = 'white'


# Go around the clock, starting at 12:00
for angle in range(90, -270, -6):

    # Calculate the end point
    x = second_hand_length * cos(angle * pi / 180)
    y = second_hand_length * sin(angle * pi / 180)

    point = (x, y)

    # Add the point to the list
    end_points.append(point)

# Print each value in the list
for each_point in end_points:
    x = each_point[0]
    y = each_point[1]
    print('({:.2f} , {:.2f})'.format(x, y))
print(len(end_points))


def offset(point):
    # Offset (0, 0) to the center of the screen
    return (point[0] + WIDTH / 2, -point[1] + HEIGHT / 2)


def draw():
    # Draw white hub in the center
    screen.draw.filled_circle(offset(center), 10, 'white')


def update():
    global second_counter

    screen.clear()

    # Draw the second hand with a red dot at the end
    screen.draw.line(offset(center), offset(end_points[second_counter]), second_hand_color)
    screen.draw.filled_circle(offset(end_points[second_counter]), 8, second_hand_color)

    # Show the numbers of seconds as text
    screen.draw.text(str(second_counter), (WIDTH / 2 - 10, 10))

    # Step the counter by one
    second_counter += 1

    # When the counter reaches 60, set it back to zero
    if second_counter == 60:
        second_counter = 0

    # Wait one second (tic)
    sleep(1)


pgzrun.go()
