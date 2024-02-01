# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:56:28 2024

@author: Acer
"""

# 23-DARS MODULLAR.
# Bugun dasturimizni modullarga bo'lishni o'rganamiz. Ya'ni modullarga
# bo'lishdan maqsad kodimizni yana ham tozalash. Ana endi yaratgan funk-
# siyalarimizni Modul ichiga yashirib qo'yishimiz ham mumkin. Modul de-
# gani bu alohida fayl ya'ni dasturlarimiz bitta fayldan iborat bo'lmay-
# di. Kelajakda yozadigan dasturimiz juda katta bo'ladi. Shu dasturlarni
# tahlil qilishimizda kerakli narsalarni bitta fayldan topish juda qiyin
# bo'lib ketadi. Shuning uchun fayllarga bo'lib yozish. Bunday qilishi-
# mizga sabab ortiqcha kodlar bo'lmaydi. Dasturimizda o'zimizga muhim
# bo'lgan qismlari ko'rinib turadi. Qolgan funksiya ichidagi uzun kod-
# larni alohida faylga yashirib qo'yamiz. Odatda katta dasturlar bir
# nechta modullardan iborat bo'lishi tabiiy. Uning bir qulayligi boshqa
# bir dasturlarda ham o'sha modullardan qayta-qayta foydalanishimiz
# mumkin.
# import kalit so'zi chaqirish,ko'chirib olish degani
# Asosiy fayl bilan modulimiz bitta papkada bo'lishi kerak.
# import avto_info_mod # bunday ko'rinishda bo'lishligi uchun. Bitta pap-
# kada bo'lmasa fayl manzili ko'rsatiladi.

# avto1=avto_info_mod.avto_info("Gm", "Malibu", "qora", "avtomat", 2019)
# # demak biz avto_info() funksiyasini chaqirish uchun avto_info_mod mo-
# # dulidan foydalanar ekanmiz aks holda funksiya mavjud emas deb xatolik
# # beradi. Endi keyingi ma'lumotni chiqaramiz.
# avto_info_mod.avto_malumot()
# # Bu birinchi usul edi.

# # Bizga modul uzunlik qilayapti unda nima kilish kerak? Buning oldini
# # olish uchun
# import avto_info_mod as aim
# aim.avto_malumot() # bu 2-usul.

# # Deylik biz funksiya oldidadi modul nomini ham yozmasdan to'g'ridan
# # to'g'ri funksiyaning nomini yozishimiz mumkin. Buning uchun eng qulay
# # usuli from usuli hisoblanadi. from ingliz tilidan (dan) deb tarjima
# # qilinadi. Misol
# from avto_info_mod import avto_info,avto_malumot # Bu degani
# # avto_info_moddan avto_info,avto_malumot,avto_ruyxatni import qilib ol
# # degani.misol
# avto_info("Daewoo", "Matiz", "Oq", "mehanika", 2008) # buning qulaylik
# avto_malumot() # tomoni modulni qayta-qayta yozishimiz shart emas.

# # Misol uchun funksiyaning nomi bizga uzunlik qilayapti yoki modulning
# # funksiyasi o'zimizda ham bor nomi bir xil bo'lsa funksiya nomini o'z-
# # gartirishimiz mumkin.Misol
# from avto_info_mod import avto_info as ainfo,avto_malumot as adata
# mashina=ainfo("Gm", "Spark", "qora", "mehanika", 2016)
# adata()

# from avto_info_mod import *   (*) belgisi modul ichidagi barcha funk-
# siyalarni chaqiradi. Bu usul tavsiya berilmaydi. Chunki juda katta mo-
# dulda funksiya va o'zgaruvchilarimiz qorishib ketadi. Keyin dasturimiz
# xato ishlashni boshlaydi. 2 ta 3 ta funksiyali modulga ishlatsa bo'ladi.

# import math
# x=400
# print(math.sqrt(x))
# print(math.pow(5,3))

# RANDOM MODULI
# Eng yaxshi modullardan biri ranmom moduli u orqali tasodifiy sonlarni
# chiqarishimiz mumkin. Misol
import random as r

# son=r.randint(0,100)

# # choise() funksiyasi ro'yxatlar ichidan istalgan ro'yxatni tasodifan
# # tanlab beradi. MISOL
# ismlar=["olim","anvar","hasan","husan"]
# ism=r.choice(ismlar)
# print(ism) # bu yerda bo'sh ro'yxat bersak dastur xato beradi.
# print(r.choice(ism)) # ismning harflarini tasodifan chiqaradi.
# x=list(range(0,51,5))
# print(r.choice(x))

# bizlarga yana eng foydali funksiyalardan biri shuffle() funksiyasi
# ingliz tilidan aralashtirib tashlash degan ma'noni anglatadi.
x=list(range(11))
print(x)
r.shuffle(x)
print(x)























