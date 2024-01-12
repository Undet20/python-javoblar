# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:21:07 2024

@author: Acer
"""

# 10-mavzu if-else shartlari va tarmoqlanish
# if so'zi ingliz tilidan olingan bo'lib agar degani. Ya'ni kodlash jara-
# yonida agar bu narsa bajarilsa bunga o't, bajarilmasa bunga o't degani.
avtolar=["audi","bmw","volvo","kia","hyundai"]
for avto in avtolar:
    if avto=="bmw": # Agar avto bmwga teng bo'lsa
        print(avto.upper()) # bu kodni bajar
    else: # Aks holda
        print(avto.title()) # bu kodni bajar
# Bu yerda 2 ta tenglik belgisi "==" tengmi degan so'zni beradi
# hozir avto hyundaiga teng. agar biz avto=="bmw" ga tengmi deb yozsak
# natija False deb chiqaradi agar biz avto=="hyundai" deb yozsak natija
# True deb chiqaradi.Ya'ni True rost, False yolg'on degani
ism='Ali'
ism.lower()=="ali" # bu yerda true natija beradi
# endi teng emasmi "!=" shartini ko'ramiz misol
a=5
a!=6 # True natijani beradi
ism=input("Ismingiz nima?\n>>>")
if ism.lower()!="ali": # Agar ism ali bo'lmasa
    print(f"Uzr {ism.title()} biz Alini kutayapmiz.")
else:
    print("Salom Ali")
javob=input("12x6 nechiga teng?\n>>>")
if javob!=72: # Agar 72 ga teng bo'lmasa
    print("Javob xato!") # else kiritilmadi kiritish zarurat bolmasa
# shart emas. 72 kiritilsa hech qanday amal bajarilmaydi.
yosh=int(input("Assalomu alaykum yoshingiz nechida?\n>>>"))
if yosh>=18: # 18 dan katta yoki teng bo'lsa
    print("Xush kelibsiz!")
else:
    print("Kirish mumkin emas")
# bu yerda yosh>18  18 dan kattami,yosh<18 18 dan kichikmi,yosh<=18
# 18 dan kichik yoki tengmi
login=input("Yangi login tanlang:\n>>")
if len(login)<=5: # login uzunligi 5 tadan kichik yoki tengligi tekshi-
# riladi.
    print("Login 5 tadan ko'p bo'lishi kerak.")
yil=int(input("Tug'ilgan yilingizni kiriting:\n>>>"))
if 2023-yil<18: print(f"Siz {2023-yil} yoshda ekansiz kirish mumkin emas!")
else: # bu yerda shartdan keyin kod yozib ketish mumkin
    print(f"Siz {2023-yil} yoshdasiz xush kelibsiz!")
# kodni bir tekis yozib ketishimiz ham mumkin
# Misol
x,y=25,50 # x=25, y=50
print("x>y") if x>y else print("x<y")
#  TOPSHIRIQLAR
# 1-topshiriq
cars=["toyota","mazda","Hyundai","gm",'kia']
for car in cars:
    if car=="gm":
        print(car.upper())
    else:
        print(car.title())
# 2-topshiriq
cars=["toyota","mazda","Hyundai","gm",'kia']
for car in cars:
    if car!="gm":
        print(car.title())
    else:
        print(car.upper())
# 3-topshiriq
foydalanuvchi_ismi=input("Login yoki ismingizni kiriting:\n>>>")
if foydalanuvchi_ismi.lower()=="admin":
    print(f"Xush kelibsiz {foydalanuvchi_ismi.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz {foydalanuvchi_ismi.title()}!")
# Oxirgi topshiriq
son=int(input("Istalgan son kiriting:\n>>>"))
if son>0: print(float(son)**float(0.5))
else: print("Musbat son kiriting:")





