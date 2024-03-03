# GenGrid.py - 生成网格
from tqdm import tqdm
from PIL import Image, ImageDraw, ImageFont
from math import floor

# 创建图章 (24 * 24)
imgTemp = Image.new("RGBA", (24, 24), "darkgreen")
drwTemp = ImageDraw.Draw(imgTemp)
drwTemp.rectangle([0, 0, 11, 11], "lightgreen")
drwTemp.rectangle([12, 12, 23, 23], "lightgreen")

# 创建图像（1200 x 1212）
fleComps = open('data/comps1.txt', 'r')
for j in range(6):
    imgMain = Image.new("RGBA", (1200, 1200), "darkgreen")
    for i in tqdm(range(50 * 50)):
        widthStart = floor(i / 50) * 24
        heightStart = i % 50 * 24
        imgMain.paste(imgTemp, (widthStart, heightStart))
    drwMain = ImageDraw.Draw(imgMain)
    fntSans = ImageFont.truetype("data/PsName.ttf", 10)

    for i in tqdm(range(10 * 100)):
        widthStart = i % 10 * 120
        heightStart = floor(i / 10) * 12 + 4
        strCompsName = fleComps.readline()
        if strCompsName == "":
            pass
        else:
            drwMain.text((widthStart, heightStart), "%d:%s" %
                     (i, strCompsName), font=fntSans, fill="seagreen")
    imgMain = imgMain.save(str(j) + ".png")
