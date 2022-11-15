import cv2
import numpy as np
from PIL import Image

dosya = "empty.png"

img = cv2.imread(dosya)

dosya2 = "orjinal.png"
img2 = cv2.imread(dosya2)

width = 1500
height = 1000

inputs =  np.float32([[0,0], [512,0], [512,640], [0, 640]])

def paste():
    background = Image.open("empty.png")
    foreground = Image.open("transparent.png")

    background.paste(foreground, (0, 0), foreground)
    background.show()


def convertImage():
    img = Image.open("warped.png")
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save("transparent.png", "PNG")
    print("Successful")


def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        kd.append([x, y])
        if len(kd)%4 == 0:
            outputs = np.float32([kd[-4], kd[-3], kd[-2], kd[-1]])   # starting from upper left corner, clockwise
            matrix = cv2.getPerspectiveTransform(inputs,outputs)
            imgOutput = cv2.warpPerspective(img2, matrix, (width,height), cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0))
            cv2.imwrite("warped.png", imgOutput)
            convertImage()
            paste()
        font = cv2.FONT_HERSHEY_SIMPLEX

if __name__=="__main__":
    kd = []
    img = cv2.imread(dosya, 1)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
