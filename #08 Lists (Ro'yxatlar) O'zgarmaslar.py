# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 07:31:59 2023

@author: Acer
"""

# 08-mavzu Lists (Ro'yxatlar) O'zgarmaslar
cars=["bmw","mercedez benz","volvo","general motors","tesla","audi"]
# sort() metodi ro'yxat elementlarini alifbo tartibida taxlaydi.
# Misol
print(cars)
cars.sort() # ro'yxat tartibga solinadi
print(cars)
# Alifbo tatibida katta va kichik harflar turlicha taxlanadi ya'ni
# katta harf kichik harfdan oldin keladi.
# Misol
cars=['Bmw','mercedez benz',"volvo","general motors","tesla","audi"]
print(cars)
cars.sort() # ro'yxat tartibga solinadi.
print(cars)
# Bu yerda katta harf birinchi kelib keyin kichik harflar boshlana-
# yapti. Bunday kamchiliklarga duch kelmaslik uchun upper(),lo-
# wer(),title() metodlaridan foydalanamiz.
# Emdi ro'yxatni teskari tartibda joylashtiramiz
cars=["bmw","mercedez benz","volvo","general motors","tesla","audi"]
cars.sort(reverse=True)# reverse degani teskari tartibda degani
print(cars)
cars=["bmw","mercedez benz","volvo","general motors","tesla","audi"]
# Asl ro'yxatga teginmagan holatda consolga chiqaramiz
print(sorted(cars))
# Ro'yxatni teskarisiga aylantirib qo'yish
# Misol
print("Asl ro'yxat:",cars)
cars.reverse()
print("Teskariga aylantirilgan ro'yxat:",cars)
cars.reverse()
# len metodi-ingliz tilida lengs so'zidan olingan bo'lib uzunlik
# degan ma'noni bildiradi. Bu asosan ro'yxat ichida qancha qiymat
# borligini aniqlashda ishlatiladi.
# range() funksiyasi ma'lum bir oraliqdagi sonlarni qaytaradi.
# sonlar ketma-ketligini ro'yxatga o'tkazish.
sonlar=list(range(0,10)) # ikkinchi sonimiz 10 gacha sonlar kira-
# di 10 ning o'zi kirmaydi.
print("Sonlar ro'yxati:",sonlar)
# range() funksiyasi yordamida qadamlarni ham olishimiz mumkin.
# Misol
toq_sonlar=list(range(1,10,2)) # bu yerda 2 soni 2 qadam tashlab
# yurish.
print("Toq sonlar:",toq_sonlar)
juft_sonlar=list(range(0,10,2))
print("Juft sonlar:",juft_sonlar)
uchlik=list(range(3,30,3)) # bu yerda 3 soni endi 3 qadam sanala-
# digan sonlar ketma-ketligi
print("Uchga bo'linadigan sonlar:",uchlik)
# Ro'yxat ichidan eng katta va eng kichik sonni topish
print("Eng katta son:",max(sonlar))
print("Eng kichik son:",min(sonlar))
# Ro'yxatlar ichidagi qiymatlar yig'indisini topish funksiyasi
print("1 dan 9 gacha bo'lgan sonlar yig'indisi:",sum(sonlar))
# Ro'yxatlarni kesish funksiyasi
print(cars[0:3]) # bu yerda 0 dan 3 gacha elementlarni ekranga
# chiqariladi 3-indeksning o'zi chiqmaydi.
print(cars[:2]) # Bu 2-indeksgacha degani. 0 dan boshlanadi
print(cars[2:]) # Bu 2-indeksdan oxirigacha degani.
# RO'YXATDAN NUSXA OLISH
# my_cars=cars deb kiritilsa bitta ro'yxatga 2 ta nom berib qo'ya-
# di. Nusxa olish uchun kesish [:] amalidan foydalanamiz.
# Misol
my_cars=cars[:] # boshidan oxirigacha kesib my_carsga yuklaydi
# tuple o'zgarmas ro'yxat bilan ishlash 
# O'zgarmas ro'yxat bilan tanishish
toys=("bus","car","bear","dino","snake","lizard")
# ro'yxat bilan tuplening farqi shundaki tuple o'zgarmas bo'lib
# yaratilishda elementlari oddiy qavs "()" ichida yoziladi
# Biz o'zgarmas ro'yxatni o'zgartirishga majbur bo'lsak oddiy
# ro'yxatga o'tkazib o'zgartiramiz, so'ng yana o'zgarmas ro'yxat-
# ga qaytaramiz. Misol
print("O'zgarmas ro'yxat:",toys)
toys=list(toys) # oddiy ro'yxatga o'tkaziladi
toys.append("teddy") # Ro'yxatga yangi element qo'shamiz.
toys=tuple(toys) # O'zgarmas ro'yxatga o'tkazamiz.

# TOPSHIRIQLAR
davlatlar=["Rossiya","AQSH","Kanada","Xitoy","Finlandiya"]
print("Davlatlar:",davlatlar)
print("Ro'yxat uzunligi:",len(davlatlar))
print("Tartiblangan ro'yxat:",sorted(davlatlar))
print("Teskari tartiblangan ro'yxat:",sorted(davlatlar,reverse=True))
print("Asl ro'yxat:",davlatlar)
davlatlar.reverse()
print("Aylantirilgan ro'yxat:",davlatlar)
davlatlar.sort()
print("Alifbo tartibda;",davlatlar)
davlatlar.sort(reverse=True)
print("Teskari alifbo tartibda;",davlatlar)
# 120 dan 1200 gacha juft sonlarni tuzish
juft_sonlar=list(range(120,1201,2))
yigindi=sum(juft_sonlar)
print("Juft sonlar yig'indisi:",yigindi)
# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani 
# hisoblang va konsolga chiqaring
print("Ro'yxatdagi eng katta va eng kivchik son ayirmasi:",
max(juft_sonlar)-min(juft_sonlar))
print("Ro'yxat Elementlari soni:",len(juft_sonlar))
print("Boshidan 20 ta qiymat:",juft_sonlar[:20])
print("O'rtasidan 20 ta qiymat",
juft_sonlar[len(juft_sonlar)//2-(20//2):len(juft_sonlar)//2+(20//2)])
print("Oxiridagi qiymat:",juft_sonlar[-20:])
taomlar=["Osh","Manti","Lag'mon","Sho'rva","Shashlik"]
nonushta=taomlar[:] # Taomlarni nonushtaga nusxa oladi.
nonushta[0]="Tuxum"
del nonushta[2]
nonushta.remove("Shashlik")
nonushta.append("Gumma")
print("Nonushtalar:",nonushta)
print("Taomlar:",taomlar)
nonushta=tuple(nonushta)






