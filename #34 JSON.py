# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:04:39 2024

@author: Acer
"""

# 34-DARS JSON.
# JSON dastlab java scriptda yaratilgan uning to'liq nomi JavaScript Object
# Notation bo'lgan. Hozirgi vaqtda deyarli barcha dasturlash tillarida JSON
# formatini qollaydigan bo'lgan va ishlaydigan bo'lgan. Keyinchalik biz inter-
# netdan pythonga ma'lumot olmoqchi bo'lsak JSON formatida bo'ladi.
# JSONGA istalgan turdagi ma'lumotlarni saqlashimiz mumkin.
# Pythondagi ma'lumot turlari,quyidagi jadval asosida,JavaScript ma'lumot tur-
# larida konvertatsiya qilinadi.
# Python                            JavaScript
# dict                              Object
# list                              Array
# tuple                             Array
# str                               String
# int                               Number
# float                             Number
# True                              true
# False                             false
# None                              Null
# qoida-JSON o'zgaruvchilar,tarkibidan qat'i nazar matn ko'rinishda saqlanadi.
import json # JSON modulini chaqirib olamiz.
x=10
# Ma'lumotlarni JSON formatiga o'tkazish uchun 2 funksiyadan foydalanamiz.
# json.dumps(x) # berilgan x o'zgaruvchini JSON matniga o'zgartiradi.
# jons.dump(x,fayl) # berilgan x o'zgaruvchini JSON matniga o'zgartirib,korsa-
# tilgan faylga saqlaydi. Misol
x_json=json.dumps(x)
sonlar=[12,45,23,67]
sonlar_json=json.dumps(sonlar)
bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor)
print(bemor_json) # json tarkibini ko'ramiz.
# Yuqoridagi natija o'qish uchun noqulay ko'rinishda chiqdi. Buni to'g'rilash
# uchun dumps() funksiyasiga qo'shimcha indent=4 parametrini beramiz. Bu para-
# metr ma'umotlarni saqlashda chapdan qancha joy tashlashni ko'rsatadi:
bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)

# json.dump() metodi.
# Ma'lumotlarni JSON formatiga o'tkazish va faylga yozish uchun json.dump() 
# funksiyasini chaqriamiz. Funksiya parametri sifatida o'zgaruvchi va fayl nom-
# larini ko'rsatamiz. Albatta buning uchun avval faylni yozish uchun ochgan 
# bo'lishimiz kerak:
with open('bemor.json','w') as f:
    json.dump(bemor,f)
# Jsondan pythonga
# JSON formatidagi ma'lumotlarni Pythondagi ma'lumot turiga keltirish uchun 
# json.loads() yoki json.load() funksiyalaridan foydalanamiz. Yuqoridagi ka'bi, 
# json.loads() funksiyasi to'g'ridan-to'g'ri JSON matn bilan ishlasa, 
# json.load() funksiyasi JSON fayllarni o'qish uchun ishlatiladi.

# json.loads 
# Bu funksiya parametr sifatida JSON matn qabul qiladi va Python o'zgaruvchiga
# o'tkazadi.
sonlar = json.loads(sonlar_json)
bemor = json.loads(bemor_json)
print(bemor)

 # json.load() # Bu funksiya JSON fayllarning tarkibini Pythonga yuklab olish 
# uchun ishlatiladi. 
filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))

# json bilan ishlash
# Ko'pincha internet orqali JSON fayllarni qabul qilganimizda ma'lumotlar bir
# necha qavatli lug'at ko'rinishida bo'ladi. JSON matnidan aynan o'zimizga ke-
# rakli ma'lumotni ajratib olish uchun lug'atni biroz tahlil qilish, uning  
# kalitlari va qiymatlarini topish talab qilinishi mumkin. Bu ayniqsa juda 
# uzun JSON fayllarga tegishli. Shuning uchun JSON bilan samarali ishlash 
# uchun lug'atlar bilan ishlashni yana bir bor takrorlab olishimiz kerak.

# Quyidagi misolda Google Maps hizmati qaytargan JSON matni lug'at ko'rinishi-
# da berilgan. Bu Toshkent shahridagi Olmazor tumanining Geografik manzili.
data = {
    "address_components": [
        {
            "long_name": "Almazar District",
            "short_name": "Almazar District",
            "types": [
                "political",
                "sublocality",
                "sublocality_level_1"
            ]
        },
        {
            "long_name": "Tashkent",
            "short_name": "Tashkent",
            "types": [
                "locality",
                "political"
            ]
        },
        {
            "long_name": "Tashkent Region",
            "short_name": "Tashkent Region",
            "types": [
                "administrative_area_level_1",
                "political"
            ]
        },
        {
            "long_name": "Uzbekistan",
            "short_name": "UZ",
            "types": [
                "country",
                "political"
            ]
        }
    ],
    "formatted_address": "Almazar District, Tashkent, Uzbekistan",
    "geometry": {
        "bounds": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        },
        "location": {
            "lat": 41.3645355,
            "lng": 69.2281531
        },
        "location_type": "APPROXIMATE",
        "viewport": {
            "northeast": {
                "lat": 41.3954567,
                "lng": 69.269883
            },
            "southwest": {
                "lat": 41.3249733,
                "lng": 69.16497629999999
            }
        }
    },
    "place_id": "ChIJ195FnkeMrjgR3nkapKKdk7A",
    "types": [
        "political",
        "sublocality",
        "sublocality_level_1"
    ]
}
# Keling shu ma'lumotlar orasidan tumanning geografik koordinatalrini topamiz.
# Avvalo, lug'atga ko'z yugurtirib chiqib, bizga kerak ma'lumotlar quyidagi 
# ko'rinishda berilganini ko'rishimiz mumkin:
#     "location":{
#         "lat": 41.3645355,
#         "lng": 69.2281531
#             }

# Bizga aynan `latitude` (kenglik) va `longitude` (uzunlik) qiymatlari kerak.
# Ular esa "location" kaliti ichidagi lug'atda lat va lng kalitlariga tegishli
# qiymatlarda joylashgan. location kalitining o'zi ham geometry kaliti ichida
# joylashganini ko'rishimiz mumkin.

# Demak, lu'gat ichidan `lat` va `lng` qiymatlarini olish uchun quyidagi kodni
# yozamiz: 
kenglik = data['geometry']['location']['lat']
uzunlik = data['geometry']['location']['lng']
print(f"{kenglik},{uzunlik}")















