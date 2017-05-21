#!/usr/bin/env python
# -*- coding: utf-8 -*-

# VectorSnake by Marek Łukasiewicz
# https://github.com/Maarrk/vectorsnake

import vector_snake as vs

dwg = vs.Drawing(800, 800)
dwg.set_scale(-2, 2, -1, 3)

# load file output
fo = open('output.svg', 'w+')

fo.write(dwg.begin())
fo.write(dwg.draw_grid())

fo.write(dwg.line(0, 0, 1, 1))

fo.write(dwg.end())
fo.close()
