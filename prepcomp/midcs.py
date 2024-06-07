#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys

dtz = set(
    "丫产乜乔么冈飞鱼东头书术页乇卫乌兴孓龙兑卢刁丰两乐兰鸟关戋乒乓为亍甩步风业习负开每马币专乡电丧亏氐长车亓岛发韦丝户齐义办贞龟亚丢农严"
)
j0set = []
# https://en.wikipedia.org/wiki/GB_2312
# exactly the same as the G0 one:
# break CFD4-CFFE

for i in range(0xB0, 0xF5):
    for j in range(0xA1, 0xFF):
        encHanzi = i * 256 + j
        if encHanzi in range(0xCFD4, 0xCFFF):
            break
        elif encHanzi in range(0xF4A6, 0xF4FF):
            break
        else:
            strHanzi = encHanzi.to_bytes(2, "big").decode(encoding="EUC-JP")
            j0set.append(strHanzi)

allHanzi = set(j0set).union(dtz)


def write2file(filePath):
    f = open(filePath, "w", encoding="UTF-8")
    f.write("".join(allHanzi))


if len(sys.argv) < 2:
    AskedFilePath = input("Where to save? ")
    write2file(AskedFilePath)
else:
    write2file(sys.argv[1])
