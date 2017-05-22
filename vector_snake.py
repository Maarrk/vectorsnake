#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake


import my_math


# converts hex to rgb tuple
def hex_color(text):
    color = text.strip('#')

    if len(color) == 6:
        return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))
    elif len(color) == 3:
        return tuple(int(color[i], 16) for i in range(3))
    else:
        print 'Wrong hex value'


# handles shapes in coordinate system
class Drawing:
    def __init__(self, width_init, height_init):
        self.width = width_init
        self.height = height_init

    def begin(self):
        beginning_string = """<?xml version="1.0" encoding="utf-8"?>
<!-- Created with VectorSnake https://github.com/Maarrk/vectorsnake -->

<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s">\n""" % (str(self.width), str(self.height))

        return beginning_string

    def end(self):
        return "</svg>\n"

    scaled = False
    left = 0
    right = 0
    top = 0
    bottom = 0

    def set_scale(self, x_min, x_max, y_min, y_max):
        if x_min < x_max and y_min < y_max:
            self.scaled = True

            x_min = float(x_min)
            x_max = float(x_max)
            y_min = float(y_min)
            y_max = float(y_max)

            ppu_x = self.width / (x_max - x_min)
            ppu_y = self.height / (y_max - y_min)

            if ppu_x < ppu_y:
                ppu_y = ppu_x
            else:
                ppu_x = ppu_y

            x_cen = (x_max + x_min) / 2
            y_cen = (y_max + y_min) / 2

            self.left = x_cen - self.width / 2 / ppu_x
            self.right = x_cen + self.width / 2 / ppu_x
            self.bottom = y_cen - self.height / 2 / ppu_y
            self.top = y_cen + self.height / 2 / ppu_y
        else:
            print 'Wrong scale input'

    def scaled_x(self, x):
        if self.scaled:
            return float(x - self.left) / float(self.right - self.left) * self.width
        else:
            return x

    def scaled_y(self, y):
        if self.scaled:
            return self.height - float(y - self.bottom) / float(self.top - self.bottom) * self.height
        else:
            return

    def scaled_point(self, point):
        if self.scaled:
            return self.scaled_x(point[0]), self.scaled_y(point[1])
        else:
            return point

    color = (0, 0, 0)

    def set_color(self, r, g, b):
        self.color = (my_math.clamp(r, 0, 255), my_math.clamp(g, 0, 255), my_math.clamp(b, 0, 255))

    stroke_width = 2

    def set_stroke(self, px):
        self.stroke_width = px

    def style(self):
        return 'style="fill:none;stroke:rgb%s;stroke-width:%d"' % (str(self.color), self.stroke_width)

    def draw_grid(self):
        text = ['  <!-- Coordinate grid: -->\n']
        old_color = self.color

        self.color = (191, 191, 191)
        text += [self.line((x, self.bottom), (x, self.top)) for x in range(int(self.left), int(self.right) + 1, 1) if x != 0]
        text += [self.line((self.left, y), (self.right, y)) for y in range(int(self.bottom), int(self.top) + 1, 1) if y != 0]

        self.color = (63, 63, 63)
        text += [self.line((0, self.bottom), (0, self.top)), self.line((self.left, 0), (self.right, 0))]

        self.color = old_color
        return '  '.join(text) + '\n'

    def line(self, point1, point2):
        x1 = self.scaled_x(point1[0])
        x2 = self.scaled_x(point2[0])

        y1 = self.scaled_y(point1[1])
        y2 = self.scaled_y(point2[1])

        data_str = '  <line x1="%d" y1="%d" x2="%d" y2="%d" ' % (x1, y1, x2, y2)
        return data_str + self.style() + ' />\n'

    def polyline(self, points):
        scaled_points = [self.scaled_point(point) for point in points]

        point_str = [str(point[0]) + ',' + str(point[1]) for point in scaled_points]
        data_str = '  <polyline points="' + ' '.join(point_str) + '" '
        return data_str + self.style() + ' />\n'

    def circle(self, center, radius):
        data_str = '  <circle cx="%d" cy="%d" r="%d" ' % (center[0], center[1], radius)
        return data_str + self.style() + ' />\n'
