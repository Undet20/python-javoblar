# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 07:15:17 2024

@author: Acer
"""

# 28-DARS OBJECT ORIENTED DASTURLASH CLASSLAR

# # Endi pythonda o'zimiz obyekt yaratishni ko'ramiz. Albatta obyekt uchun
# # class yaratishimiz kerak. Class obyekt uchun shablon hisoblanadi.
# class Talaba: # iloji boricha yangi class nomini katta harf bilan boshlash
# # kerak o'zgaruvchi va classni ajratish uchun.
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#         # endi talaba bajarishi mumkin bo'lgan metodlarini yozamiz. Misol
#     def tanishtir(self):
#         print(f"Ismim {self.ism} familiyam {self.familiya} {self.tyil}-"
#               f"yilda tug'ilganman.")
#     def get_name(self):
#         return self.ism
#     # Endi qo'shimcha argumentlar ham berib ko'ramiz.
#     def get_age(self,yil):
#         return yil-self.tyil
#         # endi shu classdan obyekt yaratamiz.
# talaba1=Talaba("Olim","Olimov",2000) # mana shu shablon asosida turlicha
# talaba2=Talaba("Hasan","Husanov",1995) # obyekt yaratishimiz mumkin.
# talaba3=Talaba("Akram","Alimov",2004) # bu hususiyatlari Eni talaba baja-
# # rishi mumkin bo'lgan metodlarini yaratamiz.
# print(talaba1.get_age(2024)) # bitta argument qabul qiladi va yoshini
# # chiqaradi.

# TOPSHIRIQLAR

# 1-2-topshiriqlar
class User():
    def __init__(self,foydalanuvchi,ism,familiya,tyil,email):
        self.foydalanuvchi=foydalanuvchi
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.email=email
        self.yil=2024
    def info(self):
        return (f"Foydalanuvchi: {self.foydalanuvchi} \nIsmi " 
                f"{self.familiya.capitalize()} {self.ism.capitalize()} "
        f"\nTug'ilgan yili: {self.tyil}-yil.\nYoshi: {self.yil-self.tyil} "
        f"\nElektron pochtasi: {self.email}")

akbar=User("Akbar2000","Akbar","Saidov",2000,"akbarsaidov614@gmail.com")
print(akbar.info())


