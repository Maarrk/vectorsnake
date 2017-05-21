#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake


# converts hex to rgb tuple
def hex(text):
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
        x_min = float(x_min)
        x_max = float(x_max)
        y_min = float(y_min)
        y_max = float(y_max)

        if x_min < x_max and y_min < y_max:
            self.scaled = True
            # PPU on x is bigger
            if float(self.width) / (x_max - x_min) > float(self.height) / (y_max - y_min):
                x_center = (x_min + x_max) / 2
                x_min = x_center + (x_center - x_min) * float(self.height) / (y_max - y_min)
                x_max = x_center + (x_max - x_center) * float(self.height) / (y_max - y_min)
            elif float(self.width) / (x_max - x_min) < float(self.height) / (y_max - y_min):
                y_center = (y_min + y_max) / 2
                y_min = y_center + (y_center - y_min) * float(self.width) / (y_max - y_min)
                y_max = y_center + (y_max - y_center) * float(self.width) / (y_max - y_min)

            self.left = int(x_min)
            self.right = int(x_max)
            self.bottom = int(y_min)
            self.top = int(y_max)
        else:
            print 'Wrong scale input'

    def scaled_x(self, x):
        return float(x - self.left) / float(self.right - self.left) * self.width

    def scaled_y(self, y):
        return self.height - float(y - self.bottom) / float(self.top - self.bottom) * self.height

    color = (0, 0, 0)

    def set_color(self, r, g, b):
        self.color = (r, g, b)

    def draw_grid(self):
        text = ['  <!-- Coordinate grid: -->\n']
        old_color = self.color

        self.color = (191, 191, 191)
        text += [self.line(x, self.bottom, x, self.top) for x in range(self.left, self.right + 1, 1) if x != 0]
        text += [self.line(self.left, y, self.right, y) for y in range(self.bottom, self.top + 1, 1) if y != 0]

        self.color = (63, 63, 63)
        text += [self.line(0, self.bottom, 0, self.top), self.line(self.left, 0, self.right, 0)]

        self.color = old_color
        return '  '.join(text) + '\n'

    def line(self, x1, y1, x2, y2):
        if self.scaled:
            x1 = self.scaled_x(x1)
            x2 = self.scaled_x(x2)

            y1 = self.scaled_y(y1)
            y2 = self.scaled_y(y2)

        data_str = '  <line x1="%s" y1="%s" x2="%s" y2="%s" ' % (str(x1), str(y1), str(x2), str(y2))
        style_str = 'style="stroke:rgb%s;stroke-width:2" />\n' % str(self.color)
        return data_str + style_str
