from PIL import Image
from os import listdir
from tqdm import tqdm, trange
from math import ceil, floor

字形宽 = 12
字形高 = 12
总图像宽 = (字形宽 + 1) * 16
部件列表 = listdir("out/")
print("共 %s 个部件" % len(部件列表))
总图像高 = ceil(len(部件列表) / 16) * 字形高
图 = Image.new("RGBA", (总图像宽, 总图像高))
print("开始生成图片…")
for i in trange(len(部件列表)):
    部件 = 部件列表[i]
    部件图 = Image.open("out/" + 部件)
    图.paste(部件图, (i % 16 * (字形宽 + 1), floor(i / 16) * 字形高))
print("保存…")
图.save("rawya-table-%d-%d.png"  % (13,12))

with open("rawya.fnt", "w+") as 文件:
    print("写入字体信息到文件…")
    文件头 = '--name=Rawya\n--metrics={"baseline":0,"xHeight":8,"capHeight":10}\ntracking=0\n'
    文件.write(文件头)
    for i in trange(len(部件列表)):
        部件 = 部件列表[i]
        文件.write("%s\t%d\n" % (部件.replace(".png", ""), 字形宽))
