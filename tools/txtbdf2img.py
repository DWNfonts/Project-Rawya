# TxtBdf2Img
from bdfparser import Font
from PIL import Image, ImageOps

font = Font("data/xypx.bdf")
im = Image.new("RGBA", (0, 0))
print(font.headers["fontname"])
with open("data/compsr.txt", "r") as file:
    for line in file:
        ac = font.draw(line)
        width = im.size[0]
        im_ac = Image.frombytes(
            "RGBA", (ac.width(), ac.height()), ac.tobytes("RGBA"))
        if ac.width() > width:
            im = ImageOps.expand(im, border=(
                0, 0, ac.width() - width, ac.height()))
        else:
            im = ImageOps.expand(im, border=(0, 0, 0, ac.height()))
        height = im.size[1] - 12
        im.paste(im_ac, (0, height))
        print(line)
im.save("awa.png")
