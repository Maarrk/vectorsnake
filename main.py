#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import vector_snake as vs
import qtong

triangle = [(-1, 0), (0, 2), (1, 0)]
beniz = qtong.left_ball()

dwg = vs.Drawing(600, 600)
dwg.set_scale(-3, 3, -1, 7)

# load file output
fo = open('output.svg', 'w+')

fo.write(dwg.begin())
fo.write(dwg.draw_grid())

fo.write(dwg.line((-1, 0), (2, 1)))

dwg.set_color(0, 255, 255)
fo.write(dwg.polyline(beniz))

dwg.set_color(255, 0, 0)
fo.write(dwg.polyline(qtong.intersection()))

fo.write(dwg.end())
fo.close()
