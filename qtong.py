#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import math
import my_math

ellipse_perimeter = 7.93272


def left_ball(s):
    end_point = my_math.resize(my_math.rotate(my_math.translate((-1, 2),
                                             (1.5, -1)),
                               -math.atan(0.5)),
                (1, 0.6666666667))

    end_angle = math.atan2(end_point[1], end_point[0])

    circle = (math.cos(s * math.pi + end_angle), math.sin(s * math.pi + end_angle))
    scaled = my_math.resize(circle, (1, 1.5))
    rotated = my_math.rotate(scaled, math.atan(0.5))
    translated = my_math.translate(rotated, (-1.5, 1))

    return translated
