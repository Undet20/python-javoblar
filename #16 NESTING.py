# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 17:19:47 2024

@author: Acer
"""
# 16-dars NESTING.
# # Nesting so'zi ingliz tilidan olingan bo'lib ya'ni bir narsaning ichida
# # boshqa bir narsani saqlash. bu narsa istalgancha tarmoqlanib ketaveradi
# # Endi lug'atlardan ro'yxat yaratishni ko'ramiz.
# car0={
#      "model":"lacetti",
#      "rang":"oq",
#      "yil":2018,
#      "narx":13000,
#      "km":50000,
#      "karobka":"avtomat"
#       }
# car1={
#       "model":"nexiya 3",
#       "rang":"qora",
#       "yil":2015,
#       "narx":9000,
#       "km":89000,
#       "karobka":"mexanika"
#       }
# car2={
#       "model":"gentra",
#       "rang":"qizil",
#       "yil":2019,
#       "narx":15000,
#       "km":20000,
#       "karobka":"mexanika"
#       }
# cars=[car0,car1,car2]
# car=car0
# print(f"{car['model'].title()} " # bu qator tashlash ko'rinishi
#       f"{car['rang'].title()} rang " # qo'shtirnoq yopiladi qavs oxirida
#       f"{car['yil']}-yil {car['narx']} $") # yopiladi

# # Endi har bir mashina uchun ro'yxat ichidagi lug'atlarni chiqaramiz.
# for car in cars:
#     print(f"{car['model'].title()} "
#           f"{car['rang']} rang "
#           f"{car['yil']}-yil {car['narx']} $")

# # Ro'yxat tarkibidagi lug'at elementini ekranga chiqaramiz
# print(cars[0]['model'].capitalize()) # bu yerda ro'yxat ichidagi 0-inde-
# # ksdagi lug'atning 'model' kalit so'z qiymatini ekranga chiqar degani

# # Endi lug'atlarni for sikli yordamida shakllantiramiz
# malibus=[] # bo'sh ro'yxat yaratamiz. Dastur kodi bo'yicha biz 10 ta ma-
# # libu ishlab chiqarmoqchimiz. for sikl yordamida buni shakllantiramiz
# for n in range(10):
#     new_car={
#         "model":"malibu",
#         "rang":None,
#         "yil":2020,
#         "narx":None,
#         "km":0,
#         "karobka":"avto"
#         }
#     malibus.append(new_car) # 10 ta bir xil yangi moshina yaratildi.

# # Mashinalarni chiroyli ko'rinishda konsolga chiqaramiz.
# for malibu in malibus:
#     print(f"Model:{malibu['model'].capitalize()} "
#           f"Rang:{malibu['rang']} "
#           f"Yil:{malibu['yil']}-yil "
#           f"Narxi:{malibu['narx']} "
#           f"Yurgan yo'li':{malibu['km']} km "
#           f"Karobkasi:{malibu['karobka'].capitalize()} ")

# # Endi 3 ta mashina rangini qizil qilamiz.
# for malibu in malibus[:3]: # 0, 1, 2 indeksdagi lug'atlar ishlaydi
#     malibu['rang']="qizil" # 3 ta mashina qizil rangga o'zgartirildi
    
# # for malibu in malibus:
# #     print(malibu)

# # keyingi 3 ta mashina rangini qora qilamiz.
# for malibu in malibus[3:6]: # 3, 4, 5 indeksdagi lug'atlar ishlaydi
#     malibu['rang']="qora"
# # for malibu in malibus:
# #     print(malibu)

# # Keyingi mashinani qora qilib karobkani mehanika qilamiz.
# for malibu in malibus[6:]: # 6, 7, 8, 9 indekslar ishlaydi.
#     malibu['rang']='qora'
#     malibu['karobka']="mehanika"
# # for malibu in malibus:
# #     print(malibu)

# # Endi bundan ham biroz qiyinroq kod yozamiz.
# for malibu in malibus:
#     if malibu['karobka']=="avto": # agar karobkasi avto bo'lsa narxi
#         malibu['narx']=40000 # narxi 40000 $ bo'lsin, aks holda 35000 $
#     else:                    # bo'lsin deb kod yozdik
#         malibu['narx']=35000
# for malibu in malibus:
#     print(malibu)
    
# # Endi lug'atlar ichida ro'yxatlarni joylaymiz.
# dasturchilar={ # Lug'at kaliti ism, uning qiymati esa ro'yxatlar bo'la-
#     "ali":["python","c++"], # yapti. demas biz bitta kalitga bir nechta
#     "vali":["html","css","js"], # ro'yxatlarni berayapmiz.
#     "hasan":["php","sql"],
#     "husan":["python",'php'],
#     "maryam":["c++","c#"]
#     }
# for ism,tillar in dasturchilar.items():
#     print(ism.title(),"quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper()) # bu yerda dashturlash tillari pastgi qator-
# # dan chiqayapti uni davomli qilishimiz ham mumkin.
# print("Keyingi kodimiz")
# for ism,tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:",end='')
#     for til in tillar:
#         print(f"{til.upper()} ",end='') # bu yerda biz tugash joyini
# # '' ga almashtir degani ya'ni keyingi gal print kelsa davomidan bajari-
# # ladi.

# # Endi lug'at ichida lug'atlarni tuzamiz. Bu kod tavsiya berilmaydi.
# # Agar zarurat bo'lsa bajarishimiz mumkin.
# hamkasblar={
#     "ali":{ # kalit ali. Uning qiymati yana bir lug'at. O'sha lug'at
#         "familiya":"valiyev", # tarkibida ro'yxat ham bor.
#         "tyil":1995,
#         "malumot":"oliy",
#         "tillar":["python","c++"]
#         },
#     "vali":{
#         "familiya":"aliyev",
#         "tyil":2001,
#         "malumot":"o'rta mahsus",
#         "tillar":["html","css","js"]
#         },
#     "hasan":{
#         "familiya":"husanov",
#         "tyil":1999,
#         "malumot":"maxsus",
#         "tillar":["python","php"]
#         }
#     }
# for ism,info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()} "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti {info['malumot']}.\n"
#           f"Quyidagi dasturlash tillarini biladi:", end='')
#     for til in info['tillar']:
#         print(til.upper(),end=' ')

# TOPSHIRIQLAR.

# 1-TOPSHIRIQ
buxoriy={
    "ism":"Imom Al-Buxoriy",
    "tyil":810,
    "vyil":870,
    "tjoy":"Buxoro"
    }
motsart={
    "ism":"Volfgang Amadey Motsart",
    "tyil":1752,
    "tjoy":"Avstriya"
    }    
navoiy={
        "ism":"Alisher Navoiy",
        "tyil":1441,
        "vyil":1501,
        "tjoy":"Hirot"
        }
xorazmiy={
    "ism":"Al-Xorazmiy",
    "tyil":"IX-X asrlar",
    "tjoy":"Xorazm"
    }
shaxslar=[buxoriy,motsart,navoiy,xorazmiy]
# for shaxs in shaxslar:
#     print(f"Ismi {shaxs['ism']}. ",end='')
#     if type(shaxs['tyil'])==str:
#         print(f"{shaxs['tyil']}da yashagan.",end='')
#     elif type(shaxs['tyil'])==int:
#         print(f"{shaxs['tyil']}-yilda tug'ilgan.",end='')
#     print(f"Tug`ilgan joyi {shaxs['tjoy']}. ",end='')
#     emas=(shaxs.get('vyil'))
#     if emas!=None:
#         print(f"U {emas}-yilda vafot etgan.")
#     else:
#         print("")
# Bu topshiriqni o'zim hohlaganimdek bajarishga harakat qilib bajara
# oldim.

# # 2-TOPSHIRIQ
# buxoriy['asarlar']=['hadis',"kitob"]
# motsart['asarlar']=['Sonata','Simfoniya']
# navoiy['asarlar']=['Hamsa',"G'azal"]
# xorazmiy['asarlar']=['algoritm','matematika']
# # Asarlarini ham qo'shib konsolga chiqaramiz.
# for shaxs in shaxslar:
#     print(f"Ismi {shaxs['ism']}. ",end='')
#     if type(shaxs['tyil'])==str:
#         print(f"{shaxs['tyil']}da yashagan.",end='')
#     elif type(shaxs['tyil'])==int:
#         print(f"{shaxs['tyil']}-yilda tug'ilgan.",end='')
#     print(f"Tug`ilgan joyi {shaxs['tjoy']}. ",end='')
#     emas=(shaxs.get('vyil'))
#     if emas!=None:
#         print(f"U {emas}-yilda vafot etgan.",end='')
#     else:
#         print(end="")
#     print("Uning asarlari:",end="")
#     for asar in shaxs['asarlar']:
#         print(f" {asar}",end='')
#     print(".")

# # 3-TOPSHIRIQ
# dadam_filmi=[]
# onam_filmi=[]
# akam_filmi=[]
# singlim_filmi=[]
# print("Dada 3 ta kinoni kiriting!:")
# for kino in range(3):
#     dadam_filmi.append(input(f"{kino+1}-chi kinoyingiz:"))
# print("Ona 3 ta kinoni kiriting!:")
# for kino in range(3):
#     onam_filmi.append(input(f"{kino+1}-chi kinoyingiz:"))
# print("Aka 3 ta kinoni kiriting:")
# for kino in range(3):
#     akam_filmi.append(input(f"{kino+1}-chi kinoyingiz:"))
# print("Singlim 3 ta kinoni kiriting:")
# for kino in range(3):
#     singlim_filmi.append(input(f"{kino+1}-chi kinoyingiz:"))
# kinolar={
#     "dadam":dadam_filmi,
#     "onam":onam_filmi,
#     "akam":akam_filmi,
#     "singlim":singlim_filmi
#     }
# for ism,filmlar in kinolar.items():
#     print(f"{ism}ning filmlari:",end="")
#     for film in filmlar:
#         print(f"{film} ",end="")
#     print("")










