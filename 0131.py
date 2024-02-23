from PIL import Image

img=Image.open("poke500/491_다크라이.png")

for i in range(500):
    for j in range(500):
        if not img.getpixel((i,j))[3]<10:
            img.putpixel((i,j),(0,0,0,255))


img.show()
