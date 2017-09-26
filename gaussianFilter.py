from PIL import Image
import numpy
def filtering(matris):
    neighbormatrice = numpy.zeros(shape=(5, 5))#Neighbor matrice to be filtered pixel
    for i in range(2, w - 2):
        for j in range(2, h - 2):
            for m in range(3):
                toplam = 0.0
                for k in range(5):
                    for l in range(5):
                        neighbormatrice[k][l] = matris[k + i - 2][l + j - 2][m]#Create neighbor matrice's indexs(exclude a frame size=2)
                for k in range(5):
                    for l in range(5):
                        toplam = (toplam + (neighbormatrice[k][l] * 0.04))#0.04 is filter value.
                matris[i][j][m] = int(toplam)
    return matris
im = Image.open("source.jpg")
w,h=im.size
pix=numpy.zeros(shape=(w, h, 3),dtype=numpy.uint8)
for i in range(w):  #Get and assign image's RGB values
   for j in range(h):
        rgb_im = im.convert('RGB')
        r , g , b = rgb_im.getpixel((i, j))
        pix[i][j] =r, g, b
pix=filtering(pix)#Filtering
pixTranspose=numpy.zeros(shape=(h, w, 3),dtype=numpy.uint8)#Edit target image's sizes
for i in range(h):
   for j in range(w):
       pixTranspose[i][j]=pix[j][i]
img = Image.fromarray(pixTranspose, 'RGB')#Create an image with RGB values
img.save('target.jpg')
img.show()