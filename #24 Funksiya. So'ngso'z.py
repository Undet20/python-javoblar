# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:22:20 2024

@author: Acer
"""

# 24-DARS FUNKSIYA. SO'NGSO'Z
# import math
# # Biz nomsiz funksiya yaratishni ko'ramiz.
# # lambda argument:ifoda ko'rinishda bo'ladi misol.
# uzunlik=lambda pi,r:2*pi*r 
# print(uzunlik(math.pi,10)) # uzunlik bu yerda indentifikator deyiladi.

# kvadrat=lambda x,y:x**y
# print(kvadrat(3,2))

# # Endi bir misol ko'ramiz.
# def daraja(n): # Bu funksiyamiz daraja yasaydigan funksiya bo'ldi.
#     return lambda x:x**n

# kvadrat=daraja(2)
# kub=daraja(3)
# print(kvadrat(6))
# print(kvadrat(9))
# print(kub(3)) # Demak lambda funksiyasidan boshqa funksiya ichida qo'l-
# # lash foydalanish qulay ekan.

# # Endi lambda funksiyasining ikkinchi qulayligini ko'ramiz.
# # Shunday funksiyalar bor bu funksiyalar argument sifatida boshqa funk-
# # siyalarni qabul qilib oladi. Keyin qandaydir qiymatlar qaytaradi.
# # Mana shunday funksiyalardan biri map() funksiyasi.
# from math import sqrt
# sonlar=list(range(11))
# ildizlar=list(map(sqrt,sonlar)) # map funksiyasi qanday ishlaydi. map
# print(ildizlar) # funksiyasi sonlar argumentni oladi. Keyin shu ro'yxat-
# # larni birinchi argument funksiyaga yuboradi. Odatda map funksiyasining
# # o'zi ro'yxat qaytarmaydi,obyekt qaytaradi. shuning uchun listga o'tka-
# # zib olamiz.

# Daraja funksiyasini yozib olamiz.
def daraja2(x):
    """Berilgan sonning kvadratini hisoblovchi funksiya"""
    return x*x

# # Endi map() funksiyasi yordamida ro'yxatdagi qiymatlarni darajaga ko'-
# # taramiz.
# darajar=list(map(daraja2,sonlar)) # map funksiyasi ichida birinchi argu-
# print(darajar) # mentda qavslar "()" bo'lmaydi. Faqat argumnet nomi bo'-
# # ladi. Aslida buning osonroq yo'li lambda yordamida edi. lambda funksi-
# # yasidan foydalansak buni osongina quyidagicha ko'rinishda yozamiz.
# # Misol 

sonlar=list(range(11))
kvadratlar=list(map(lambda x:x*x,sonlar)) # map funksiyasi tarkibida bi-
# rinchi argumentda funksiya nomi yo'q shuning uchun bu funksiyamiz nom-
# siz funksiya deb ataladi.Yuqoridagi kod bilan hozirgi kodni solishtir-
# sak ancha qisqa va oson bo'ldi.
print(kvadratlar)

# # map funksiyasi uchun yana boshqa amallarni ham ko'rishimiz mumkin.
# a=[4,5,6]
# b=[7,8,9]
# a_plus=list(map(lambda x,y:x+y,a,b))
# print(a_plus)

# Yana bir misol ko'ramiz. lambda funksiyasini yana qayerda ko'rishimiz
# mumkin.
import random as r
sonlar=r.sample(range(100), 10)
# print(sonlar)

# def juftmi(x):
#     return x%2==0

# juft_sonlar=list(filter(juftmi,sonlar)) # filter degani saralash degani
# # bu yerda sonlar ro'yxatini juftmi funksiyasiga yuboradi. Agar True
# # bo'lsa o'sha juft sonni juft_sonlar degan yangi ro'yxatga yuklaydi.

# # Lekin juftmi funksiyasi 1 marta kerak u holda lambda funsiyasidan foy-
# # dalanamiz. Misol
# juft_sonlar=list(filter(lambda x:x%2==0,sonlar))
# print(juft_sonlar)

# # lambda yordamida faqat sonlar bilan emas balki matnlar bilan ham ish-
# # lashimiz ham mumkin.
mevalar=["olma","anor","anjir","shaftoli","o'rik","tarvuz","qovun","banan"]
# harf="a"
# mevalar_a=list(filter(lambda meva:meva.startswith(harf),mevalar))
# print(mevalar_a)

# Endi uzunligi bo'yicha elementlarni chiqaramiz.
mevalar_2=list(filter(lambda meva:len(meva)<=5,mevalar))
print(mevalar_2)

mevalar_3=list(filter(lambda meva:(meva.startswith("a") and meva.endswith("r")),mevalar))
# Bu kod boshi a harfdan boshlanib tugashi r harfidan tugaydigan so'z-
# larning ro'yxatini Shakllantiradi.
print(mevalar_3)




