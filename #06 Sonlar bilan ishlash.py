# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:21:48 2023

@author: Acer
"""
# 06-mavzu Sonlar bilan ishlash
a=5
b=3.6
temp=36.6
# type() funksiyasi qanaqa o'zgaruvchi ekanligini aniqlovchi funksiyasi
# Misol
print(type(temp)) # <class 'float'>
# pythonda "_" ning qulaylik tomoni dasturga juda uzunson kiritilayotgan-
# da qo'llaniladi.
# Misol
aholi_soni=7_594_376_567
print("Aholi soni",aholi_soni,"kishi") # Aholi soni 7594376567 kishi
# Bir nechta o'zgaruvchilarni bitta qatorda qiymat berib yozish ham mumkin
# Misol
x,y,z=12,5.5,"Noutbuk"
print("x="+str(x)+"\ny="+str(y)+"\nz="+str(z))
# Natija
# x=12
# y=5.5
# z=Noutbuk
# bu yerda str(x) degani int qiymat turini str qiymatga o'tkazadi
# str qiymat bilan son qiymatni pythonda "+" operatori yordamida qo'-
# shish mumkin emas shu sababli son qiymatni str qiymatga o'tkazdim
# Konstanta bu o'zgarmas degani. pythonda constanta qiymat yo'qligi sa-
# babli dasturchilar o'zlari kelishib olib Katta harflarda kiritadi
# keyinchalik katta harfli o'zgaruvchiga duch kelganda bu katta harf
# ekan bunga teginmaslik kerak deb teginmasdan o'zgartirmasdan o'tib
# ketadi
radius=20
diametr=2*radius
PI=3.14159 # konstanta o'rnida saqlanadi
# Aylana uzunligini ekranga chiqaramiz
print("Aylana uzunligi",PI*diametr) # Aylana uzunligi 125.6636

# Har qanday foydalanuvchidan olgan ma'lumotni str ko'rinishda qabul
# qiladi. biz uni boshqa o'zgaruvchi turiga o'tkazishimiz mumkin
# Misol
# Foydalanuvchidan tug'ilgan yilini so'raymiz
tugilgan_yil=int(input("Tug'ilgan yilingizni kiriting:\n>>>"))
xabar=2023-tugilgan_yil
print(f"Siz {xabar} yoshda ekansiz") # 2000 kiritilsa natija Siz 23
# yoshda ekansiz deb chiqaradi
# int(), float(), str() funksiyalari mavjud bo'lib o'nlik son ko'rini-
# shidagi matnni (str) butun songa ya'ni int tipiga o'tkazib bo'lmaydi
# dasturda xatolik beradi
 






