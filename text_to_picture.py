import math
from PIL import Image
from random import randint
def decode(text):
    str_len = len(text)
    width = math.ceil(str_len**0.5)
    im = Image.new("RGB",(width,width),0x0)

    x,y = 0,0
    color = randint(0,255)
    for i in text:
        index = ord(i)
        rgb = (color,(index & 0xFF00)>>8,index & 0xFF)
        im.putpixel((x,y),rgb)
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1
    return im

def detext(im):
    width,height = im.size
    lst = []
    for y in range(height):
        for z in range(width):
            red,green,blue = im.getpixel((z,y))
            if (blue | green | red)== 0:
                break
            index = (green << 8) + blue
            lst.append(chr(index))
    return "".join(lst)

if __name__=="__main__":
    file = input("输入：")
    if file[-4:] == ".txt":
        with open(file,encoding = "utf-8") as f:
            all_text = f.read()
        im = decode(all_text)
        im.save(file[:-4] +".bmp")
    elif file[-4:] == ".bmp":
        all_text = detext(Image.open(file,"r"))
        with open(file[:-4] + ".txt","w",encoding = "utf-8") as f:
            f.write(all_text)
    else:
        im = decode(file)
        im.save("out.bmp")
