from math import cos, sin, pi

for angle in range(90, -270, -6):
    x = cos(angle * pi / 180) * 150
    y = sin(angle * pi / 180) * 150
    end_point = (x, y)
    print(angle, end_point)
