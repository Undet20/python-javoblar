# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:23:35 2024

@author: Acer
"""

# 26-DARS SO'ZNI TOPISH O'YINI
import random as r
from uzwords import words
def get_word():
    return r.choice(words)
def display(harflar,tasodif_soz):
    harf=''
    for s in tasodif_soz:
        if s in harflar:
            harf+=s
        else:
            harf+="-"
    return harf
def play():
    soz=get_word().upper()
    harflar=""
    kiritilgan_harf="" # kiritilgan harf 
    print(f"Мен {len(soz)} хонали сон ўйладим. Топа оласизми?")
    print(display(harflar,soz))
    while True:
        if harflar==soz:
            break
        else:    
            hh=(input("Ҳарф киритинг: ")).title()
            
            harflar=display(kiritilgan_harf,soz)
            if hh not in kiritilgan_harf:
                kiritilgan_harf+=hh
            elif hh in kiritilgan_harf:
                print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг")
            elif hh not in soz:
                print("Бундай ҳарф йўқ")
            elif hh in soz:
                print(f"{hh} ҳарфи тўғри")
            
            print(harflar)
            print("Киритган ҳарфларингиз",kiritilgan_harf)    
    print(f"Табриклайман! {soz} сўзини {len(kiritilgan_harf)} уринишда"
          f" топдингиз")       
    
# Bu kodni o'zim mustaqil tuzdim. Bu kodni tuzishga ancha qiynaldim. Umid
# qilamanki, keyingi darslarning topshirig'ini dars mobaynida bajarib
# boraman.
            
        
play()        
        
        

        