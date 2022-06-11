# Kod na podstawie strony
# https://www.geeksforgeeks.org/dda-line-generation-algorithm-computer-graphics/
from math import ceil


def DDA(x0, y0, x1, y1) -> list:
    # find absolute differences
    dx = abs(x0 - x1)
    dy = abs(y0 - y1)

    # find maximum difference
    steps = ceil(max(dx, dy))

    # calculate the increment in x and y
    xinc = dx / steps
    yinc = dy / steps

    # start with 1st point
    x = float(x0)
    y = float(y0)

    coordinates = []

    for i in range(steps):
        # append the x,y coordinates in respective list
        coordinates.append((x, y))

        # increment the values
        x = x + xinc
        y = y + yinc

    return coordinates
