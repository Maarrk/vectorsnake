#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import math
import my_math

ellipse_perimeter = 7.93272


def left_ball():
    end_point = my_math.resize(my_math.rotate(my_math.translate((-1, 2),
                    (1.5, -1)), -math.atan(0.5)), (1, 0.6666666667))
    end_angle = math.atan2(end_point[1], end_point[0])

    circle = [(math.cos(float(i) / 10 * math.pi + end_angle),
               math.sin(float(i) / 10 * math.pi + end_angle))
              for i in range(11)]
    scaled = [my_math.resize(point, (1, 1.5)) for point in circle]
    rotated = [my_math.rotate(point, math.atan(0.5)) for point in scaled]
    translated = [my_math.translate(point, (-1.5, 1)) for point in rotated]

    return translated