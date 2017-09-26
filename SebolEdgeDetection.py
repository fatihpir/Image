from math import sqrt
from PIL import Image
import numpy
def filtering(matris):
    neighbormatrice = numpy.zeros(shape=(5, 5), dtype=numpy.uint8)  # Neighbor matrix to be filtered pixel
    matris_sobel = numpy.zeros(shape=(w, h, 3), dtype=numpy.uint8)
    filtermatrice_vertical = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    filtermatrice_horizontal = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    for i in range(1, w - 1):
        for j in range(1, h - 1):
            for m in range(3):
                value_vertical = 0.0
                value_horizontal = 0.0
                for k in range(3):
                    for l in range(3):
                        neighbormatrice[k][l] = matris[k + i - 1][l + j - 1][m]  # Create neighbor matrice's indexs(except a frame size=2)
                for k in range(3):
                    for l in range(3):
                        value_vertical = (value_vertical + (neighbormatrice[k][l] * filtermatrice_vertical[k][l]))
                        value_horizontal = (value_horizontal + (neighbormatrice[k][l] * filtermatrice_horizontal[k][l]))
                value = sqrt((value_vertical**2) + (value_horizontal**2))
                matris_sobel[i][j][m] = int(value)
    return matris_sobel
im = Image.open("source.jpg")
w, h = im.size
pix = numpy.zeros(shape=(w, h, 3), dtype=numpy.uint8)
for i in range(w):  # Get and assign image's RGB values
    for j in range(h):
        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((i, j))
        pix[i][j] = r, g, b
pix = filtering(pix)  # Filtering
pixTranspose = numpy.zeros(shape=(h, w, 3), dtype=numpy.uint8)  # Edit target image's sizes
for i in range(h):
    for j in range(w):
        pixTranspose[i][j] = pix[j][i]
img = Image.fromarray(pixTranspose, 'RGB')  # Create an image with RGB values
img.save('target.jpg')
img.show()