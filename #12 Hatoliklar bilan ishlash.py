# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 21:16:58 2024

@author: Acer
"""
# 12-MAVZU xATOLIKLAR BILAN ISHLASH
    # Xatoliklar 3 turga bo'linadi.
    # Sinteks xatoliklar
# EOF deb xatolik chiqarsa qaysidir funksiyani qavsini yopish esdan chi-
# qib qolsa uni o'zimiz topib to'g'irlashimiz kerak bunday xatolarni qa-
# yerda borligini dastur ko'rsatmaydi. EOF degani funksiya yakunida xato-
# lik bo'ldi degani. Uni o'zimiz qarab tekshiramiz
# EOL deb xatolik chiqarsa qaysidir qatorning oxirida xatolik bor degani
# qo'shtirnoq va qavsni yopish esdan chiqqanda EOL deb chiqadi.

    # IndentationError xatoligi-bu surish xatoligi agar print funksiyasi
# oldidan kutilmaganda bo'sh joy bo'lsa IndentationError deb chiqaradi
# sikl badanida joy tashlashda bir xil joy tashlash kerak bu qat'i qoida
# aks holda xato beradi.

    # Run time Error xatoligi dastur bajarilish vaqtida xatoliklar keyin
# kelib chiqadi.
# 1. TypeError-ma'lum bir ma'lumot turi bilan bajarib bo'lmaydigan amalni
# bajarsak chiqadi.
# 2. NameError xatoligi ma'lum bir o'zgaruvchi yoki funksiya nomini xato
# yozib qo'yishdan kelib chiqadi.
# 3. ValueError xatoligi noto'g'ri qiymat berib qo'yganimizda kelib chi-
# qadi. misol uchun son=int(input("Istalgan son kiriting: ")) kodni ba-
# jarsak foydalanuvchi o'nlik son kiritib qo'yganda chiqadi.
# 4. IndexError xatoligi ro'yxatdagi index raqamini noto'g'ri berib qo'y-
# ganda chiqadi. ya'ni chegaradan oshib ketganda chiqadi.
# 5. ZeroDivisionError xatoligi 0 ga bo'lish xatoligi

# MANTIQIY XATOLAR
# Misol ildiz chiqarish 9**1/2 xato hisoblanadi 9 ning 1-darajasi 9 va
# uni 2 ga bo'ladi. 9**(1/2) bu yerda 9 ning 0.5-darajasi ildizini beradi

# TOPSHIRIQLAR
# 27/11/2020
# Dasturlash asoslari
#12-dars: Xatolar
# Muallif: Anvar Narzullaev
# Web sahifa: https://python.sariq.dev
# """

# # 1-topshiriq
# son = float(input("Juft son kiriting: "))
# if son%2!=0:
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# 2-topshiriq
# yosh = int(input("Yoshingiz nechida? "))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
    
# print(f"Chipta {narh} so'm")

# # 3-topshiriq
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# # 4-topshiriq
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
    
# # 5-topshiriq
# users = ['alisher1983','aziza','yasina','umar']

# login = input("Yangi login tanlang:")

# if login.lower() in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")















