# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 20:30:01 2024

@author: Acer
"""

# 20-DARS FUNKSIYADAN QIYMAT QAYTARISH
# def toliq_ism_yasa(ism,familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism=f"{ism.title()} {familiya.title()}"
#     return toliq_ism # return so'zi qiymat qaytaradi.
# talaba=toliq_ism_yasa("olim","hakimov")
# print(talaba)

# # Ixtiyoriy argument
# # foydalanuvchidan 3 ta 4 ta argument qabul qiladi ba'zilarini biz ixti-
# # yoriy qilishimiz ham mumkin.
# def toliq_ism_yasa(ism,familiya,otasining_ismi=""):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi: # agar o'zgaruvchida 1 dana ham element bo'lsa
# # if operatori True qaytaradi.
#         toliq_ism=f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism.title()
# print(toliq_ism_yasa("akbar","saidov","fazliddin o'g'li"))
# print(toliq_ism_yasa("akbar","saidov"))
# ism_familiyam=toliq_ism_yasa("akbar","saidov","fazliddin o'g'li")
# print(ism_familiyam)

# # Funksiya ichida lug'atlarni shakllantiramiz.
# def avto_info(kompaniya,model,rangi,korobka,yili,narxi=None): # None us-
# # tunlik tomoni if operatoriga qo'ysa False qiymat qaytaradi. Shunday
# # ko'plab foydali amallarni bajarish mumkin.
#     avto={
#           "kompaniya":kompaniya,
#           "model":model,
#           "rangi":rangi,
#           "korobka":korobka,
#           "yili":yili,
#           "narxi":narxi
#           }
#     return avto
# avto1=avto_info("GM","Malibu","Qora","Avtomat",2018)
# avto2=avto_info("GM","Gentra","Oq","Mexanika",2016,15000)
# avtolar=[avto1,avto2]
# print("Onlayn bozordagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["narxi"]: # agar avto narx mavjud bo'lsa
#         narx=avto["narxi"]
#     else:
#         narx="noma'lum"
#     print(f"{avto['rangi']} {avto['model']} narxi {narx}")
    
# # Funksiyadan ro'yxat qaytarishini ko'ramiz
# def oraliq(min,max):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# # range ingliz tilidan oraliq deb tarjima qilinadi.
# print(oraliq(0,10))
# print(oraliq(10,21))

# # Avtolar ro'yxatini shakllantirish
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:",end="")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi: ")
# # Foydalanuvchi kiritgan ma'lumotlardan avto_info funksiyasi yordamida
# # lug'at shakllantirib har bir lug'atni ro'yxatga qo'shamiz.
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narxi))
# #  yana avto qo'shish qo'shmasligini so'raymiz.
#     javob=input("Yana avto qo'shasizmi? (yes/no):")
#     if javob=="no":
#         break
# print("\nSalonimizdagi mavjud avtomashinalar:")
# for avto in avtolar:
#     if avto["narxi"]: # agar avto narx mavjud bo'lsa
#         narx=avto["narxi"]
#     else:
#         narx="noma'lum"
#     print(f"{avto['model'].title()} {avto['rangi'].title()} Krobkasi \
# {avto['korobka'].title()} Ishlab chiqarilgan yili: {avto['yili']}-yil \
# narxi {narx} $")

# TOPSHIRIQLAR
# # Oraliq funksiyasini yozish.
# def oraliq(min,max,qadam=None):
#     sonlar=[]
#     if qadam:
#         while min<max:
#             sonlar.append(min)
#             min+=qadam
#     else:
#         while min<max:
#             sonlar.append(min)
#             min+=1
#     return sonlar

# print(oraliq(0,10))
# print(oraliq(0,10,2))

# 1-topshiriq
# Foydalanuvchi haqida ma'lumot
def foydalanuvchi_lugat(ism,familiya,t_yil,t_joy,yosh,e_maili="",tel_raqam=None):
    foydalanuvchi_haqida={
                          "ism":ism,
                          "familiya":familiya,
                          "t_yil":t_yil,
                          "t_joy":t_joy,
                          "yosh":yosh
                          }
    if e_maili:
        if e_maili!=type(int):
            foydalanuvchi_haqida['e_mail']=e_maili
    if tel_raqam:
        foydalanuvchi_haqida['tel_raqam']=tel_raqam
    return foydalanuvchi_haqida
# lugat=foydalanuvchi_lugat("Akbar", "Saidov", 2000, "Samarqand",24)
# print(lugat)

# # 2-topshiriq
# mijozlar=[]
# while True:
#     ism=input("Ismizgiz: ")
#     familiya=input("Familiyangiz: ")
#     t_yil=int(input("Tug'ilgan yilingiz: "))
#     t_joy=input("Tug'ilgan joyingiz: ")
#     yosh=int(input("Yoshingiz: "))
#     e_maili=input("Elektron pochtangiz (Ixtiyoriy): ")
#     tel_raqam=input("Telefon raqamingiz (ixtiyoriy): ")
#     mijozlar.append(foydalanuvchi_lugat(ism, familiya, t_yil, t_joy, yosh,e_maili,tel_raqam))
#     javob=input("Yana foydalanuvchilar kiritasizmi? (ha/yo'q): ")
#     if javob=="yo'q":
#         break
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()} "
#           f"{mijoz['t_yil']}-yilda {mijoz['t_joy']}da tug'ilgan. Yoshi "
#           f"{mijoz['yosh']} yoshda telefoni {mijoz['tel_raqam']}")
    
# # 3-topshiriq
# def kattasi(x,y,z):
#     max=x
#     if max<=y:
#         max=y
#     if max<=z:
#         max=z
#     return max
# print(kattasi(5,-7,3))

# # 4-topshiriq
# def aylana_info(radius,pi=3.14159):
#     aylana_lugat={
#         "radius":radius,
#         "diametr":radius*2,
#         "perimetr":2*radius*pi,
#         "yuza":pi*radius**2
#         }
#     return aylana_lugat
# print(aylana_info(5))

# 5-topshiriq
# def tub_sonlar_top(min,max):    
#     tub_sonlar = []    
#     for n in range(min,max+1): # 1 DAN 20 gacha sonlar kiritiladi
#         tub = True
#         if (n==1): # agar n 1 ga teng bo'lsa
#             tub = False # tub False bo'lsin
#         elif(n==2): # n 2 ga teng bo'lsa
#             tub = True # tub true bo'lsin
#         else: # aks holda
#             for x in range(2,n): # 2 dan n gacha sonlar oralig'i
#                 if(n%x==0): # agar n ni x ga bo'lganda qoldiq 0 bo'lsa
#                     tub = False # tub false bo'lsin
#         if tub: # agar tub True bo'lsa
#             tub_sonlar.append(n) # tub sonlarga n sonini qo'sh            
#     return tub_sonlar # tub_sonlar qiymatni qaytar.
# tub_sonlar_top(1,20)

# 6-topshiriq
def fibonachchi(son):
    fib_son=[1,1]
    for n in range(son-2):
        fib_son.append(fib_son[n]+fib_son[n+1])
    return fib_son
print(fibonachchi(18))
    
# 2-ko'rinish
def fib(son):
    fib_son=[]
    for n in range(son):
        if n==0 or n==1:
            fib_son.append(1)
        else:
            fib_son.append(fib_son[n-1]+fib_son[n-2])
    return fib_son
fibonachchi(10)







