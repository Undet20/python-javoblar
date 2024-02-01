# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:37:03 2024

@author: Acer
"""

# 25-DARS SONNI TOPISH O'YNI
import modul_son_top1 as m
ishora=True
while ishora:
    print("Keling o'ylagan sonni topish o'ynaymiz!")
    a=m.son_top()
    print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
    b=m.son_top2()
    if a==b:
        print(f"Durrang ikkimiz ham {a} ta tahmin bilan topdik.")
    elif a<b:
        print(f"Men {b} ta taxmin bilan topdim. Siz {a} ta taxmin bilan"
              f" topdingiz. Siz yutdingiz.")
    elif a>b:
        print(f"Men {b} ta taxmin bilan topdim. Siz {a} ta taxmin bilan"
              f" topdingiz. Siz yutqazdingiz.")        
    ishora=bool(int(input("Yana o'ynaymizmi: ha(1) / yo'q(0) ")))
















