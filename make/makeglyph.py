#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image
from pathlib import Path

# 在此设定宽高
宽 = 12
高 = 12
# 严格模式：设为真的时候，只有所有部件都存在时保存
严格模式 = True
# 点 a 模式，如果有 .a 后缀的文件，直接复制
点a模式 = True

if __name__ == "__main__":

    def chr2ufn(strChar):
        # Char to Unicode Filename
        lstOutput = []
        for i in range(len(strChar)):
            lstOutput.append("%x" % ord(strChar[i]))
        return ".".join(lstOutput)

    with open("data/comps.txt") as 部件表:
        a = open("data/midcs.txt")
        小雅BDF含有汉字 = list(list(a.readlines())[0])
        print(小雅BDF含有汉字)
        a.close()
        for 单字对应部件 in 部件表:
            处理后的单字对应部件 = 单字对应部件.rstrip().split("\t")
            汉字 = 处理后的单字对应部件[0]
            print("处理汉字「%s」" % 汉字)
            汉字编码 = chr2ufn(汉字)
            存在点a = None  # 来没来？如来
            if (
                Path("comps/%s.a.png" % 汉字编码).is_file()
                or Path("comps/%s.m.png" % 汉字编码).is_file()
            ):
                存在点a = True  # 这回真来了
            存在于BDF = None # 能不能？可能
            if 汉字 in 小雅BDF含有汉字:
                存在于BDF = True # 这回真能了
            包含的部件 = 处理后的单字对应部件[1].split(",")
            要生成的部件路径 = []
            for 单个部件 in 包含的部件:
                该部件路径 = "comps/%s.png" % 单个部件
                if Path(该部件路径).is_file():
                    要生成的部件路径.append(该部件路径)
            if 存在点a:
                目标路径 = "comps/%s.a.png" % 汉字编码
                try:
                    with Image.open(目标路径) as 图:
                        print("存在 %s 汉字的独体部件。")
                        图.save("out/%s.png" % 汉字)
                except:
                    print("似乎出了点问题")
            elif 存在于BDF:
                print("汉字「%s」存在于 BDF 中。" % 汉字)
            elif len(要生成的部件路径) == 0:
                print("无部件可用。")
            else:
                if 严格模式 == False or len(要生成的部件路径) == len(包含的部件):
                    print("要生成的部件路径：%s。" % "、".join(要生成的部件路径))
                    with Image.new(mode="RGBA", size=(宽, 高)) as 图:
                        for 目标部件路径 in 要生成的部件路径:
                            with Image.open(目标部件路径) as 目标图:
                                图 = Image.alpha_composite(图, 目标图)
                    图.save("out/%s.png" % 汉字)
                else:
                    print("严格模式已开启，将不会生成此汉字。")
