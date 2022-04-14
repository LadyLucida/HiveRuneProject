from cmath import nan
import os
import csv
from tokenize import Triple
import numpy as np
import cv2
import pandas as pd


def fix(folder):
    dir = "../Parts/Numbers/"
    name = os.listdir(dir + folder)
    name = sorted(name)
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
        search = row.tolist()
        if np.nan in search:
            v = [a for a in search if pd.isnull(a)== False]
            f = v[::-1]
            if f == v:
                print(search)
                print('This rune cannot be flipped')
                continue
            variant.append(f)
        else:
            s = search[::-1]
            if s == search:
                print(search)
                print('This rune cannot be flipped')
                continue
            variant.append(s)

    
    for i in variant:
        print(i)

    return variant

def SaveFunction(data,search,save_name,img,variant,short = True):


    for r in data:
        print('Search:',search)
        if short == True:
            if ((data['num0'] == search[0]) & (data['mid0'] == search[1]) & (data['num1'] == search[2])).any() == True:
                print("This is a Real Rune")
                print()
                real = color_change(img,real=True)
                save_dir = 'Numbers/Real/'
                cv2.imwrite( save_dir + save_name,real)
            else:
                if search in variant:
                    print("This is a Variant Rune")
                    print()
                    flip = color_change(img,flip=True)
                    save_dir = 'Numbers/Variant/'
                    cv2.imwrite( save_dir + save_name,flip)
                else:
                    print("This is a Hypothetical Rune")
                    print()
                    hypo = color_change(img,hypo=True)      
                    save_dir = 'Numbers/Hypothetical/'
                    cv2.imwrite( save_dir + save_name,hypo)

        if short == False:
            if ((data['num0'] == search[0]) & (data['mid0'] == search[1]) &
                (data['num1'] == search[2]) & (data['mid1'] == search[3]) & 
                (data['num2'] == search[4])).any() == True:
                print("This is a Real Rune")
                print()
                real = color_change(img,real=True)
                save_dir = 'Numbers/Real/'
                cv2.imwrite( save_dir + save_name,real)
            else:
                if search in variant:
                    print("This is a Variant Rune")
                    print()
                    flip = color_change(img,flip=True)
                    save_dir = 'Numbers/Variant/'
                    cv2.imwrite( save_dir + save_name,flip)
                else:
                    if search[2] == 'num_00':
                        print("This rune breaks the rules")
                        continue
                    else:
                        print("This is a Hypothetical Rune")
                        print()
                        hypo = color_change(img,hypo=True)      
                        save_dir = 'Numbers/Hypothetical/'
                        cv2.imwrite( save_dir + save_name,hypo)         

dir = "../Parts/Numbers/"
num = fix("Nums/")
mid = fix("Mids/")


#loads in the known hive runes
colnames = ['num0', 'mid0', 'num1','mid1','num2']
data = pd.read_csv('../Hive_Rune_Database_Numbers.csv', names=colnames)


variant = Variant(data)

for num0 in range(len(num)):
    first = num[num0] 
    num0_im = cv2.imread(dir + "Nums/" + first + ".png")
    for num1 in range(len(num)):
        second = num[num1]
        num1_im = cv2.imread(dir + "Nums/" + second + ".png")

        #do small number stuff here
        midS_im = cv2.imread(dir + 'Mids/mid_01.png')
        small_img = np.hstack([num0_im,midS_im,num1_im])
        search = [first,'mid_01',second]
        save_name = '_'.join(search) + '.png'
        SaveFunction(data,search,save_name,small_img,variant,True)
        
        
        for num2 in range(len(num)):
            third = num[num2]
            midL_im = cv2.imread(dir + 'Mids/mid_02.png')
            num2_im = cv2.imread(dir + "Nums/" + third + ".png")
            large_img = np.hstack([num0_im,midL_im,num1_im,midL_im,num2_im])
            search = [first,'mid_02',second,'mid_02',third]
            save_name = '_'.join(search) + '.png'
            SaveFunction(data,search,save_name,large_img,variant,False)


            #do beeg number stuff here
