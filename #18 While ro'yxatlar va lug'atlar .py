# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:06:04 2024

@author: Acer
"""

# 18-DARS WHLE RO'YXATLAR VA LUG'ATLAR

# # While sikli yordamida ro'yxatlar bilan ishlaymiz. Misol
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n}-do'stingizning ismini kiriting:\n>>>"
#     ism=input(savol)
#     ismlar.append(ism)
#     takrorlash=input("Yana ism qo'shasizmi? (ha/yo'q)\n>>>")
#     n+=1
#     if takrorlash != 'ha':
#         break
# print("Do'stlaringiz ro'yxati")
# for ism in ismlar:
#     print(ism.title())

# # Endi lug'at bilan ishlaymiz.
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("Do'stingiz ismini kiriting: ")
#     yosh=input("Do'stingiz yoshini kiriting: ")
#     dostlar[ism]=int(yosh)
#     javob=input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob=="yo'q":
#         ishora=False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda.")              

# # Endi while sikli yordamida ro'yxat ichidagi bir nechta qiymatlarni
# # o'chirib tashlashni ko'ramiz.
# cars=["lasetti","nexiya","toyota","nexiya","audi","malibu","nexiya"]
# # remove metodining kamchiligi shundaki ro'yxat ichida bir nechta bir
# # element bo'lsa faqat birinchisini o'chiradi holos.
# # Agar hamma bir xil element o'chirilishi kerak bo'lsa u holda while
# # siklidan foydalanamiz. Misol
# while "nexiya" in cars: # toki cars ichida nexiya bor ekan
#     cars.remove('nexiya') # mana bu ifodani bajar.
# print(cars) # 'nexiya' elementi hammasi o'chgandan keyin sikldan chiqadi

# # Keyingi misolimiz.
# talabalar=["hasan","husan","olim","botir"]
# baholangan_talabalar={}
# while talabalar: # toki talabalar ichida bitta bo'lsa ham elemant bo'lsa
#     talaba=talabalar.pop() # mana bu kodni bajar.
#     baho=input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba]=int(baho) # toki ro'yxat bo'shaguncha ayla-
#     # naveradi. pop() metodiga indeks kiritilmasa oxirgi elementdan su-
#     # g'urib oladi.
    
# TOPSHIRIQLAR

# # 1-topshiriq
# print("Nima buyurtma berasiz.")
# qiymat=''
# buyurtmalar=[]
# n=1
# while True:
#     qiymat=input(f"{n}-buyurtmangiz:") 
#     buyurtmalar.append(qiymat)
#     javob=input("Yana buyurtma berasizmi? (ha/yo'q)\n>>>")
#     if javob=="ha":
#         n+=1
#     elif javob=="yo'q":
#         break
#     else:
#         while (javob=='ha' or javob=="yo'q")!=True:
#             javob=input("Noto'g'ri qiymat kiritildi. Qayta yozing\n>>>")
#         if javob=="yo'q":
#             break
#         elif javob=="ha":
#             n+=1
# print("Dastur tugadi")      
        
# # 2-topshiriq Mahsulot va ularning narxini chiqarish
# print("Mahsulot va ularning narxlarini chiqaramiz.")
# e_bozor={}
# ishora=True
# while ishora:
#     mahsulot=input("Mahsulotni kiriting: chiqish uchun exitni ki\
# riting\n>>>")
#     if mahsulot=="exit":
#         ishora=False
#     else:   
#         narx=input("Mahsulotning narxini kiriting:\n>>>")
#         e_bozor[mahsulot]=int(narx)
# for mahsulot,narx in e_bozor.items():
#     print(f"{mahsulot}ning narxi {narx} so'm")
# print("Dastur tugadi.")    

# # 3-topshiriq
# e_bozor={"olma":20000,"anor":18000,"shaftoli":17000,"uzum":16000}
# buyurtmalar=["olma","uzum","shaftoli","o'rik"]
# while buyurtmalar:
#     savat=buyurtmalar.pop()
#     if savat in e_bozor.keys():
#         narx=e_bozor[savat]
#         print(f"{savat} {narx} so'm")


















