# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:19:44 2024

@author: Acer
"""

# 30-DARS VORISLIK VA POLIMORFIZM

# Bir class yaratamiz
class Shaxs:
    def __init__(self,ism,familiya,pasport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.pasport=pasport
        self.tyil=tyil
    def get_info(self):
        return (f"Ismi:{self.ism} Familiyasi:{self.familiya} Pasporti:"
                f"{self.pasport} Tug'ilgan yili:{self.tyil}")
    def get_age(self,yil):
        return yil-self.tyil
    
# Endi mana shu classdan yangi class yaratamiz. 
class Talaba(Shaxs): # Endi bu yerda shaxs classi super class deyiladi.
# Talaba esa voris class deb ataladi
    def __init__(self,ism,familiya,pasport,tyil,id_raqam,manzil):
        super().__init__(ism,familiya,pasport,tyil) # ism,familiya pas-
        self.id_raqam=id_raqam # port,tyil super classimizdan meros bo'-
        self.bosqich=1 # lib o'tayapti. Yana qo'shimchasiga 2 ta id_ra-
        self.manzil=manzil # qam va bosqich xususiyatlarni qo'shdik
        self.fanlar=[]
    def get_id(self):
        return self.id_raqam
    def get_bosqich(self):
        return self.bosqich
    # Ana endi polimorfizmga o'tamiz
    def get_info(self):
        """Talaba id raqamini qaytaradi"""
        info=f"{self.familiya} {self.ism} {self.tyil}-yilda tug'ilgan. "
        info+=f"Pasporti {self.pasport}. {self.bosqich}-bosqich talabasi. "
        info+=f"Talaba IDsi {self.id_raqam}"# voris classdagi ma'lumot-
        return info # ga qoniqmasak uni qaytadan to'ldirib yozamiz. Bu
# narsa polimorfizm deyiladi.
    def fanga_yozil(self,obyektlar):
        self.fanlar.append(obyektlar)
    def chiqarish(self):
        return [obyekt.fan_nomi for obyekt in self.fanlar] 
    def remove_fan(self,obyekt_matni): # matn kiritishi kerak
        if obyekt_matni.lower() in self.chiqarish(): # bu yerda obyekt tarkibi-
            for matn in self.chiqarish(): # ni yozsak ham oxirida ish-
                if matn==obyekt_matni.lower(): # layverar ekan.
                    matn=self.chiqarish().index(obyekt_matni.lower())
                    del self.fanlar[matn]
        else:
            return ("Kechirasiz siz bu fanga kiritilmagansiz")
# Endi obyekt yaratamiz
# talaba1=Talaba("Akbar","Saidov","AB6143604",2000,"N2233445")
# Super classimizdagi metodlar voris classga o'tadi misol
# talaba1.get_age(2024) # Birinchi super class yaratiladi keyin voris class
# yaratiladi shu ketmaketlikkA amal qilish kerak aks holda bunday class
# yo'q deb hatolik beradi. Bu vorislik edi.

# Ba'zida hususiyatlar ko'payib ketishi mumkin. Obyekt to'g'ri ishlashiga
# yoki obyektga murojat qilish qiyinlashib ketishi mumkin. Bunday holat-
# da obyekt hususiyatini boshqa obyektga o'tkazishimiz ham mumkin.
class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat
    def get_mazil(self):
        manzil=f"{self.viloyat.title()} viloyati {self.tuman.capitalize()} "
        manzil+=f"tumani {self.kocha.capitalize()} ko'chasi {self.uy}-uy"
        return manzil
talaba_manzili=Manzil(34,"mustaqillik","qo'shrabot","samarqand")

talaba1=Talaba("Akbar", "Saidov", "AB6143604", 2000, "N1234545",talaba_manzili)

print(talaba1.manzil)

print(talaba1.manzil.get_mazil())
    
# TOPSHIRIQLAR
class Fan:
    def __init__(self,fan_nomi):
        self.fan_nomi=fan_nomi # keyin klass yaratilayapti
    def get_fan(self):
        return self.fan_nomi
fan1=Fan("matematika")
fan2=Fan("informatika")
student1=Talaba("Akbar","Saidov","AB6143604",2000,"N12345678",talaba_manzili)
student1.fanga_yozil(fan1)
student1.fanga_yozil(fan2)

print(student1.remove_fan("matematika")) # kod to'g'ri kelib ishlayapti
print(student1.chiqarish())    
        






    