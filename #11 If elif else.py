# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:08:30 2024

@author: Acer
"""

# # 11-mavzu If elif else 
# # else vazifasi bir nechta shartlarni bajarishda ishlatiladi.
# yosh=int(input("sizning yoshingiz nechida?\n>>>"))
# if yosh==7:
#     print("Siz 1-sinfda o'qiysiz.")
# elif yosh==8: # 2-Shart kodi
#     print("Siz 2-sinfda o'qiysiz")
# elif yosh==9: # 3-shart kodi va hokazo shunday ketaveradi
#     print("Siz 3-sinfda o'qiysiz")
# elif yosh==10:
#     print("Siz 4-sinfda o'qiysiz")
# else:
#     if 19>yosh>10:
#         print("Siz katta sinfda o'qiysiz.")
#     else:
#         if yosh>=19:
#             print("Siz maktabni bitirgansiz")
# # har bir shart operatorga print deb yozmasdan qisqartirib yozish ham
# # mumkin. Misol
# yosh=int(input("Yoshingiz nechida?\n>>>"))
# if yosh<=4:
#     narx=0
# elif yosh<=12:
#     narx=5000
# elif yosh<=18:
#     narx=8000
# else:
#     narx=10000
# print(f"Sizga kirish {narx} so'm.")
# # Bizda bir nechta shartlarni tekshirish to'g'ri kelib qolishi mumkin.
# # Bular "or", va "and" operatorlaridan foydalanamiz.
# kun=(input("Bugun nima kun?\n>>>"))
# if kun.lower()=="shanba" or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni.")
# # "or" operatori- yoki degani bittasi to'g'ri bo'lsa ham shart bajariladi
# # "and" operatori- va degani ikkalasi ham to'g'ri bo'lishi kerak.
# # "()" yordamida bir nechta shartlarni ham bajarish mumkin.
# # misol (True or False) and True   | (True and Fase) or True va hokazo
# # Demak bu narsa boolean mantiqiy ma'lumotlar turi deyiladi.

# # endi boolean o'zgaruvchi yaratamiz.
# narx=15000
# choy=True # choy ham oldi
# salat=False # salat olmadi
# if choy and salat: # choy va salat olgan bo'lsa
#     print(narx+10000)
# elif choy or salat: # choy yoki salat olgan bo'lsa
#     print(narx+5000)
# # if elif else ning bir kamchilik tomoni birinchi shart bajarilsa qolgan
# # shartlarni tekshirib o'tirmaydi. bir nechta shartlarni bajarishga hara-
# # kat qilamiz. Misol
# narx=15000
# choy=True # choy ham oldi
# salat=False # salat olmadi
# non=True
# kompot=True
# assorti=False
# if choy:
#     print("Mijoz choy oldi.")
#     narx=narx+3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx=narx+5000
# if non:
#     print("Mijoz non oldi.")
#     narx=narx+2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narx=narx+5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narx=narx+15000
# print("Jami narx",narx,"so'm")
# # Bu yerda hamma shart tekshirilayapti
# # True False o'rniga 1, 0 raqamlarini qo'ysak ham dastur ishlayveradi

# # Endi "in" operatori bilan tanishamiz.
# menu=["osh","qazonkabob","shashlik","norin","somsa"]
# print("manti" in menu) # "in" degani ichida degani. ya'ni menu ichida
# # manti bormi degani. Natijada manti yo'q, False qiymat qaytaradi
# # "in"ning aksi "not in" operatori bor. U ro'yxatda yo'qligini tekshira-
# # di. Misol
# print("osh" not in menu) # menuda osh yo'qmi degani. Natija False
# # Ro'yxatlar bilan ishlaganimizda 2 ta ro'yxatni bir-biri bilan solish-
# # tirishimiz ham mumkin. Misol:
# buyurtmalar=["osh", "somsa","manti","shashlik"]
# for taom in buyurtmalar: # har bir buyurtma qilingan taom uchun
#     if taom in menu: # taom menu ichida bo'lsa
#         print(f"Menuda {taom} bor")
#     else: # aks holda
#        print("Kechirasiz menuda",taom,"yo'q")
        
# # Bazida buyurtmalarni foydalanuvchi shakllantirishi mumkin. U holda
# # kodlash quyidagicha bo'ladi.
# menu=["osh","qazonkabob","shashlik","norin","somsa"]
# buyurtmalar=[]
# if buyurtmalar:
#     print(f"Sizda {len(buyurtmalar)} ta taom bor")
# else: 
#      print("Sizda buyurtmalar yo'q!")
#      buyurtma=input("Buyurtma berasizmi?\n>>>")
#      if buyurtma.lower()=="ha":
#          buyurtma_soni=int(input("Nechta\n>>>"))
#          for zakaz in range(buyurtma_soni):
#              buyurtmalar.append(input(f"{zakaz+1}-chi buyurtma:"))
#      elif buyurtma.lower()=="yo'q":
#          print("So'g' bo'ling")
#      else:
#          print("Noto'g'ri belgi kiritildi")
#      for taom in buyurtmalar: # har bir buyurtma qilingan taom uchun
#          if taom in menu: # taom menu ichida bo'lsa
#              print(f"Menuda {taom} bor")
#          else: # aks holda
#              print("Kechirasiz menuda",taom,"yo'q")      

# #        TOPSHIRIQLAR
# # 1-topshiriq. foydalanuvchidan juft son so'rash
# juft_son=int(input("Juft son kiriting:\n>>>"))
# if juft_son%2==0:
#     print("Raxmat!")
# else:
#     print("Bu son juft emas.")
    
# # 2-topshiriq. chipta narxini yoshga qarab belgilash
# yosh=int(input("Yoshingizni kiriting:"))
# if yosh<4 or yosh>60:
#     print("Sizga kirish bepul.")
# elif yosh<18:
#     print("Sizga kirish 10 000 so'm.")
# elif yosh>=18:
#     print("Sizga kirish 20 000 so'm")

# # 3-topshiriq 2 ta sonning tengligi katta va kichikligini chiqarish
# print("2 ta son kiriting.")
# son1=int(input("1-son\n>>>"))
# son2=int(input("2-son\n>>>"))
# if son1>son2:
#     print("Birinchi son ikkinchi sondan katta.")
# elif son1==son2:
#     print("Birinchi son ikkinchi son bilan teng.")
# else:
#     print("Birinchi son ikkinchi sondan kichik.")

# # 4-topshiriq Mahsulotlarni solishtirish
# mahsulotlar=["un","yog'","go'sht","tuxum","piyoz","sabzi","non","pomidor","bodring","sut"]
# savat=[]
# print("5 ta mahsulot kiriting:")
# for mahsulot in range(5): # 5 marta takrorlanadi
#     savat.append(input(f"{mahsulot+1}-mahsulot\n>>>"))
# for produxta in savat: # savat ichidagi produxta
#     if produxta in mahsulotlar: # mahsulotlar ichida produxta bormi
#         print(f"{produxta} do'konimizda bor.")
#     else:
#         print(f"{produxta} do'konimizda yo'q.")

# 5-topshiriq
mahsulotlar=["un","yog'","go'sht","tuxum","piyoz","sabzi","non","pomidor","bodring","sut"]
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
print("5 ta mahsulot kiriting:")
for mahsulot in range(5): # 5 marta takrorlanadi
    savat.append(input(f"{mahsulot+1}-mahsulot\n>>>"))
for produxta in savat: # savat ichidagi produxta
    if produxta in mahsulotlar: # mahsulotlar ichida produxta bormi
        bor_mahsulotlar.append(produxta)
    else:
        mavjud_emas.append(produxta) 
if len(mavjud_emas)==0: 
    print("Siz so'ragan barcha mahsulotlar bor.")
else:
    print("Quyidagi mahsulotlar mavjud emas:",mavjud_emas)
    # if mavjud_emas:  kodi agar ro'yxatda element bo'lsa degani

# 5-topshiriqning yana boshqcha bir ko'rinish
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6-topshiriq login
foydalanuvchilar=["akbar","jahon","akmal","shaxzod","anvar"]
ism=input("Login kiriting:")
if ism.lower() in foydalanuvchilar:
    print("Login band. Boshqa login kiriting")
else:
    print("Xush kelibsiz")

# 7-topshiriq
son=int(input("Son kiriting: "))
for son1 in range(2,11):
    if son%son1==0: # if not son%son1: deb ham yozish mumkin ekan
        print(f'{son} raqami {son1} ga qoldiqsiz bo\'linadi')
        
    

       


    








