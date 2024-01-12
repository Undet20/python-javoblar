# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 07:31:14 2023

@author: Acer
"""
# 07-mavzu Lists (Ro'yxatlar)
mevalar=['olma','o\'rik','shaftoli'] # Matnli ro'yxat
narxlar=[10000,15000,20000] # Sonli ro'yxat
sonlar=["bir",'ikki',3,4,5] # Aralash ro'yxat
ismlar=[] # bo`mbo`sh ro`yxat
print(mevalar[-1]) # shaftoli
# mevalar[-1] degani eng ohirgi element degani -2 esa eng oxirgi ele-
# mentdan bitta oldingi element degani
# Indeks elementlarini string metodlarini ham qo`llash mumkin
# Misol
print(mevalar[0].upper()) # OLMA
# Ro`yxat sonlar o'rtasida turli arifmetik amallar ham bajarishimiz mum-
# kin. Misol
print(narxlar[0]+narxlar[1]) # 25000
# Ro'yxat elementlarini o`zgartirish
mevalar[0]='anor' # olma element anorga o'zgartiriladi
mevalar[-1]='uzum' # Shaftoli element uzumga o`zgaradi
# append() metodi bu ro`yxatga yangi element qo'shadi
# Misol
mevalar.append('tarvuz')
# insert() metodi-agarda elementni boshiga o'rtasiga yoki oxiriga yangi
# element qo'shish kerak bo`lsa insert() metodidan foydalanamiz.
# Misol
mevalar.insert(0,'banan')
mevalar.insert(2,"ananas") # endi uchinchi indeksda ananas qo'shildi
# DIQQAT!
# Ro'yxat yaratilayotganda oxiriga ko'plik qo'shimchasini qo'shish ke-
# rak. Keyinchalik ro'yxat ekanligini bilib turishimiz uchun.
cars=[]
cars.append("Lacetti")
cars.append("Cobalt")
cars.append("Malibu")
cars.append("Tracker")
print(cars)
# Agarda shu ro'yxat ichidan biror bir elementini o'chirmoqchi bo'lsak
# del operatorini ishlatamiz. Misol
del cars[0] # 0-indeksdagi element o'chiriladi
print(cars)
# Biz ro'yxat ichidagi element nomini bilamiz-u lekin qaysi indeksda
# joylashishini bilmasak remove metodidan foydalanamiz.
# Misol
cars.remove("Malibu")
print(cars) # agar ro'yxatda bir nechta bir xil element bo'lganda remo-
# ve metodi faqat birinchi uchragan elementni o'chiradi.
# Misol
hayvonlar=["it",'mushuk','sigir','qo\'y','quyon','mushuk']
print(hayvonlar)
hayvonlar.remove('mushuk')
print(hayvonlar)
# Agar hamma bir xil elementni o'chirish kerak bo'lsa u metodni qayta-
# qayta takrorlash kerak.
# Ro'yxat ichidan elementni sug'urib olish
# Misol
bozorlik=["yog'","un","piyoz","banan",'g\'sht']
print(bozorlik)
mahsulot=bozorlik.pop(1) # birinchi indeksdan o'chirib mahsulot degan
# o'zgaruvchiga yuklaydi.
print(bozorlik)
print(mahsulot)
# Agar pop metodiga hech qanday indeks berilmasa ro'yxatning oxirgi
# elementini sug'urib oladi.
# Misol
mahsulot2=bozorlik.pop() # Oxirgi elementni sug'urib oladi
print(mahsulot2) # Sug'urib olgan oxirgi element go'sht
print(bozorlik) # ["yog'", 'piyoz', 'banan']
# Ro'yxatlar ustida amallar
print(narxlar) # Eski narxlarni chiqaradi
narxlar[0]=narxlar[0]+2000 # 10000 qiymati 2000 ga oshadi
print(narxlar) # [12000, 15000, 20000]
# AMALIYOT
ismlar=['Shavkat',"Jahongir","Akbar"]
print(f"Salom {ismlar[0]}, qandaysan")
print(ismlar[1],"ertaga o'tirishga borasanmi?")
print(f"Kompyuterni tezroq o'rgan {ismlar[2]}")
# o'rtasiga element qo'shish uslub
# len(lists) ro'yxat elementlar sonini aniqlash metodi
print("6 ta mevalar:",mevalar)
mevalar.insert((len(mevalar)//2),"Olcha")
print("7 ta mevalar:",mevalar)
# bu yerda len metodi yordamida ro'yxatlar sonini aniqlab o'sha sonni
# 2 ga bo'lamiz. chiqqan natijasi teng o'rtasining indeksini beradi
# insert metodi bilan o'rtasiga element qo'shamiz.

# 8-topshiriq
friends=["Shavkat","Jahon","Dilmurid","Sahzod","Javohir"]
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(1))
print("Kelgan mehmonlar:",mehmonlar)
print("Kelolmagan mehmonlar:",friends)





