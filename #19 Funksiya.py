# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:40:42 2024

@author: Acer
"""

# 19-DARS. FUNKSIYA
# # Funksiya ma'lum bir kodlar yig'indisi ya'ni bir necha kodlar yig'indisi
# # Endi o'zimiz funksiya yaratib ko'ramiz.
# def salom_ber(): # def so'zi funksiya yaratmoqchi ekanligimizni bildiradi.
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")
    
# salom_ber()
# salom_ber()
# # Funksiyaga nom berayotganimizda fel ya'ni birir bir harakatni angla-
# # tuvchi nom berishimiz kerak. Boshqa nom bersak keyinchalik qaysi biri
# # o'zgaruvchi yoki qaysi biri funksiya ekanligiga adashib ketishimiz
# # mumkin.

# # Endi funksiyaga parametr berib ko'ramiz.
# def salom_ber(ism): # qavs ichidagi parametr
#     """Foydalanuvchi ismini qabul qilib 
#     salom beruvchi funksiya""" # docstring. funksiya haqida ma'lumot
#     print(f"Assalomu alaykum hurmatli {ism.title()}!")

# salom_ber("hasan")
# salom_ber("olim") 
# # Foydalanuvchi uchun argument dasturchi uchun parametr deyiladi.
# # Funksiya haqida ma'lumotni ekranga chiqarish uchun quyidagicha yozamiz.
# print(salom_ber.__doc__)

# # Bazida funksiyaga bir necha parametrlarni ham shakllantirishimiz ham
# # mumkin. Misol
# def toliq_ism(ism,familiya):
#     """Ism familiyani to'liq chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}")
#     print(f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism("Akbar","Saidov") # Argumetlarni kiritganimizda parametr ketma-
# # ketligida kiritishimiz kerak. Aks holda hato natija chiqaradi.
# # Agar funksiya parametri bilan bir xil argumnet bilan qiymatini yozsak 
# # ketmaketlik muhim bo'lmaydi. Misol.
# def yosh_hisobla(ism,tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur."""
#     print(f"{ism.title()} {2024-tugilgan_yil} yoshda.")
# yosh_hisobla(tugilgan_yil=2000,ism="akbar") # funksiya parametri bilan
# # yozilgan argument bir xil bo'lishi shart

# # Endi standart qiymat berib funksiya yozamiz
# def yosh_hisobla(tugilgan_yil,joriy_yil=2024): # joriy_yil 2024 bu yerda
#     """Yoshni hisoblovchi funksiya""" # standart qiymat
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(2000,2024)
# yosh_hisobla(2000) # 2024 deb yozmasak ham natija chiqaveradi. Agar funk-
# # siya yaratishda joriy qiymat berilmaganda edi dastur xatolik berar edi.

# Funksiyadan foydalanishdan maqsad bir necha bor uzun kodlarni yozib
# o'tirmasdan funksiya ichiga biriktirib so'ng faqat funksiyaga murojat
# qilamiz. Ya'ni qayta-qayta uzun kodlarni yozib o'tirmasdan funksiya-
# ning o'zidan foydalanib qo'yamiz.

# TOPSHIRIQLAR
# # 1-topshiriq
# def t_yil_hisobla(yosh,joriy_yil=2024):
#     """Tug'ilgan yilini hisoblovchi funksiya"""
#     print(f"Siz {joriy_yil-yosh}-yilda tug'ilgansiz.")
# t_yil_hisobla(24)

# # 2-topshiriq
# def kv_kub_hisobla(son):
#     """Sonning kvadrat va kubini hisoblovchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga teng")
#     print(f"{son} ning kubi {son**3} ga teng")
# kv_kub_hisobla(5)

# # 3-topshiriq
# def juft_toq_aniqla(son):
#     """Sonning juft yoki toqligini hiasoblovchi funksiya"""
#     if son%2==0:
#         print(f"{son} soni juft son")
#     else:
#         print(f"{son} soni toq son")
# juft_toq_aniqla(13)
# juft_toq_aniqla(124)

# # 4-topshiriq
# def taqqosla(son1,son2):
#     """Sonni taqqoslovchi funksiya"""
#     if son1>son2:
#         print(son1,">",son2) 
#     elif son1==son2:
#         print(son1,"=",son1)
#     else:
#         print(son1,"<",son2)
# taqqosla(5,7)
# taqqosla(9,3)
# taqqosla(5,5)

# # 5-topshiriq
# def daraja(x,y):
#     """X ning y darsjasini hisoblovchi funksiya"""
#     print(f"{x} ning {y} darajasi {x**y}")
# daraja(5,3)
# daraja(2,10)

# # 6-topshiriq
# def daraja(x,y=2):
#     """X ning y darsjasini hisoblovchi funksiya"""
#     print(f"{x} ning {y} darajasi {x**y}")
# daraja(3)
# daraja(9)

# 7-topshiriq
def qoldiqsiz_bol(son):
    for raqam in range(2,11):
        if son%raqam==0:
            print(f"{son} soni {raqam} soniga qoldiqsiz bo'linadi")
qoldiqsiz_bol(99)
qoldiqsiz_bol(100)


