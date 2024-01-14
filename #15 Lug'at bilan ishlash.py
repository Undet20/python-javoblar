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

# Sets ma'lumot turi haqida-Bunday ma'lumot turi ham o'z tarkibi ichiga
# string ro'yxat va lu'at kabi ma'lumotlarni qabul qiladi Misol
toys={"ball","car","lamp","ball","bear","car"} # Diqqat! set ichidagi 
# elementlar takrorlanmaydi









