# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:44:16 2024

@author: Acer
"""

# 39-DARS PYTHON TASHQI KUTUBXONASI
# from googletrans import Translator
# tarjimon=Translator()
# msg="Tarjima uchun so'z kiriting:\n>>>"
# while True:
#     text=input(msg)
#     if text=="q":
#         break
#     else:
#         tarjima=tarjimon.translate(text, src='uz', dest='en')
#         print(tarjima.text)

import googletrans    
import requests # Eng yaxshi modullardan biri requests moduli bu mo-
# gul orqali web sahifalarni chaqirib olishimiz mumkin.

# from pprint import pprint
# sahifa="https://kun.uz/news/main"
# r=requests.get(sahifa)
# pprint(r.text)

url="https://api.adviceslip.com/advice"
r=requests.get(url)
advice=r.json()['slip']['advice']
print(advice)

translator=googletrans.Translator()
tarjima=translator.translate(advice, dest='uz')
print(tarjima.text)











