#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys

dtz = list(
    "一丁七万丈三上下不与丐丑专且世丘丙业东丝丞丢两严丧个丫中丰串丸丹为主乃久乇么义之乌乍乎乏乐乒乓乔乖乘乙乜九乞也习乡书了予争事二亍于亏云互亓五井亚亡亦产人儿兀兆先光克免兑兔入八公六兮兰共关兴兵其具典内冈冉册农冬几凡凸凹刀刁刃力办匕十千卅升午半卜卞占卢卫又叉及友反发只可史吏土士壬大天太夫夭央失头女子孑孓寸小少尢尤尹尺屮屯山岛巛川州工巨巫己已巳巴币市干平年并幺廿开弓弗弟心必戈戊戋戌戍成户手才承支攴文斗斤斥方无曰曲曳更月有未末本术朱束来柬欠止正步毋母每毛氏氐民气水永求火爪父片牙牛犬玉王瓜瓦甘生用甩甫甬田由甲申电疋白皮皿直矛矢石示禾穴立糸系缶羊羌而耒耳臣自臼舌舟良色血衣西言谷豆贞负赤走足身车辛辰酉里长隶隹雨非面革韦页风飞食首马鬼鱼鸟齐龙龟"
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

allHanzi = set(dtz) - set(j0set)


def write2file(filePath):
    f = open(filePath, "w", encoding="UTF-8")
    f.write("".join(allHanzi))


if len(sys.argv) < 2:
    AskedFilePath = input("Where to save? ")
    write2file(AskedFilePath)
else:
    write2file(sys.argv[1])
