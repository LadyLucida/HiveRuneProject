import os
import csv
import numpy as np
import cv2
import pandas as pd


def fix(folder):
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
            mnew = 1
        if mnum == 2:
            mnew = 5
        if mnum == 3:
            mnew = 3
        if mnum == 4:
            mnew = 4
        if mnum == 5:
            mnew = 2
        if mnum == 6:
            mnew = 7
        if mnum == 7:
            mnew = 6
        
        
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

       
dir = "../Parts/Full/"
top = fix("Tops/")
mid = fix("Mids/")
bot = fix("Bottoms/")  

broken_top = [
    'Top_13','Top_14','Top_15','Top_16','Top_17','Top_18','Top_19','Top_20','Top_21','Top_22',
    'Top_23','Top_24','Top_28','Top_29','Top_33','Top_34','Top_35','Top_36','Top_37','Top_38',
    'Top_39','Top_40','Top_41','Top_42','Top_43','Top_44','Top_45','Top_46','Top_47','Top_48',
    'Top_49','Top_50','Top_51','Top_52','Top_53','Top_54','Top_55','Top_56','Top_60','Top_61',
    'Top_62','Top_63','Top_64','Top_65','Top_66','Top_67','Top_69','Top_70','Top_71','Top_72',         
    'Top_73','Top_74','Top_75','Top_76','Top_77','Top_78','Top_79','Top_80','Top_81',               
]
                
broken_bot = [
    'Bot_13','Bot_14','Bot_15','Bot_16','Bot_17','Bot_18','Bot_19','Bot_20','Bot_21','Bot_22',
    'Bot_23','Bot_24','Bot_28','Bot_29','Bot_33','Bot_34','Bot_35','Bot_36','Bot_37','Bot_38',
    'Bot_39','Bot_40','Bot_41','Bot_42','Bot_43','Bot_44','Bot_45','Bot_46','Bot_47','Bot_48',
    'Bot_49','Bot_50','Bot_51','Bot_52','Bot_53','Bot_54','Bot_55','Bot_56','Bot_60','Bot_61',
    'Bot_62','Bot_63','Bot_64','Bot_65','Bot_66','Bot_67','Bot_69','Bot_70','Bot_71','Bot_72',         
    'Bot_73','Bot_74','Bot_75','Bot_76','Bot_77','Bot_78','Bot_79','Bot_80','Bot_81',               
]
                
circle_top = [
    'Top_04','Top_05','Top_17','Top_18','Top_19','Top_34','Top_38','Top_39','Top_40','Top_31',
    'Top_44','Top_45','Top_58','Top_61','Top_65','Top_66','Top_67','Top_71','Top_72',
]

circle_bot = [
    'Bot_04','Bot_05','Bot_17','Bot_18','Bot_19','Bot_34','Bot_38','Bot_39','Bot_40','Bot_31',
    'Bot_44','Bot_45','Bot_58','Bot_61','Bot_65','Bot_66','Bot_67','Bot_71','Bot_72',
]      

triangle_top = [
    'Top_05','Top_08''Top_18','Top_19','Top_23','Top_24','Top_25','Top_38','Top_39','Top_40',
    'Top_49','Top_50','Top_51','Top_65','Top_66','Top_67','Top_76','Top_77','Top_78',
]

triangle_bot = [
    'Bot_05','Bot_08''Bot_18','Bot_19','Bot_23','Bot_24','Bot_25','Bot_38','Bot_39','Bot_40',
    'Bot_49','Bot_50','Bot_51','Bot_65','Bot_66','Bot_67','Bot_76','Bot_77','Bot_78',
]

real_top = [
    'Top_01','Top_02','Top_03','Top_04','Top_05','Top_06','Top_07','Top_08','Top_09','Top_10',
    'Top_11','Top_12','Top_14','Top_26','Top_27','Top_28','Top_29','Top_30','Top_31','Top_32',
    'Top_33','Top_34','Top_35','Top_55','Top_57','Top_58','Top_60','Top_61','Top_62'       
]

real_mid = ['Mid_01','Mid_02','Mid_03','Mid_04','Mid_05']

real_bot = [
    'Bot_01','Bot_02','Bot_03','Bot_04','Bot_05','Bot_06','Bot_07','Bot_08','Bot_09','Bot_10',
    'Bot_11','Bot_14','Bot_23','Bot_26','Bot_27','Bot_33','Bot_35','Bot_55','Bot_57','Bot_59',
    'Bot_61'  
]

#loads in the known hive runes
colnames = ['tops', 'mids', 'bots']
data = pd.read_csv('Hive_Rune_Database.csv', names=colnames)

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
                    save_dir = 'Hypothetical/Real/'
                    real = color_change(img,real = True)
                    cv2.imwrite( save_dir + save_name,real)
                    print("This rune is real")
                    continue
                
                if top[i] in broken_top and bot[k] in broken_bot:
                    print("This rune would break the rules!")
                    continue
                
                if mid[j] == 'Mid_03' and top[i] not in circle_top and bot[k] not in circle_bot:
                    print("This rune would break the rules!")
                    continue
                
                if top[i] == 'Top_26' and bot[k] not in triangle_bot or bot[k] == 'Bot_26' and top[i] not in triangle_top:
                    print("This rune would break the rules!")
                    continue
                
                if (
                    top[i] == 'Top_10' and mid[j] != 'Mid_04' or 
                    top[i] == 'Top_12' and mid[j] != 'Mid_04' or
                    top[i] == 'Top_27' and mid[j] != 'Mid_04' or  
                    bot[k] == 'Bot_10' and mid[j] != 'Mid_04' or 
                    bot[k] == 'Bot_12' and mid[j] != 'Mid_04' or
                    bot[k] == 'Bot_27' and mid[j] != 'Mid_04'     
                    ):
                    print('This rune would break the rules')
                    continue
                
                #check to see if the rune is variant
                variant_search = [top[i],mid[j],bot[k]]
                
                if variant_search in variant:
                    print("This is a Variant Rune")
                    flip = color_change(img,flip=True)
                    save_dir = 'Variant/'
                    cv2.imwrite( save_dir + save_name,flip)
                
                elif top[i] in real_top and mid[j] in real_mid and bot[k] in real_bot:
                    if mid[j] == 'Mid_02' or mid[j] == 'Mid_05':
                        print("This one has the wonky middle")
                    else:
                        print("This is a Hypothetical Rune")
                        hypo = color_change(img,hypo=True)      
                        save_dir = 'Hypothetical/'
                        cv2.imwrite( save_dir + save_name,hypo)
            
                #if this isn't in the database and the parts are fake
                else:
                    if mid[j] == 'Mid_02' or mid[j] == 'Mid_05':
                        print("This one has the wonky middle")
                    else:
                        print("This is a Imaginary Rune")
                        imag = color_change(img,imag=True)      
                        save_dir = 'Imaginary/'
                        cv2.imwrite( save_dir + save_name,imag)
