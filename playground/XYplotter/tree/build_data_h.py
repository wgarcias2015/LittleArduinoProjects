#!/usr/bin/env python

# These are the key virtices of the Christmas Tree
# Borrowed from http://www.johngineer.com/blog/?p=648
VERTICES = [
    (110,  15),
    (110,  35),
    ( 50,  35),
    ( 80,  85),
    ( 65,  85),
    ( 95, 135),
    ( 80, 135),
    (110, 185),
    ( 95, 185),
    (125, 235),
    (155, 185),
    (140, 185),
    (170, 135),
    (155, 135),
    (185,  85),
    (170,  85),
    (200,  35),
    (140,  35),
    (140,  15)
]

LINE_STEP = 3
ANGLE_STEP = 3

points = []


def insert_point(x, y):
    points.append((x, y))


def interpolate(last_p, p):
    x1, y1 = VERTICES[last_p]
    x2, y2 = VERTICES[p]

    if x1 == x2:
        for y in range(y1, y2, LINE_STEP if y2 > y1 else -LINE_STEP):
            insert_point(x1, y)
    elif y1 == y2:
        for x in range(x1, x2, LINE_STEP if x2 > x1 else -LINE_STEP):
            insert_point(x, y1)
    else:
        for x in range(x1, x2, ANGLE_STEP if x2 > x1 else -ANGLE_STEP):
            y = int(y1 + (y2 - y1)/(float(x2) - x1)  * (x - x1))
            insert_point(x, y)


def outputPreamble():
    print (
        '// auto-generated by build_data.h.py\n\n'
        '#ifndef Points_h\n'
        '#define Points_h\n\n'
        '// x,y coordinates for plotting\n'
        'const static byte VERTICES[][2]  = {'
    )


def outputPoints():
    data = '  {}'.format(
        ',\n  '.join([
            '{{{}, {}}}'.format(point[0], point[1])
            for point in points
        ])
    )
    print data


def outputEpilogue():
    print (
        '};\n\n'
        'int NUM_POINTS = sizeof(VERTICES) / 2;\n\n'
        '#endif'
    )


def build():
    last_p = len(VERTICES) - 1
    for p in range(last_p + 1):
        interpolate(last_p, p)
        last_p = p
    outputPreamble()
    outputPoints()
    outputEpilogue()


if __name__ == '__main__':
    build()