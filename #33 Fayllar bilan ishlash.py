# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 07:42:49 2024

@author: Acer
"""

# 33-DARS FAYLLAR BILAN ISHLASH

# son=1
# file=open("pi.txt") # bu ko'rinishda faylni ochish tavsiya qilinmaydi. Faylni
# # ochishga ochamiz lekin fayl yopilmay qolib ketishi mumkin. bunday holatda fa-
# # ylimizga shikast yetishi mumkin.
# PI=file.read()
# print(PI)
# file.close()

# Buning yana bir yaxshi usuli with operatori 
with open("pi.txt") as file: # bu faylni faqat o'qish uchun ochamiz u faylga
# yoza olmaymiz.
    pi=file.read() # bu blokdan chiqqandan keyin fayl avtomatik yopiladi.

# print(pi)

# pi=pi.rstrip()
# pi=pi.replace("\n", "") # \n belgisini "" belgiga almashtiradi ya'ni keyingi
# # qator belgisini topib uni hech narsaga almashtiradi. Shu bilan qator tashlash
# # belgisi yo'q bo'ladi.
# pi=float(pi)
# print(pi)

# # Endi har bir qatorni alohida o'zgaruvchiga saqlashni ko'ramiz.
# filename="data.txt"

# # with open(filename) as file:
# #     for line in file:
# #         print(line)

# with open(filename) as file:
#     talabalar=file.readlines()
    
# print(talabalar)
# talabalar=[talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# Endi yangi faylga matn yozishni o'rganamiz.
fayl_nomi="new_file.txt"
ism="Olimjon Hasanov"
tyil=2004
# with open(fayl_nomi,"w") as  fayl: # w degani write ya'ni yozish degan ma'no-
# # ni bildiradi. Endi ehtiyot bo'lishimiz kerak faylni ochayotganimizda yozmoq-
# # chi bo'lgan faylimiz oldindan mavjud bo'lsa uning ichidagi o'chib ketib us-
# # tidan yangi faylni yozib yuboradi.
#     fayl.write(ism) # buning bir kamchiligi hamma o'zgaruvchi faylga birinchi
#     fayl.write(str(tyil)) # qator oxiridan qo'shib yoziladi.
    
# Buning oldini olish uchun quyidagicha kod yozamiz.
with open(fayl_nomi,"w") as  fayl:
    fayl.write(ism+'\n') # o'zgaruvchigaga yangi qatorga o'tkazish belgisini 
    fayl.write(str(tyil)+'\n') # qo'shamiz.
    
# Endi mavjud faylimizga yangi ma'lumot qo'shamiz.
with open(fayl_nomi,"a") as fayl: # a degani append ya'ni qo'shish degani.
    fayl.write("Alijon Valiyev\n") # Agar fayl mavjud bo'lmasa yangi fayl ochib
    fayl.write("2000\n") # Yozib ketaveradi.

# Endi biz har xil o'zgaruvchilar bilan obyektlar bilan ishlaymiz ularni faqat
# matn ko'rinishda saqlay olmaymiz u holda nima qilamiz?
# Buning uchun mahsus modul bor bu pickle deb ataladi. Buning tarjimasi tuzlan-
# gan bodring degani kelib chiqadigan ma'nosi konservalash degani.
# Pickle asosan o'zgaruvchilarni obyektlarni 2lik sanoq sistemasiga o'tkazadi.
# Uni faqat pythonda ochish mumkin. C++ yoki boshqa muharrirlarda ochib bo'l-
# maydi.
import pickle
talaba1={'ism':'hasan','familiya':'husanov','tyil':2003,'kurs':2}
talaba2={'ism':'alijon','familiya':'valiyev','tyil':2004,'kurs':1}
with open("info.pickle","wb") as file:
    pickle.dump(talaba1,file) # o'zgaruvchilar pickle faylda "talaba1,talaba2"
    pickle.dump(talaba2,file) # ketmaketlikda yoziladi.

# Ana endi pickle faylni ochishni ko'ramiz.
with open("info.pickle","rb") as file: # rb degani read biany-o'qimoq degani.
    student1=pickle.load(file) # bunday ko'rinish tavsiya qilinmaydi. Har bir
    student2=pickle.load(file) # O'zgaruvchi uchun alohida fayl yaratiladi.
# print(student1)
# print(student2)

# TOPSHIRIQLAR 

# 1. pi_million_digits.txt faylini yuklab olib shu fayl ichidan tug'ilgan kuni,
# oyi va yilini topish.
with open("pi_million_digits.txt") as file:
    dat=file.read()
def son_top(sonlar):
    if dat.count(sonlar): # count metodi ma'lumot nechta borligini aniqlaydi
#   if sonlar in dat:   # dat sonlar ichida sonlar degan o'zgaruvchining soni
# bormi degani kodni shunday yozishimiz mumin.
        return sonlar
    else:
        return "Bunday son yo'q!"
print(son_top("06092000"))

# 2. float turiga o'tkazib uni pickle yordamida yangi faylga saqlaymiz.
dat=dat.rstrip()
dat=dat.replace("\n", "")
dat=dat.replace(" ","")
dat=float(dat)

with open("dat.pickle","wb") as file:
    pickle.dump(dat,file)

# 3. Foydalanuvchidan ma'lumotni olib faylga saqlash.
ishora=True
while ishora:
    javob=input("Ma'lumot kiritasizmi? (ha/yo'q)\n>>>")
    if javob=="ha":
        axborot=input("Ma'lumot kiriting:\n>>>")
        with open("user_data.txt","a") as file:
            file.write(axborot+"\n")
    else:
        print("Kiritgan ma'lumotlaringiz faylga saqlandi.")
        ishora=False
    




 




