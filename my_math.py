#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import math
import re


# clamps value between min and max
def clamp(val, min, max):
    if min > max:
        print 'Wrong clamp range'
        return val
    elif min == max:
        return min
    else:
        if val < min:
            return min
        elif val > max:
            return max
        else:
            return val


def translate(point, vector):
    return point[0] + vector[0], point[1] + vector[1]


def resize(point, ratio):
    return point[0] * ratio[0], point[1] * ratio[1]


def rotate(point, rad):
    x = point[0] * math.cos(rad) - point[1] * math.sin(rad)
    y = point[1] * math.cos(rad) + point[0] * math.sin(rad)
    return x, y


# changes wolfram plaintext polynomial to python expression
def wolfram_polynomial(wolfram_str):
    multi_pi_str = re.sub(r'(\d+) (π)', r'\1 * \2', wolfram_str)
    pi_str = re.sub(r'π', r'math.pi', multi_pi_str)
    multi_x_str = re.sub(r'(\d+) (x)', r'\1 * \2', pi_str)
    pow_str = re.sub(r'\^', r'**', multi_x_str)
    float_str = re.sub(r'(\d+)', r'\1.0', pow_str)

    return float_str
