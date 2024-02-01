# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:29:41 2024

@author: Acer
"""
def avto_info(kompaniya,model,rangi,korobka,yili,narxi=None): # None us-
# tunlik tomoni if operatoriga qo'ysa False qiymat qaytaradi. Shunday
# ko'plab foydali amallarni bajarish mumkin.
    avto={
          "kompaniya":kompaniya,
          "model":model,
          "rangi":rangi,
          "korobka":korobka,
          "yili":yili,
          "narxi":narxi
          }
    return avto
def avto_malumot():
    avto1=avto_info("GM","Malibu","Qora","Avtomat",2018)
    avto2=avto_info("GM","Gentra","Oq","Mexanika",2016,15000)
    avtolar=[avto1,avto2]
    print("Onlayn bozordagi mavjud avtomashinalar:")
    for avto in avtolar:
        if avto["narxi"]: # agar avto narx mavjud bo'lsa
            narx=avto['narxi']
        else:
            narx="noma'lum"
        print(f"{avto['rangi']} {avto['model']} narxi {narx}")

def avto_ruyxat():
    print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
    avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:",end="")
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narxi=input("Narxi: ")
    # Foydalanuvchi kiritgan ma'lumotlardan avto_info funksiyasi yordamida
    # lug'at shakllantirib har bir lug'atni ro'yxatga qo'shamiz.
        avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narxi))
    #  yana avto qo'shish qo'shmasligini so'raymiz.
        javob=input("Yana avto qo'shasizmi? (yes/no):")
        if javob=="no":
            break
    print("\nSalonimizdagi mavjud avtomashinalar:")
    for avto in avtolar:
        if avto["narxi"]: # agar avto narx mavjud bo'lsa
            narx=avto["narxi"]
        else:
            narx="noma'lum"
        print(f"{avto['model'].title()} {avto['rangi'].title()} Krobkasi \
    {avto['korobka'].title()} Ishlab chiqarilgan yili: {avto['yili']}-yil \
    narxi {narx} $")
