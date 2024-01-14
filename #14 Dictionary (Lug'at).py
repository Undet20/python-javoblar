# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:34:12 2024

@author: Acer
"""

# # 14-dars Dictionary Lug'at
# # Har bir ma'lumot 2 qismdan iborat
# # 1. Kalit so'z
# # 2. Qiymat    Mana shu kalit so'zga to'g'ri keluvchi qiymat
# # Bu narsa "Key-Value pair" ya'ni "Kalit so'z-qiymat juftligi" deb atala-
# # di. Misol
# car_0={"model":"firrari","rang":"qizil"} # bu yerda 1-qiymati kalit so'z
# # 2-qiymati esa uning qiymat
# print(car_0["model"])
# print(car_0["rang"])
# talaba_0={"ism":'murod olimov',"yosh":24,"t_yil":2000}
# print(f"{talaba_0['ism'].title()}, \
# {talaba_0['t_yil']}-yilda tug'ilgan, \
# yoshi {talaba_0['yosh']} da") # bu yerda "\" belgisi pastki qatordan da-
# # vomli yozish uchun ishlatiladi.

# # Lug'atga yangi element qo'shish
# talaba_0["kurs"]=4
# talaba_0["fakultet"]="informatika"

# # Bo'sh lug'at yaratamiz
# talaba_1={}
# talaba_1["ism"]="qobil rasulov"
# talaba_1["kurs"]=3
# talaba_1["yosh"]=20
# print(f"talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs.")

# # Lug'atni elementini yangilash
# talaba_1["kurs"]=4

# # Lug'at elementini o'chirish
# talaba_0={"ism":'murod olimov',"yosh":24,"t_yil":2000}
# del talaba_0["yosh"]

# # Lug'atlarni bir nechta qatorda yozish
# # Lug'atlar juda uzun bo'lib ketadigan bo'lsa bir nechta qatorlarda yo-
# # zamiz Misol
# telefonlar={
#     "ali":"iphone x",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310"
#     }

# # get() metodi.
# # Agar biz   telefonlar['hasan']   deb kiritadigan bo'lsak KeyError deb
# # xatolik chiqaradi. Bunday xatolikning oldini olish uchun .get() meto-
# # didan foydalanamiz. Misol
# phone=telefonlar.get("hasan","Bunday ism mavjud emas") # agar lug'atda 
# print(phone) # hasan degan kalit bo'lmasa bunday ism mavjud emas degan 
# # habarni chiqaradi. Demak biz get metodi yordamida  1 o'zgaruvchiga 2 ta
# # qiymatdan birini berar ekanmiz. 
# # Agar lug'atda kalit mavjud bo'lsa uning qiymati, yoki
# # vergul qo'yib qo'shtirnoq ichida o'zimiz qiymat beramiz
# # Agar  phone=telefonlar.get(hasan)  deb yozilsa konsolda "none" deb chi-
# # qaradi. Uning o'zbekchaga tarjimasi mavjud emas degani

# # TOPSHIRIQLAR
# # 1-topshiriq
# otam={"ism":"fazliddin","t_yil":1971,"t_joy":"qo'shrabot"}
# onam={"ism":"gulshod","t_yil":1976,"t_joy":"qo'shrabot"}
# akam={"ism":"sayilboy","t_yil":1995,"t_joy":"qo'shrabot"}
# print(f"Otamning ismi {otam['ism'].title()} {otam['t_yil']}-yilda,\
# {otam['t_joy'].capitalize()} tumanida tug'ilgan.")
# print(f"Onamning ismi {onam['ism'].title()} {onam['t_yil']}-yilda,\
# {onam['t_joy'].capitalize()} tumanida tug'ilgan.")
# print(f"Akamning ismi {akam['ism'].title()} {akam['t_yil']}-yilda,\
# {akam['t_joy'].capitalize()} tumanida tug'ilgan.")

# # 2-topshiriq
# taomlar={
#     "ali":"osh",
#     "vali":"shashlik",
#     "hasan":"kabob",
#     "husan":"norin",
#     "olim":"somsa"
#     }
# print("Alining sevimli taomi",taomlar["ali"])
# print(f"Vali {taomlar['vali']}ni juda yaxshi ko'radi")
# print(f"Hasan {taomlar['hasan']}ga juda ko'p boradi")

# # 3-topshiriq Python izohli lug'atini tuzish
python_lugat={"print":"konsolga chiqaruvchi funksiyasi","int":"butun \
son","float":"o'nlik son","string":"matn","upper":"barcha harflarni \
katta harfga o'tkazish","lower":"barcha harflarni kichik harfga \
o'tkazish","title":"har bir so'zning birinchi harfini katta harfga \
almashtiradi.","capitalize":"matnning faqat birinchi harfini bosh \
harfga almashtiradi.","if":"shart operatori bajarilsa","else":"aks \
holda"}
# kalit=input("Kalit so'zni kiriting: ")
# print(python_lugat.get(kalit,"bunday kalit so'z mavjud emas."))

# 4-topshiriq
tarjima=python_lugat
kalit_soz=input("Biror so'z kiriting: ")
soz=tarjima.get(kalit_soz)
if soz==None:
    print("Bunda so'z mavjud emas")
else:
    print(f"{kalit_soz} so'zi {soz} deb tarjima qilinadi")








