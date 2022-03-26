import os
import csv
import pandas
import numpy as np
import sys
import cv2

def color_change(im,real = False,flip = False,hypo = False,Imag = False):
    #im = cv2.imread(img)
    
    #colors are in BGR order
    green = [150,224,1]
    blue = [212,2,0]
    pink = [126,43,212]
    yellow = [43,212,210]
    
    Gmask = np.all(im == green, axis=-1)
    Bmask = np.all(im == blue, axis=-1)
    Pmask = np.all(im == pink, axis=-1)
    Ymask = np.all(im == yellow, axis=-1)
    
    #if the part is imaginary make it yellow
    if Imag == True:
        im[Gmask] = yellow
    
    #if the part is a flip of a real make it blue    
    if flip == True:
        im[Gmask | Ymask] = blue
    
    # if the part is hypothedical make it pink    
    if hypo == True:
       im[Gmask | Ymask] = pink
       
    if real == True:
        im[Ymask] = green

    return im


dir = "../Parts/Half/"
top = os.listdir(dir + "Tops/")
top = sorted(top)
top_len = len(top) + 1
print(top_len)
num = [*range(1,top_len)]
print(num)


#loads in the known hive runes
colnames = ['tops', 'mids', 'bottoms']
data = pandas.read_csv('../Hive_Rune_Database_Half.csv', names=colnames)

known = data.tops.tolist()
known.extend(data.bottoms.tolist())

#removes dupes from the list
res = []
[res.append(x) for x in known if x not in res]
res.sort()

for i,value in enumerate(top, start = 0):
    im = cv2.imread(dir + "Tops/" + value)
    top_name = "Half_Top_" + str(num[i]).zfill(2)

    #make all tops be bottoms
    bot = cv2.flip(im, 0)
    bot_name = "Half_Bot_" + str(num[i]).zfill(2)
    if bot_name not in res:
        bot = color_change(bot,Imag = True)
    else:
         bot = color_change(bot,real = True)
    save_name = dir + "Bottoms/" + bot_name + ".png"
    cv2.imwrite(save_name,bot)

    flip_num = num[i] + 25
    print(flip_num)
    top = cv2.flip(im, 1)

    #flips the top
    top_name_F = "Half_Top_" + str(flip_num)
    if top_name_F not in res:
        top = color_change(top,Imag = True)
    else:
        top = color_change(top,real = True)
    top_flipped_save_name = dir + "Tops/" + top_name_F + ".png"
    cv2.imwrite(top_flipped_save_name, top)

    #flips the bottom
    bot_m = cv2.flip(im, -1)
    bot_name_M = "Half_Bot_" + str(flip_num)
    if bot_name_M not in res:
        bot_m = color_change(bot_m,Imag = True)
    else:
        bot_m = color_change(bot_m,real = True)
    bot_flipped_save_name = dir + "Bottoms/" + bot_name_M + ".png"
    cv2.imwrite(bot_flipped_save_name, bot_m)
