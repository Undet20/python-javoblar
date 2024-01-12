# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 20:58:45 2023

@author: Acer
"""

# 09-mavzu For takrorlash sikli
mehmonlar=["Ali","Vali","Hasan","Husan","Olim"]
for mehmon in mehmonlar: # for degani uchun, in degani ichida, ya'ni meh-
    print("Salom",mehmon) # monlar ichidagi har bir mehmon uchun sikl ta-
# nasi ichidagi amaliyotni bajar degani.
# for sikl yordamida ro'yxatni shakllantirish
sonlar=list(range(1,11))
sonlar_kvadrati=[]
for son in sonlar:
    sonlar_kvadrati.append(son**2)
    print(son,"ning kvadrati",sonlar_kvadrati[son-1],"ga teng")
print("5 ta eng yaqin do'stingiz kim?")
dostlar=[]
for dost in range(5):
    dostlar.append(input(f"{dost+1}-chi do'stingizni kiriting:\n>>>"))
for dost in dostlar:
    print(f"Sizning {dostlar.index(dost)+1}-do'stingiz {dost}")
# bu yerda index() metodi yordamida qaysi element qaysi indeksda joylash-
# ganini aniqlab olamiz.

# TOPSHIRIQLAR
# 1-topshiriq
ismlar=["Shavkat","Jahon","Azim","Laziz","Ibrohim"]
for ism in ismlar:
    print(f"Salom {ism} ishlaring yaxshimi?")
# 2-topshiriq
print("Kod",len(ismlar),"marta takrorlandi.")
# 3-topshiriq
toq_sonlar=list(range(11,101,2))
print("Toq sonlar:",toq_sonlar)
for toq_s in toq_sonlar:
    print(toq_s,'ning kubi',toq_s**3,"ga teng")
# 4-topshiriq
print("5 ta eng sevimli kinolaringizni kiriting:")
kinolar=[]
for kino in range(5):
    kinolar.append(input(f"{kino+1}-chi kinoyingiz:\n>>>"))
for kino in kinolar:
    print(f"Sizning {kinolar.index(kino)+1}-sevimli kinoyingiz: {kino}")
# 5-topshiriq
odam_soni=input("Siz nechta odam bilan uchrashdingiz:\n>>>")
odamlar=[]
for odam in range(int(odam_soni)):
    odamlar.append(input(f"{odam+1}-chi odam:\n>>"))
for odam in odamlar:
    print(f"Siz {odamlar.index(odam)+1}-chi {odam.title()} degan kishi bilam uchrashdingiz.")
    


