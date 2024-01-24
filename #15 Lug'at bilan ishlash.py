# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 09:21:15 2024

@author: Acer
"""

# # 15-dars LUG'AT BILAN ISHLASH
# # items() metodi-lug'at ichidagi kalit va qiymatlarni bilmasak kalit va
# # qiymatlarni ekranga chiqaramiz. buning uchun items metodidan foydala-
# # namiz. Misol
# talaba_0={
#     "ism":"Alijon",
#     "familiya":"shamshiyev",
#     "yosh":22,
#     "fakkultet":"matematika",
#     "kurs":4
#     }
# print(talaba_0.items()) # natija chiqishi yomon emas lekin uni chiroyli
# # ko'rinishga keltirish kerak.
# for kalit,qiymat in talaba_0.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat}")
# # boshqacha bir ko'rinish
# print("\nKeyingi ko'rinish\n")
# for kalit,qiymat in talaba_0.items():
#     print(kalit,":",qiymat)
# # Yana bir chiroyli ko'rinish
# telefonlar={
#     "ali":"iphone",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310"
#     }
# print("\n")
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
    
# # keys() metodi-Bizga qiymatlar emas faqat kalitlarni chiqarish muhim 
# # bo'lsin. u keys() metodidan foydalanamiz.Misol
# mahsulotlar={
#     "olma":10000,
#     "anor":20000,
#     "uzum":40000,
#     "anjir":25000,
#     "shaftoli":30000
#     } 
# print(mahsulotlar.keys()) # Mahsulotlar kalitini chiqaramiz.
# # Buni foydalanuvchiga chiroyli ko'rinishda qilishimioz ham mumkin.
# print("Do'kondagi mahsulotlar: ")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# # Bu yerda keys metodini ishlatmasak ham kodimizni shu holatda chiqarsak
# # ham bir xil natijani olamiz. Misol
# print("\nKeyingi misolimiz")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
    
# # Endi foydali kod yozib ko'ramiz
# mahsulotlar={
#     "olma":10000,
#     "anor":20000,
#     "uzum":40000,
#     "anjir":25000,
#     "shaftoli":30000
#     } 
# bozorlik=['anor',"uzum","non","baliq"]
# for mahsulot in bozorlik:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
# # Buning aksini ham qilishimiz ham mumkin ekan. Misol
# for buyum in bozorlik:
#     if buyum not in mahsulotlar: # Agar buyum mahsulotlarda bo'lmasa
#         print("Iltimos do'koningizga",buyum,"ham olib keling")
# # Mahsulotlarni alifbo tartibida chiqarish talab qilinishi mumkin. U hol-
# # da sorted funksiyasidan foydalanamiz. Misol
# print("\nDo'kondagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title()) # lekin buyerda asosiy lugat tartibi o'zgar-
# # madi. Misol
# print("\nAsosiy lug'atlar")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
    
# # Values() metodi-Ba'zida bizdan kalitlar emas qiymatlarni chiqarish ta-
# # lab qilinishi mumkin. value degani ingliz tilida qiymat degani Misol
# telefonlar={
#     "ali":"iphone X",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310"
#     }
# print("\nFoydalanuvchilar quyidagi telefonlarni ishlatishadi: ")
# for tel in telefonlar.values():
#     print(tel.title())
    
# # Set funksiyasi
# # Endi uzunroq lug'at tuzamiz.
# telefonlar={
#     "ali":"iphone x",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310",
#     "hamida":"galaxy s9",
#     "maryam":"huwai p30",
#     "tohir":"iphone x",
#     "umar":"iphone x"
#     }
# print("\nKeyingi kodimiz.")
# for tel in telefonlar.values():
#     print(tel.title()) # Bu yerda 2 va undan ortiq bir xil qiymatlar
# # bor. faqat takrorlanmas bitta qiymat qilish uchun set funksiyasini
# # ishlatamiz. Misol
# print("\nFoydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in set(telefonlar.values()):
#     print(tel.title())

# # Sets ma'lumot turi haqida-Bunday ma'lumot turi ham o'z tarkibi ichiga
# # string ro'yxat va lu'at kabi ma'lumotlarni qabul qiladi Misol
# toys={"ball","car","lamp","ball","bear","car"} # Diqqat! set ichidagi 
# # elementlar takrorlanmaydi
# print(toys)

# # TOPSHIRIQLAR
# # 1-TOPSHIRIQ. Python izohli lug'atini yaratish
# print("Python izohli lug'ati:")
# python_lugat={
#     "print":"konsonga chiqarish funksiyasi",
#     "int":"butun son",
#     "float":"o'nlik son",
#     "string":"matn",
#     "list":"ro'yxat",
#     "for":"takrorlash operatori",
#     "set":"bir nechta bir xil matnlarni olib tashlash funksiyasi",
#     "pop":"sug'urib olish metodi",
#     "del":"o'chirish operatori",
#     "len":"qiymat uzunligini tekshirish funksiyasi"
#     }
# for kalit in sorted(python_lugat): # lug'atni alifbo tartibida tartib-
# # laymiz.
#     print(f"{kalit}:\n{python_lugat[kalit]}") # tartiblangan holatda ek-
# # ranga chiqaramiz.

# # 2-topshiriq    Davlatlar va poytaxtlarni chiqarish
# print("Davlatlar va ularning poytaxtlarini tuzamiz.")
# davlatlar={
#     "o'zbekiston":"toshkent",
#     "qozog'iston":"ashxabot",
#     "tojigiston":"dushanbe",
#     "turkmaniston":"bishkek",
#     "rossiya":"moskva",
#     "koreya":'seul',
#     "yaponiya":"tokyo",
#     "hindiston":"dehli",
#     "xitoy":"gongkong"
#     }
# for davlat in sorted(davlatlar):
#     print(f"{davlat.capitalize()}ning puytaxti:\n{davlatlar[davlat]}")
# print("\nEndi poytaxtlarni alifbo tartibida chiqaramiz:")
# for d in sorted(davlatlar, key=davlatlar.get):
#     print(d,":",davlatlar[d])
    
# # 3-topshiriq    
# davlatlar={
#     "o'zbekiston":"toshkent",
#     "qozog'iston":"ashxabot",
#     "tojigiston":"dushanbe",
#     "turkmaniston":"bishkek",
#     "rossiya":"moskva",
#     "koreya":'seul',
#     "yaponiya":"tokyo",
#     "hindiston":"dehli",
#     "xitoy":"gongkong"
#     }
# mamlakat=input("Istalgan davlatni kiriting:\n>>>")
# # if mamlakat in davlatlar:
# #     print(f"{mamlakat.capitalize()}ning poytaxti \
# # {davlatlar[mamlakat].capitalize()}",)
# # else:
# #     print("Bunday davlat mavjud emas.")
# print(davlatlar.get(mamlakat,"Bunday davlat mavjud emas"))

# 4-topshiriq restoran menusini shakllantirish
restoran_menusi={
    "shashlik":11000,
    "osh":28000,
    "somsa":8000,
    "manti":6000,
    "sho'rva":25000,
    "lag'mon":25000,
    "chuchvara":20000,
    "kabob":45000,
    "baliq":40000,
    "norin":30000
    }
buyurtmalar=[]
print("3-ta taom buyurtma bering!")
for taom in range(3):
    buyurtmalar.append(input(f"{taom+1}-chi taom: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in restoran_menusi:
        print(buyurtma,restoran_menusi[buyurtma],"so'm")
    else:
        print("Kechirasiz bizda",buyurtma,"yoq!")




