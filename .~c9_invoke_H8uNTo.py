import os,sys
import Image
jpgfile = Image.open("color_img.b")
print jpgfile.bits, jpgfile.size, jpgfile.format

jpgfile.show()
