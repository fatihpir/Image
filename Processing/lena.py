from PIL import Image

im=Image.open("lena.png")
pix=im.load()
w=im.size[0]
h=im.size[1]
graylist=[[0]*h for x in range(w)]
temparray=[[0]*(h+2) for x in range(w+2)]
print im.getpixel((3,5))
for i in range(w):
    for j in range(h):
        r, g, b = im.getpixel((i, j))
        gray=(int)((r*0.2126)+(g*0.7152)+(b*0.0722))
        graylist[i][j]=gray
        pix[i,j]=(gray,gray,gray)
im.save("newlena.png")