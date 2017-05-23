#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import math
import my_math

ellipse_perimeter_half = 3.96636


def qtong(s):
    # mirror image
    if s > 0.5:
        point = qtong(1-s)
        return my_math.resize(point, (-1, 1))

    s = s * 17.0743126536

    if s < ellipse_perimeter_half:
        return left_ball(s)
    elif s <= ellipse_perimeter_half + 3:
        return -1, s - ellipse_perimeter_half + 2
    else:
        return -math.cos(s - ellipse_perimeter_half - 3), 5 + math.sin(s - ellipse_perimeter_half - 3)


def left_ball(s):
    s = s / ellipse_perimeter_half
    end_angle = 0.4636476090

    circle = (-math.cos(s * math.pi - end_angle), math.sin(s * math.pi - end_angle))
    scaled = my_math.resize(circle, (1, 1.5))
    rotated = my_math.rotate(scaled, math.atan(0.5))
    translated = my_math.translate(rotated, (-1.5, 1))

    return translated
