import pyautogui as pg
import lackey
import cv2
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
from cv2 import cv2

x_rgn = 100
y = 266
x_pix = 480
h_rgn = 96
w_rgn = 350
mouse_speed = 0.4
checked = 0
sent = 0
p=0

time.sleep(5)
pg.moveTo(745, 345, mouse_speed)
try:
    state = True
    while state:
        p=p+1 
        prog_state = True
        while prog_state:
            im = pg.screenshot()
            pix = im.getpixel((x_pix, y))
            pg.scroll(-1)
            #print (pix)
            if pix == (235, 237, 240):
                prog_state = False
            png_name = str(p)
            read_png = png_name + '.png'
            print(type(read_png))
            i = lackey.Region (x_rgn, y, w_rgn, h_rgn)
            i.saveScreenCapture(path= 'C:\\Users\\HRK\\Documents\\vscode', name = png_name)
            img = cv2.imread(read_png)
            text = pytesseract.image_to_string(img)
            #x = type(text)
            #print(x)
            #print(text)
            name = text.split("\n")[0]
            print(name.ljust(35), end= '')
            #li= list(str.split(text))
            #print (li)
            numbers = [int(word) for word in text.split() if word.isdigit()]
            #print(numbers)
            j = [str(integer) for integer in numbers]
            k_string = "".join(j)
            if k_string == '':
                mut_fr = 0
            else:
                mut_fr = int(k_string)
                print('Mutual', '', mut_fr)
            mutual = mut_fr

            #print(png_name,',', read_png) #OK
            #print(mutual) #OK
            if mutual >= 50:
                movement.clickBack(745, 345, 560, 315, mouse_speed)
                print("Request sent!!")
                sent+=1
            else:
                print("Request NOT sent")
            checked+=1
            pg.scroll (-110)
            if sent >= 1000:
                state = False
                print("Final result... ", )
                print("Checked ", checked, "ID's")
                print(sent, "requests have been sent")
except KeyboardInterrupt:
    print("TASK HAS BEEN INTERRUPTED!\nWHY WOULD YOU DO THAT??!")
    time.sleep(2)
    print("Final result... ", )
    print("Checked ", checked, "ID's")
    print(sent, "requests have been sent")

def clickBack(a, b, x, y, d):
    pg.moveTo(a, b, d)
    print ("Cursor on rest")
    pg.moveTo(x, y, d)
    print ("Offestting")
    pg.click()
    print ("Clicked! ", end = '')
    pg.moveTo(a, b, d)
    print ("Resetting..")
