from PIL import Image

img = Image.new("1", (2560,3200))

import sys

refx = 2042
refy = 12298

data =[]
with open('map/temp/all3.csv') as f:
    for line in f:
       line = line.replace('\n','') #末尾の\nの削除
       line = line.replace("  "," ") #
       line = line.split(" ") #分割
       #print(line[1],line[2])
       x = int(float(line[1])*100) - refx
       y = int(float(line[2])*100) - refy
       #print(x,y)
       img.putpixel((x,y),1)

img.save('map/map.png')
