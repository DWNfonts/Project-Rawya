from PIL import Image
from pathlib import Path

# 在此设定宽高
宽 = 12
高 = 12
# 严格模式：设为真的时候，只有所有部件都存在时保存
严格模式 = True

with open("data/comps.txt") as 部件表:
    for 单字对应部件 in 部件表:
        处理后的单字对应部件 = 单字对应部件.rstrip().split("\t")
        汉字 = 处理后的单字对应部件[0]
        print("处理汉字「%s」" % 汉字)
        包含的部件 = 处理后的单字对应部件[1].split(",")
        要生成的部件路径 = []
        for 单个部件 in 包含的部件:
            该部件路径 = "comps/%s.png" % 单个部件
            if Path(该部件路径).is_file():
                要生成的部件路径.append(该部件路径)
        if len(要生成的部件路径) == 0:
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
