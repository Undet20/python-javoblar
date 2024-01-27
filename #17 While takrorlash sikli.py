# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 20:29:43 2024

@author: Acer
"""

# # 17-dars. While tsikli
# # While tsikli ingliz tilidan 'toki' deb tarjima qilinadi.
# son=1
# while son<=5: # toki bu shart bajarilmaguncha
#     print(son,end=" ") # bu ifodani bajar.
#     son+=1 # son=son+1 ifodasi bilan bir xil.
# # Agar shart bajarilmagan holatda while sikldan chiqib ketadi. Ya'ni son
# # 6 ga teng bo'ladi son<=5 shart bajarilmaydi sikldan chiqib ketadi.

# Endi while siklidan input funksiyasidan foydalanishni ko'ramiz.
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan sonni kiriting: "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):\n>>>"
# qiymat=''
# while qiymat!='exit': # Agar qiymat exitga teng bo'lmasa
#     qiymat=input(savol) # foydalanuvchidan qiymat so'raladi
#     if qiymat!='exit': # Agar qiymat exitga teng bo'lmasa
#         print(float(qiymat)**2) # bu ifodani bajar.
        
# # Ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol="Istalgan sonni kiriting: "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):\n>>>"
# qiymat=''
# ishora=True
# while ishora: # Agar ishora True bo'lsa
#     qiymat=input(savol)
#     if qiymat=='exit':
#         ishora=False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi.")

# # Break While-Break ingliz tilidan sindirish to'xtatish deb tarjima qi-
# # lidandi. Misol
# savol="Istalgan sonni kiriting: "
# savol+="(dasturni to'xtatish uchun 'exit' deb yozing):\n>>>"
# qiymat=''
# while True: # Abadiy sikl
#     qiymat=input(savol)
#     if qiymat=="exit": # Agar qiymat exitga teng bo'lsa
#         break # sikl to'xtasin
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtadi.")

# # Break operatorini for sikli uchun ham ko'rishimiz mumkin
# sonlar=list(range(1,11)) # 1 dan 10 gacha sonlar ro'yxati shakllanadi
# for son in sonlar:
#     if son==5: # Agar son 5 ga teng bo'lsa
#         break # siklni to'xtat
#     print(f"{son} ning kvadrati {son**2} ga teng") # keyingi kod ham ba-
# # jarilmaydi.

# # Endi breakning aksi ham bor bu continue deb ataladi. Continue operato-
# # ri yordamida bitta qadam tashlab o'tib ketamiz. Misol
# sonlar=list(range(1,11)) # 1 dan 10 gacha sonlar ro'yxati shakllanadi
# for son in sonlar:
#     if son==5: # Agar son 5 ga teng bo'lsa
#         continue # bir qadam tashla ya'ni keyingi ifodani bajarmay sikl
#     print(f"{son} ning kvadrati {son**2} ga teng") # boshiga qayt.

# # continue While
# son=0
# print("Juft sonlar")
# while son<10:
#     son+=1
#     if son%2!=0: # Agar son 2 ga bo'lgandagi qoldiq 0 ga teng bo'lmasa
#         continue # sikl boshiqa qayt.
#     else:
#         print(son) # juft sonni chiqaruvchi kod.
# son=0
# print("Toq sonlar")        
# while son<10:
#     son+=1
#     if son%2==0: # Agar son 2 ga bo'lgandagi qoldiq 0 ga teng bo'lsa
#         continue # sikl boshiqa qayt.
#     else:
#         print(son) # toq sonni chiqaruvchi kod.

# Abadiy sikl yozib qo'yishdan ehtiyot bo'lishimiz kerak. Bu narsa man-
# tiqiy xatolardan kelib chiqadi. Bular Noto'g'ri shart,o'zgarmas qiymat
# kodlar ketma-ketligida hatolik va hokazo.Agar bunday xato bo'lib qolsa
# ctrl+c knopkalari yoki consol oynasidagi qizil to'rtburchak knopkasini
# bosamiz. Quyidagicha misollarni ko'ramiz.

# son=0
# print("Juft sonlar")
# while son<10: 0 dan 10 gacha
#     # son+=1 kod esdan chiqib qolishi mumkin
#     if son%2!=0: # Agar son 2 ga bo'lgandagi qoldiq 0 ga teng bo'lmasa
#         continue # sikl boshiqa qayt.
#     else:
#         print(son)
        
# # keyingi xatolik
# son=0
# print("Juft sonlar")
# while son<10:
    
#     if son%2!=0: # Agar son 2 ga bo'lgandagi qoldiq 0 ga teng bo'lmasa
#         continue # sikl boshiqa qayt.
#     else:
#         print(son) # Konsolga chiqqanda faqat 1 ta 0 chiqadi dastur tu-
#     son+=1 # gamaydi. buning sababi son+=1 ifodasi son<10: shartidan
# # keyingi pastki qatorda yozilishi kerak bo'ladi.

# # Keyingi abadiy sikl
# son=1
# while son>0: # son<10 deb yozish kerak edi. son>0 ifodasi 0 dan cheksiz
#     son+=1 # songacha degani
#     if son%2!=0:
#         continue
#     else:
#         print(son)
    
# TOPSHIRIQLAR

# # 1-topshiriq
# savol="Eng sevimli kitobingizni kiriting: "
# savol+="Chiqish uchun exitni bosing:\n>>>"
# kitoblar=[]
# qiymat=''
# while qiymat!="exit":
#     qiymat=input(savol)
#     if qiymat!="exit":
#         kitoblar.append(qiymat)
# print("Eng sevimli kitoblaringiz:")
# for kitob in kitoblar:
#     print(kitob)

# # 2-topshiriq
# savol="Yoshingizni kiriting:\n"
# qiymat=''
# narx=0
# while (qiymat=="exit" or qiymat=="quit")!=True:
#     qiymat=(input(savol))
#     if (qiymat=="exit" or qiymat=="quit")!=True:
#         if int(qiymat)<7:
#             narx=2000
#         elif 7<=int(qiymat)<18:
#             narx=3000                     # shart tekshirish ko'rinish
#         elif 18<=int(qiymat)<65:
#             narx=10000
#         elif int(qiymat)>=65:
#             narx=0
#         if narx==0:
#             print("Sizga kirish bepul.")
#         else:
#             print(f"Sizga kirish {narx} so'm.")
# print("Dastur tugadi")

# savol="Yoshingizni kiriting:\n"
# qiymat=''
# narx=0
# while True:
#     qiymat=(input(savol))
#     if qiymat=="exit" or qiymat=="quit":
#         break
#     else:
#         if int(qiymat)<7:
#             narx=2000
#         elif 7<=int(qiymat)<18:
#             narx=3000                     # break ko'rinish
#         elif 18<=int(qiymat)<65:
#             narx=10000
#         elif int(qiymat)>=65:
#             narx=0
#         if narx==0:
#             print("Sizga kirish bepul.")
#         else:
#             print(f"Sizga kirish {narx} so'm.")
# print("Dastur tugadi")

# savol="Yoshingizni kiriting:\n"
# qiymat=''
# narx=0
# ishora=True
# while ishora:
#     qiymat=(input(savol))
#     if qiymat=="exit" or qiymat=="quit":
#         ishora=False
#     else:
#         if int(qiymat)<7:
#             narx=2000
#         elif 7<=int(qiymat)<18:
#             narx=3000                     # ishora ko'rinish
#         elif 18<=int(qiymat)<65:
#             narx=10000
#         elif int(qiymat)>=65:
#             narx=0
#         if narx==0:
#             print("Sizga kirish bepul.")
#         else:
#             print(f"Sizga kirish {narx} so'm.")
# print("Dastur tugadi")

# 3-topshiriq
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat=''
while True:
    qiymat = input(savol)
    if (qiymat)=='exit':
        break      
    elif int(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Dastur tugadi")
