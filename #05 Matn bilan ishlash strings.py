# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:53:30 2023

@author: Acer
"""
# 05-mavzu Matn bilan ishlash (strings)
# "," operatori matnni bitta joy tashlab qo'shadi
# Misol
print("salom","do'stim") # konsolga salom do'stim deb chiqaradi
# "+" operatori yordamida matnlarni bir-biriga qo'shamiz
# misol
ism="Akbar"
matn="Mening ismim "
print("Mening ismim "+ism)
print(matn+ism)
familiya="Saidov"
print(ism+' '+familiya)
# bu yerda "+" operatoridan foydalanganimizda hech qanday joy tashlamaydi
# Misol
print("Saidov"+"Akbar") # Konsolga SaidovAkbar deb chiqaradi
# f-string usuli
ism_sharif=f"{ism} {familiya}"
print(f"ism sharif {ism_sharif}")
ism_sharif=f"{ism+' '+familiya}"
print(f'ikkinchi ism sharif {ism_sharif}')
# "\t" belgisi uzun bo`shliq qoldiradi
# misol
print("Hello World!") # konsolga Hello World! deb chiqaradi
print("Hello \tWorld!") # konsolga Hello 	World! deb chiqaradi
# String metodlari
# Metodlarni chaqirish uchun matn.metod() kodidan foydalanamiz
# 1. .upper() metodi-Barcha harflarni katta harfga almashtiradi
# misol
print(ism_sharif.upper()) # Konsolga AKBAR SAIDOV deb chiqaradi
# 2. lower() metodi-Barcha harflarni kichik harfga almashtiradi
# misol
print(ism_sharif.lower()) # Konsolga akbar saidov deb chiqaradi
ism_sharif=ism_sharif.lower()
# 3. title() metodi-har bir so`zning bosh harfini katta harfga almashtiradi
# Misol
print(ism_sharif.title()) # Konsolga Akbar Saidov deb chiqaradi
# 4. capitalize() metodi-faqat matnnig birinchi harfini katta harfga o`tkazadi.
# Misol
print(ism_sharif.capitalize()) # Consolda Akbar saidov deb chiqadi
# lstrip() metodi-chap tomondagi bo`shliqni olib tashlaydi
# Misol
meva="      olma        "
print("uyda "+meva.lstrip(),"bor") # Konsolga uyda olma         bor deb chiqaradi
# rstrip metodi-o`ng tomondagi bo'shliqni olib tashlaydi
# Misol 
print("uyda "+meva.rstrip(),"bor") # konsolga uyda       olma bor deb chiqaradi
# strip metodi so`zning ikki tomonidagi bo`shliqlarni olib tashlaydi
# Misol
# Bundan buyon konsolda nima chiqasa print ortidan yoziladi
print("uyda",meva.strip(),"bor") # uyda olma bor
# Input funksiyasi
# Input funksiyasi foydalanuvchi tomonidan qabul qilib olinadigan ma'lumot
ism=input("Ismingiz nima?\n>>>")
print("Assalomu alaykum",ism)

# Topshiriqlar
# 1. O'zgaruvchilarni yaratish
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
# 2.
print(kocha,"ko'chasi",mahalla,"mahallasi",tuman,"tumani",viloyat,"viloyati")


