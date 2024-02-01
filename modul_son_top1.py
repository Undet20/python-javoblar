# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:55:38 2024

@author: Acer
"""

# 1-MODUL
a=1
b=2
def son_top():
    import random as r
    urinish=1
    oylangan_son=r.randint(1,10)
    javob=int(input("1 dan 10 gacha son o'yladim Topa olasizmi?;\n>>"))
    while oylangan_son!=javob:
        if oylangan_son>javob:
            javob=int(input("Xato men o'ylagan son bundan kattaroq. \
Yana harakat qiling:\n>>"))
            urinish+=1
        elif oylangan_son<javob:
            javob=int(input("Xato men o'ylagan son bundan kichikroq. \
Yana harakat qiling:\n>>"))
            urinish+=1
    print(f"TOPDINGIZ! {javob} sonini o'ylagan edim. {urinish} ta tahmin"
          f" bilan topdingiz. Tabriklayman!!")
    return urinish

def son_top2():
    import random as r
    past=1
    baland=10
    javob=r.randint(past, baland)
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    ishora=True
    urinish=1
    while ishora:
        qiymat=input(f"Siz {javob} sonni o'yladingiz: to'g'ri(T),men "
                     f"o'ylagan son bundan kattaroq (+), yoki kichikroq"
                     f" (-)?? ") # 4 s o'y.giz
        if qiymat.lower()=="t":
            ishora=False
        elif qiymat=="+":
            past=javob+1
            javob=r.randint(past,baland) # 5-10     6
            urinish+=1
        elif qiymat=="-":
            baland=javob-1 # baland=6
            javob=r.randint(past,baland) # (6-1=5)      
            urinish+=1
    print(f"Soningizni {urinish} ta taxmin bilan topdim.")
    return urinish






