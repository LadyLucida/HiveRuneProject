import os
import csv
import numpy as np
import cv2
import pandas as pd


def fix(folder):
    dir = "../Parts/Half/"
    name = os.listdir(dir + folder)
    name = sorted(name)
    name = [s.strip('.png') for s in name] # remove the png from the string borders
    name = [s.replace('.png', '') for s in name] # remove all the png
    return name

def color_change(im,real = False,flip = False,hypo = False,imag = False):
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
    if imag == True:
        im[Gmask | Bmask | Pmask] = yellow
    
    #if the part is a flip of a real make it blue    
    if flip == True:
        im[Gmask | Ymask | Pmask] = blue
    
    # if the part is hypothedical make it pink    
    if hypo == True:
       im[Gmask | Ymask | Bmask] = pink
       
    if real == True:
        im[Bmask | Ymask | Pmask] = green

    return im

def Getnumber(num):

    if num <= 27:
        new = num
    elif num > 54:
        new = num - 27
    elif num <= 54 and num >= 28:
        new = num + 27
    
    return new
    
def Variant(data):
        
    variant = []
        
    for index,row in data.iterrows():
        
        top = row['tops']
        mid = row['mids']
        bot = row['bots']
        
        print("Original:",[top,mid,bot])        

        tnum = int(top.rpartition('_')[-1])
        mnum = int(mid.rpartition('_')[-1])
        bnum = int(bot.rpartition('_')[-1])
        
        if mnum == 1:
            mnew = 4
        if mnum == 2:
            mnew = 2
        if mnum == 3:
            mnew = 3
        if mnum == 4:
            mnew = 1
        
        tnew_v = Getnumber(tnum)
        bnew_v = Getnumber(bnum)
        
        top_v = 'Top_' + str(tnew_v).zfill(2)
        mid_v = 'Mid_' + str(mnew).zfill(2)
        bot_v = 'Bot_' + str(bnew_v).zfill(2)
        
        
        
        print("Vertical Variant:",[top_v,mid_v,bot_v])        
        if ((data['tops'] == top_v) & (data['mids'] == mid_v) & (data['bots'] == bot_v)).any() == True:
            print("VV exists!")
        elif [top_v,mid_v,bot_v] in variant:
            print("VV already in variant list")
        else:
            print("adding VV variant list")
            variant.append([top_v,mid_v,bot_v])
            
        tnew_h = bnum
        bnew_h = tnum
          
        top_h = 'Top_' + str(tnew_h).zfill(2)
        mid_h = 'Mid_' + str(mnew).zfill(2)
        bot_h = 'Bot_' + str(bnew_h).zfill(2)

        print("Horizontal Variant:",[top_h,mid_h,bot_h])
        if ((data['tops'] == top_h) & (data['mids'] == mid_h) & (data['bots'] == bot_h)).any() == True:
            print("HV exists!")
        elif [top_h,mid_h,bot_h] in variant:
            print("HV already in variant list")
        else:
            print("adding HV variant list")
            variant.append([top_h,mid_h,bot_h])
            
            
        tnew_vh = Getnumber(tnew_h)
        bnew_vh = Getnumber(bnew_h)
        mnew_vh = mnum
        
        top_vh = 'Top_' + str(tnew_vh).zfill(2)
        mid_vh = 'Mid_' + str(mnew_vh).zfill(2)
        bot_vh = 'Bot_' + str(bnew_vh).zfill(2)
        
       
        print("Vertical + Horizontal Variant:",[top_vh,mid_vh,bot_vh])
        if ((data['tops'] == top_vh) & (data['mids'] == mid_vh) & (data['bots'] == bot_vh)).any() == True:
            print("VHV exists!")
            print()
        elif [top_vh,mid_vh,bot_vh] in variant:
            print("VHV already in variant list")
            print()
        else:
            print("adding VHV variant listS")
            variant.append([top_vh,mid_vh,bot_vh])     
            print()
            
    return variant

       
dir = "../Parts/Half/"
top = fix("Tops/")
mid = fix("Mids/")
bot = fix("Bottoms/")  

broken_top = [
    'Half_Top_02', 'Half_Top_08', 'Half_Top_09', 'Half_Top_11', 'Half_Top_14', 'Half_Top_16',
    'Half_Top_17', 'Half_Top_18', 'Half_Top_19', 'Half_Top_20', 'Half_Top_21', 'Half_Top_22',
    'Half_Top_23', 'Half_Top_27', 'Half_Top_33', 'Half_Top_34', 'Half_Top_36', 'Half_Top_38', 
    'Half_Top_41', 'Half_Top_42', 'Half_Top_43', 'Half_Top_44', 'Half_Top_45', 'Half_Top_46',
    'Half_Top_47'
]
                
broken_bot = [
    'Half_Bot_02', 'Half_Bot_08', 'Half_Bot_09', 'Half_Bot_11', 'Half_Bot_14', 'Half_Bot_16',
    'Half_Bot_17', 'Half_Bot_18', 'Half_Bot_19', 'Half_Bot_20', 'Half_Bot_21', 'Half_Bot_22',
    'Half_Bot_23', 'Half_Bot_27', 'Half_Bot_33', 'Half_Bot_34', 'Half_Bot_36', 'Half_Bot_38', 
    'Half_Bot_41', 'Half_Bot_42', 'Half_Bot_43', 'Half_Bot_44', 'Half_Bot_45', 'Half_Bot_46',
    'Half_Bot_47'
]

real_top = ['Half_Top_02','Half_Top_01']
real_mid = ['Half_Mid_01','Half_Mid_02']
real_bot = ['Half_Bot_01','Half_Bot_03']


#loads in the known hive runes
colnames = ['tops', 'mids', 'bots']
data = pd.read_csv('../Hive_Rune_Database_Half.csv', names=colnames)

variant = Variant(data)

for i in range(len(top)):
    top_im = cv2.imread(dir + "Tops/" + top[i] + ".png")
    for j in range(len(mid)):
        mid_im = cv2.imread(dir + "Mids/" + mid[j] + ".png")
        for k in range(len(bot)):
            bot_im = cv2.imread(dir + "Bottoms/" + bot[k] + ".png")

            img = np.vstack([top_im,mid_im,bot_im])
            save_name = top[i] + '_' + mid[j]+ '_' + bot[k] + ".png"


            for r in data:
                
                #if this is in the database it shouldn't be saved
                
                print(top[i],mid[j],bot[k])
                
                if ((data['tops'] == top[i]) & (data['mids'] == mid[j]) & (data['bots'] == bot[k])).any() == True:
                    save_dir = 'Half/Real/'
                    real = color_change(img,real = True)
                    cv2.imwrite( save_dir + save_name,real)
                    print("This rune is real")
                    continue
                
                if top[i] in broken_top and bot[k] in broken_bot:
                    print("This rune would break the rules!")
                    continue
                
                if mid[j] == 'Half_Mid_01' and i > 26 and k > 26:
                    print("This rune would break the rules!")
                    continue
                
                if mid[j] == 'Half_Mid_04' and i < 26 and k < 26:
                    print("This rune would break the rules!")
                    continue
                
                
                #check to see if the rune is variant
                variant_search = [top[i],mid[j],bot[k]]
                
                if variant_search in variant:
                    print("This is a Variant Rune")
                    flip = color_change(img,flip=True)
                    save_dir = 'Half/Variant/'
                    cv2.imwrite( save_dir + save_name,flip)
                
                elif top[i] in real_top and mid[j] in real_mid and bot[k] in real_bot:
                    print("This is a Hypothetical Rune")
                    hypo = color_change(img,hypo=True)      
                    save_dir = 'Half/Hypothetical/'
                    cv2.imwrite( save_dir + save_name,hypo)
            
                #if this isn't in the database and the parts are fake
                else:
                    print("This is a Imaginary Rune")
                    imag = color_change(img,imag=True)      
                    save_dir = 'Half/Imaginary/'
                    cv2.imwrite( save_dir + save_name,imag)
