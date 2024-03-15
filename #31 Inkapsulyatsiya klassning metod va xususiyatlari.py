# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 19:08:39 2024

@author: Acer
"""

# 31-DARS INKAPSULYATSIYA KLASSNING METOD VA HUSUSIYATLARI
from avto import Avto # agar (*) belgisi qo'yilsa barcha klasslarni cha-
# qiradi. 
avto1=Avto("GM","Malibu","qora",2019,20000,1000)
avto2=Avto("GM","Lasetti","oq",2021,15000,1000)

avto2.get_km()

# TOPSHIRIQLAR
class Shaxs:
    __odamlar_soni=0 # bu classga o'ziga hos hususiyat.
    def __init__(self,ism,familiya,pasport,tyil): # init ichidagi hususiyatlar
        self.ism=ism # faqat obyektga tegishli bo'ladi.
        self.familiya=familiya
        self.pasport=pasport
        self.tyil=tyil
        Shaxs.__odamlar_soni+=1
    @classmethod # bu class dekeratori. Klassning o'ziga hos bo'lgan hususi-
    def get_info(self): # yati.
        return (f"Ismi:{self.ism} Familiyasi:{self.familiya} Pasporti:"
                f"{self.pasport} Tug'ilgan yili:{self.tyil}")
    def get_age(self,yil): # bu funksiyaga self deb obyektni uzatayapmiz
        return yil-self.tyil
    def get_num_shaxs(cls): # bu funksiyaga cls deb classni uzatayapmiz.
        return cls.__odamlar_soni
# Endi mana shu classdan yangi class yaratamiz. 
class Talaba(Shaxs): # Endi bu yerda shaxs classi super class deyiladi.
# Talaba esa voris class deb ataladi
    __talabalar_soni=0
    def __init__(self,ism,familiya,pasport,tyil,id_raqam,manzil,harakter):
        super().__init__(ism,familiya,pasport,tyil) # ism,familiya pas-
        self.id_raqam=id_raqam # port,tyil super classimizdan meros bo'-
        self.bosqich=1 # lib o'tayapti. Yana qo'shimchasiga 2 ta id_ra-
        self.manzil=manzil # qam va bosqich xususiyatlarni qo'shdik
        self.fanlar=[]
        self.__harakter=harakter
        Talaba.__talabalar_soni+=1
    @classmethod
    def get_id(self):
        return self.id_raqam
    def get_bosqich(self):
        return self.bosqich
    def get_harakter(self):
        return self.__harakter
    def harakter_uzgartir(self):
        sifat=input("Sizga nima yoqadi?\n (musiqa),(jimjitlik)")
        if sifat.lower()=="musiqa":
            print("Harakteringiz sho'x ekan.")
            self.__harakter="sho'x"
        elif sifat.lower()=="jimjitlik":
            print("Harakteringiz og'ir ekan.")
            self.__harakter="og'ir"
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
    def get_num_talaba(cls):
        return cls.__talabalar_soni
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

talaba1=Talaba("Akbar", "Saidov", "AB6143604", 2000, "N1234545",talaba_manzili,"og'ir")

print(talaba1.manzil)

print(talaba1.manzil.get_mazil())
class Fan:
    def __init__(self,fan_nomi):
        self.fan_nomi=fan_nomi # keyin klass yaratilayapti
    def get_fan(self):
        return self.fan_nomi
fan1=Fan("matematika")
fan2=Fan("informatika")
student1=Talaba("Akbar","Saidov","AB6143604",2000,"N12345678",talaba_manzili,"og'ir")
student1.fanga_yozil(fan1)
student1.fanga_yozil(fan2)

print(student1.remove_fan("matematika")) # kod to'g'ri kelib ishlayapti
print(student1.chiqarish())  





















