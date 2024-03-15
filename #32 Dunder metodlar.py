# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 22:44:34 2024

@author: Acer
"""

# 32-DARS DUNDER METODLAR
# Dunder metodlarini ko'rmoqchi bo'lsak dir(Klass_nomi) funksiyasi bilan ko'-
# rishimiz mumkin. Biz __init__ metodi bilan tanishdik. Bu metod klassdan
# obyekt yaratishda chaqiriladi va obyektning hususiyatlarini belgilaydi.
from uuid import uuid4
from Shaxs import Talaba,Manzil,Fan
class Avto:
    __num_avto=0
    def __init__(self,make,model,rang,yil,narx,km=0):
        self.make=make
        self.model=model
        self.rang=rang
        self.yil=yil
        self.narx=narx
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto+=1
    @classmethod
    
    
    def get_id(self):
        return self.__id
    def add_km(self,km):
        if km>0:
            self.__km+=km
        else:
            print("Mashina km kamaytirib bo'lmaydi.")
    def get_km(self):
        return self.__km
    def get_num_avto(cls):
        return cls.__num_avto
    def __repr__(self): # obyekt o'zini print qilganda __repr__ funksiya
        return f"{self.make}, {self.model}" # qaytargan natiga ekranga 
# chiqadi. Endi taqqoslash metodini yozamiz.
    def __eq__(self,obyekt): # tengmi funksiyasi
        return self.narx==obyekt.narx
    def __lt__(self,y): # kichikmi funksiyasi
        return self.narx<y.narx
    def __le__(self,y): # kichik yoki tengmi funksiyasi
        return self.narx<=y.narx
class Avtosalon:
    """Avtosalon classi"""
    def __init__(self,name):
        self.name=name
        self.avtolar=[]
    def __repr__(self):
        return f"{self.name} avtosaloni"
    def add_avto(self,*qiymat):# "*" belgisi xohlagancha qiymat berishi mumkin
        for avto in qiymat:
            if isinstance(avto,Avto): # isinstance funksiyasi te-
                self.avtolar.append(avto) # gishlimi degani ya'ni avto
# qiymati Avtosalon classiga tegishlimi degani.
            else:
                print("Avto kiriting:")
    def __getitem__(self,index): # get olish deb tarjima qilinadi
        return self.avtolar[index]
    def __setitem__(self,index,qiymat): # almashtirish deb tarjima qili-
    # nadi
        self.avtolar[index]=qiymat
    def __call__(self,*qiymat):
        if qiymat: # agar 1 dona bo'lsa ham qiymat bo'lsa
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar] # bu funksiya obyektni
# chaqirish uchun ishlatiladi.
    def __add__(self,boshqa_salon):
        if isinstance(boshqa_salon,Avtosalon):
            yangi_salon=Avtosalon(f"{self.name} {boshqa_salon.name}")
            yangi_salon.avtolar=self.avtolar+boshqa_salon.avtolar
            return yangi_salon
        elif isinstance(boshqa_salon,Avto): # Agar boshqa salon Avto klassiga
            self.add_avto(boshqa_salon) # tegishli bo'lsa salonga yangi avto-
# # mobil qo'sh.
# avto1=Avto("gm","captiva","qora","2021",20000,2000)
# print(avto1) # konsolga gm kaptiva chiqaradi chunki __repr__ funksiyasi
# # ishga tushadi
# avto2=Avto("gm","cobalt","oq",2022,13000,1000)
# print(avto1==avto2) # False qaytaradi teng bo'lmagani uchun
# avto3=Avto("gm","spark","oq",2019,8000,3000)
# salon1=Avtosalon("Chevrolet")
# salon2=Avtosalon("Avtolider")
# salon1.add_avto(avto1,avto2,avto3)
# salon1[0]=Avto("BMW",'x7',"qora",2020,70000)
# avto4=Avto("Mazda","6","Qizil",2015,35000)
# avto5=Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6=Avto("Honda","Accord","Oq",2017,42000)

# salon2(avto4,avto5,avto6) # salon2 ga avto4,avto5,avto6ni qo'shayapmiz.

# salon1+avto4   bu ifoda salonga yangi avtomobil qo'sh degani.

# TOPSHIRIQLAR.
# 1-topshiriq 
talaba_manzili=Manzil(34,"mustaqillik","qo'shrabot","samarqand")
talaba1=Talaba("Akbar", "Saidov", "AB6143604", 2000, "N1234545",talaba_manzili,
               "yaxshi")
talaba2=Talaba("Sayilboy", "Saidov", "AB1234567", 1995, uuid4(),talaba_manzili,
               "o'rta")
talaba3=Talaba("Ali", "Valiyev", "AB6143609", 2000, uuid4(),talaba_manzili,
               "yomonroq")
talaba4=Talaba("Vali","Aliyev","AB1234567",2001,uuid4(),talaba_manzili,"zo'r")
# 2-topshiriq 
fizika=Fan("Fizika")
fizika.add_student(talaba1,talaba2,talaba3)


