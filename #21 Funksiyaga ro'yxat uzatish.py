# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:01:39 2024

@author: Acer
"""

# 21-DARS FUNKSIYAGA RO'YXAT UZATISH
# def bahola(ismlar):
#     baholar={}
#     while ismlar: # ismlar ichida element bormi
#         ism=ismlar.pop()
#         baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=["ali","vali","hasan","husan"] # diqqat. biz funksiyaga asl
# baholar=bahola(talabalar) # ro'yxatni bergan bo'lamiz. chunki talabalar
# print(baholar) # ismlar ro'yxati bitta xotiraga bog'lanadi.
# print(talabalar)
# # Qanday qilib biz asl ro'yxatimizni saqlab qolishimiz mumkin.
# # Buning uchun nusxa olish ([:]) belgisidan foydalanamiz. Misol
# talabalar=["ali","vali","hasan","husan"]
# baholar=bahola(talabalar[:]) # Funksiyaga ro'yxat nusxasini yubordik.
# print(baholar) 
# print(talabalar) # Ro'yxat o'z joyida turibdi.
# # talabalar2=talabalar ifodasi 2 ta o'zgaruvchini bitta ro'yxatga bog'-
# # lab qo'ydik.
# # Intejer va boshqa o'zgaruvchilarda muammo yo'q faqat ro'yxatlarga te-
# # gishli

# TOPSHIRIQLAR
# # 1-topshiriq
# def katta_harf(ismlar):
#     for son in range(len(ismlar)):
#         ismlar[son]=ismlar[son].title()
#     return ismlar
# matn=["ali","vali","hasan","husan","olim"]
# matn2=katta_harf(matn[:])

# 2-topshiriq
def bahola(ismlar):
    baholar={}
    for ism in ismlar:
        
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar
talabalar=["ali","vali","hasan","husan"]
talabalar2=bahola(talabalar[:])
print(talabalar)
print(talabalar2)


