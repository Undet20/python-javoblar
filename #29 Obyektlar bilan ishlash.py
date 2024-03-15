# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 22:41:02 2024

@author: Acer
"""

# 29-DARS OBYEKTLAR BILAN ISHLASH
# class Talaba: # iloji boricha yangi class nomini katta harf bilan boshlash
# # kerak o'zgaruvchi va classni ajratish uchun.
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         self.bosqich=1
#         # endi talaba bajarishi mumkin bo'lgan metodlarini yozamiz. Misol
#     def tanishtir(self):
#         return (f"{self.ism} {self.familiya} {self.bosqich}-bosqich talaba"
#               f"si")
#     def update_bosqich(self):
#         self.bosqich+=1
#     def get_name(self):
#         return self.ism
#     # Endi qo'shimcha argumentlar ham berib ko'ramiz.
#     def get_age(self,yil):
#         return yil-self.tyil
#     def get_lastname(self):
#         return self.familiya
#     def full_name(self):
#         return self.ism+" "+self.familiya
# talaba1=Talaba("Akbar","Saidov",2000)
# talaba1.ism # bunday ko'rinish tavsiya berilmaydi classimiz takomillashi
# # mumkin. O'zgartirish kiritilishi mumkin. Boshqa dasturchilar classimiz-
# # ni foydalanganda kod hato ishlashi mumkin. Metod o'zini o'zgartiramiz
# # holos.

# # talaba1.bosqich=2
# # print(talaba1.tanishtir())

# # talaba1.update_bosqich()
# # print(talaba1.tanishtir())

# # Endi yangi class yaratamiz
# class Fan:
#     """Fan nomli class"""
#     def __init__(self,nomi):
#        self.nomi=nomi
#        self.talabalar_soni=0
#        self.talabalar=[]
       
#        # Endi yangi mahsus metod qo'shamiz.
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni+=1
# # Bu talabalarni ekranga chiqarish uchun chiroyli metod yozamiz.
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [talaba.full_name() for talaba in self.talabalar]

        
from Kerakli_kodlarim import methods # methodsni dasturimizga yuklaymiz.

# matematika=Fan("Oliy matematika")
# talaba1=Talaba("Akbar","Saidov","2000")
# talaba2=Talaba("Ali","Valiyev",2001)
# talaba3=Talaba("Hasan","Alimov",2001) # Obyektlar yaratamiz.
# matematika.add_student(talaba1) # Talaba obyektlarni Matematika Obyektga
# matematika.add_student(talaba2) # qo'shamiz.
# matematika.add_student(talaba3) 

# print(matematika.get_students())
# methods(Talaba) # classda qanaqa metodlar borligini ko'rish mumkin.
# print(talaba1.__dict__) # Obyektning hususiyatlarini lug'at ko'rinishda 
# # chiqaradi
# print(talaba1.__dict__.keys()) # lug'at kalitlarini chiqaradi.
# # Biz faqat classni emas balki obyektlarni ham chiqarishimiz mumkin.
# # Misol
# print(methods(talaba1)) # bunda faqat metod emas balki xususiyatlarni ham
# # chiqaradi.

# TOPSHIRIQLAR

# # 1-topshiriq
# class Avto():
#     def __init__(self,model,rang,karobka,narx):
#         self.model=model
#         self.rang=rang
#         self.karobka=karobka
#         self.narx=narx
#         self.kilometr=0
#     def get_info(self):
#         return (f"Modeli:{self.model}\nRangi:{self.rang}\nKarobkasi:"
#                 f"{self.karobka}\nNarxi:{self.narx}\nYurgan kilometri:"
#                 f"{self.kilometr}")
#     def update_km(self,km):
#         self.kilometr=km
        
        
# class Avtosalon():
#     def __init__(self,salon_nomi,manzili,sotuvdagi_avtomobillar):
#         self.salon_nomi=salon_nomi
#         self.manzili=manzili
#         self.sotuvdagi_avtomobillar=sotuvdagi_avtomobillar
#     def add_avto(self,avto):
#         self.sotuvdagi_avtomobillar.append(avto)
#     def get_avto(self):
#         return (f"Salon:{self.salon_nomi}\nManzili:{self.manzili}\nso"
#                 f"tuvdagi avtomobillar:{self.sotuvdagi_avtomobillar}")
        


# salon=Avtosalon("chevrolet","samarqand",["gentra","spark"])

# salon.get_avto()

print(methods(int))
print(methods(str))



