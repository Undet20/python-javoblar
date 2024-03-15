# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:25:41 2024

@author: Acer
"""

# Shaxs modul
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
    def __repr__(self): # obyekt o'zini chaqirganda ishga tushadigan funksiya
        return f"{self.familiya} {self.ism}" # ism familiyani qaytaradi
    def __lt__(self,boshqa_obyekt):
        """Kichiklikni tekshiruvchi funksiya"""
        if self.tyil<boshqa_obyekt.tyil:
            return f"{self} {boshqa_obyekt}dan katta"
        else:
            return f"{self} {boshqa_obyekt}dan kichik"
    def __eq__(self,boshqa_obyekt):
        return self.tyil==boshqa_obyekt.tyil
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
class Fan:
    __fandagi_talabalar=0
    def __init__(self,fan_nomi,talabalar_ruyxati=[]):
        self.fan_nomi=fan_nomi
        self.talabalar_ruyxati=talabalar_ruyxati
    def add_student(self,*talabalar):
        for talaba in talabalar:
            if isinstance(talaba,Talaba):
                self.talabalar_ruyxati.append(talaba)
            else:
                print("Faqat talaba kiriting:")
    def __getitem__(self,index):
        return self.talabalar_ruyxati[index]
# fizika[1]
    def __setitem__(self,index,talaba):
        if isinstance(talaba,Talaba):
            self.talabalar_ruyxati[index]=talaba
# fizika[1]=talaba4
    def __len__(self):
        return len(self.talabalar_ruyxati)
# len(fizika)
    def __add__(self,boshqa_obyekt):
        if isinstance(boshqa_obyekt,Talaba):
            self.talabalar_ruyxati.append(boshqa_obyekt)
# fizika+talaba4
    def __sub__(self,pasport):
        for talaba in self.talabalar_ruyxati:
            if talaba.pasport==pasport:
                self.talabalar_ruyxati.remove(talaba)
# fizika-"AB6143604"
    def __call__(self,talaba):
        if isinstance(talaba,Talaba):
            for student in self.talabalar_ruyxati:
                if student==talaba:
                    return student
# fizika(talaba1) 







