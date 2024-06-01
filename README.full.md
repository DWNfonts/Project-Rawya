![Project Rawya 生雅](docs/logo.png)  
[![QQ 群：619164913](https://img.shields.io/badge/619164913-%2312B7F5?style=for-the-badge&logo=tencentqq&logoColor=white)](https://qm.qq.com/q/m3j4G5YGsw)
[![爱发电](https://img.shields.io/badge/%E7%88%B1%E5%8F%91%E7%94%B5-%23946CE6.svg?style=for-the-badge&logoColor=white)](http://afdian.net/a/DWNfonts)
[![3 语句 BSD + 其他](https://img.shields.io/badge/3%20语句%20BSD%20+%20其他-%23870000?style=for-the-badge&logo=freebsd&logoColor=white)](LICENSE.md)
[![回到小雅](https://img.shields.io/badge/回到小雅-%23880e4f?style=for-the-badge&logoColor=white)](https://github.com/DWNfonts/XiaoyaPixel)

---
生雅项目——没煮熟的小雅，没有手工干预的半成品。  
（也就是说，小雅是这玩意的 fork）  
目前只有一堆脚本，部件一笔没动 ~~（懒癌晚期，没救了）~~  
**请不要将此项目用于生产**
## 怎么用
首先建议使用 GNU/Linux 操作系统（macOS 也行），并且安装**最新版** Python 以及 `tqdm`、`pillow` 和 `pixel_font_builder` 库。
> 建议使用虚拟环境安装。

**`make` 段：**`cd` 到此目录，然后执行 `make/make.sh`。
* 此时 `rawya.fnt` 是传统方法所生成的 Playdate 字体，可用 [Bits'n'Picas](https://github.com/kreativekorp/bitsnpicas) 打开；
* `rawya.ttf` 等非 `fnt` 后缀为 `makepfb.py` 通过[狼人小林](https://github.com/TakWolf) [`pixel_font_builder` 库](https://github.com/TakWolf/pixel-font-builder)生成的现代字体。~~（不过挺糙的，一看就是复制粘贴自述文档（~~
> `makecompsfont.py` 是用来直接生成单部件字体的。本人尝试了一些方案，但是觉得使用演算表（LibreOffice Calc）来处理比较好。

**`tools` 段：** 大概率废弃。  
**`prepcomp` 段：** 由于这段代码其实是我在 2024 年 1 月写的，到现在我也记不清写了什么。脚本的开头部分或许写了这些代码是干什么的。
## 贡献
> 说到这玩意…还有人要贡献的说？

你大抵可以[搞个 Pull Request](https://github.com/DWNfonts/Project-Rawya/pulls)。
## 分支
### `old-apr24` 分支
四月 5 日、14 日制作的部件。因为质量原因将源 `develop` 分支存档为 `old-apr24` 后重新变基。