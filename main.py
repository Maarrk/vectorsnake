#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import vector_snake as vs
import qtong

beniz = [qtong.qtong(i * 0.02) for i in range(51)]

dwg = vs.Drawing(600, 600)
dwg.set_scale(-3, 3, -1, 7)

# load file output
fo = open('output.svg', 'w+')

fo.write(dwg.begin())
fo.write(dwg.draw_grid())

dwg.set_color(0, 255, 255)
fo.write(dwg.polyline(beniz))

fo.write(dwg.end())
fo.close()
