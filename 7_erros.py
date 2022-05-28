from PIL import Image,ImageChops

img1 = Image.open('fist.jpg')
img2 = Image.open('second.jpg')

diff = ImageChops.difference(img1,img2)

if diff.getbbox():
    diff.show()

