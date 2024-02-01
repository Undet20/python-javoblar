# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 07:59:33 2024

@author: Acer
"""

# 22-DARS MOSLASHUVCHAN FUNKSIYALAR
# Shaunday funksiya yarataylikki istalgancha argument qabul qilsin.

# # 1. *args usuli-tarjimasi argumentlar degani u orqali istalgancha argumnet ki-
# # ritish mumkin. Misol
# def summa(*sonlar): # *sonlar argumenti o'zgarmas ro'yxat ko'rinishida 
#     yigindi=0 # shakllanadi
#     for son in sonlar:
#         yigindi+=son # sonlarni yig'indiga jamlaymiz.
#     return yigindi
# print(summa(1,2,3,4,5))
# print(summa()) # umuman son kiritilmasa ham dastur ishlayveradi.

# # 2. **kwargs Keyword arguments-Kalit so'zli argumnetlar degani
# # U argumnet orqali ro'yxatlarni shakllantiramiz. yozilishida 
# # kalitso'z=qiymat ko'rinishida yoziladi. Misol
# def english(**lugatlar):
#     return lugatlar
# lugatlar = english(reply="javob bermoq",salom="zo'r")

# # 1-topshiriq
# def kopaytma(*sonlar):
#     natija=1
#     for son in sonlar:
#         natija*=son
#     return natija
# print(kopaytma(1,2,3,4,5))

# 2-topshiriq
def talaba_info(ism,familiya,**malumot):
    talabalar={
            "ism":ism.title(),
            "familiya":familiya.title()
            }
    for kalit,qiymat in malumot.items():
        talabalar[kalit]=qiymat
    return talabalar
studentlar=talaba_info("akbar", "saidov", kurs=3,fakutet="cholg'u \
ijodiyoti",yunalish="rubob")

















