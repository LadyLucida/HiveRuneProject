from PIL import Image, ImageOps
import os
import csv
import pandas
import numpy as np
import sys

def color_change(img):
    img = img.convert('RGBA')
    data = np.array(img)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    # Replace white with red... (leaves alpha values alone...)
    green_areas = (red == 54) & (blue == 61) & (green == 61)
    data[..., :-1][green_areas.T] = (204, 153, 102) # Transpose back needed
    im2 = Image.fromarray(data)
    return im2


dir = "Parts/Half/"
top = os.listdir(dir + "Tops/3x")
top = sorted(top)
num = [w[4:6] for w in top]

print(num)

#loads in the known hive runes
colnames = ['tops', 'mids', 'bottoms']
data = pandas.read_csv('../Hive_Rune_Database.csv', names=colnames)

known = data.tops.tolist()
known.extend(data.bottoms.tolist())
#removes dupes from the list
res = []
[res.append(x) for x in known if x not in res]

for i,value in enumerate(top, start = 0):
    im = Image.open(dir + "Tops/3x/" + value)

    if i <= 26 or i == 31:
        #these ones don't have a top flip or a bottom flipped since they are symetrical
        bot_f = ImageOps.flip(im)
        bot_name = str("Bottom_" + num[i])
        if bot_name not in known:
            bot_f = color_change(bot_f)

        save_name = dir + "Bottoms/3x/" + bot_name + ".png"
        bot_f.save(save_name, "png")

    else:

        bot_f = ImageOps.flip(im)
        bot_name = str("Bottom_" + num[i])
        if bot_name not in known:
            bot_f = color_change(bot_f)

        bottom_save_name = dir + "Bottoms/3x/" + bot_name + ".png"
        bot_f.save(bottom_save_name, "png")

        top = ImageOps.mirror(im)
        top_num = num
        toppnumber = top_num[-1] + 1
        top_name_F = str("Top_" + toppnumber)
        top_num.append(toppnumber)
        if top_name_F not in known:
            top = color_change(top)

        top_flipped_save_name = dir + "Tops/3x/" + top_name_F + ".png"
        top.save(top_flipped_save_name, "png")

        bot_mf = ImageOps.mirror(im)
        bot_mf = ImageOps.flip(bot_mf)
        bot_num = num
        botnumber = bot_num[-1] + 1
        bot_name_MF = str("Bottom_" + botnumber)
        bot_num.append(botnumber)
        if bot_name_MF not in known:
            bot_mf = color_change(bot_mf)

        bot_flipped_save_name = dir + "Bottoms/3x/" + bot_name_MF + ".png"
        bot_mf.save(bot_flipped_save_name, "png")
