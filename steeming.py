# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 14:18:27 2023

@author: KIIT

"""
import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """ung may puting bulbul na ko.. hahaha lolo https://t.co/CP6phmG2aS
Work promptly, Odisha knows you can 🔥
ବାତ୍ୟା ବୁଲ୍‌ବୁଲ୍‌ର କ'ଣ ରହିଛି ସ୍ଥିତି? ଏହା କେଉଁ ଆଡ଼କୁ ମୁହାଁଉଛି? ଏହାର ବେଗ ଘଣ୍ଟାପ୍ରତି କେତେ ରହିଛି? କେଉଁ କେଉଁ ଜିଲ୍ଲାରେ ଅ… https://t.co/35dopROK5j
RT @ndmaindia: #CycloneBulbul: Very Severe Cyclonic Storm ‘Bulbul’  over west-central &amp; adjoining east-central Bay of Bengal continued to m…
@srinu0072 I thought it was trademarked by bulbul balayya
RT @heritagewalkcal: Stay in, stay safe!

#cyclonebulbul #bulbul https://t.co/bjUBDJI94l
RT @Indiametdept: Hourly update based on 1100 IST of 9th November

THE VERY SEVERE CYCLONIC STORM ‘BULBUL’ LAY CENTRED AT 1030 HRS IST OF T…
Ayodhya Verdict end, Bulbul cyclone start... God save us @AnilSinghvi_ https://t.co/vp5jLZ263o
RT @SpBhadrak: Officers and staff Dhusari PS clearing road. #Bulbul https://t.co/iAByrRYWTq
The very severe cyclonic storm 'Bulbul' over the Bay of Bengal is likely to make landfall between West Bengal-Bangl… https://t.co/boUCvVcr2Z
RT @EconomicTimes: Cyclone 'Bulbul': Expected landfall on Nov 9, coastal districts on alert, says Odisha SRC https://t.co/tjiZ754Vg0 https:…
RT @CesuOdisha: Due to very severe cyclonic storm Bulbul power supply infra in the coastal divisions of Paradeep, Kendrapara ,Marshaghai ,…
RT @OdishaReporter: ଭଦ୍ରକରେ ବୁଲ୍‌ବୁଲ୍‌ ତାଣ୍ଡବ; ଲାଗି ରହିଛି ବର୍ଷା, ପବନ #Odisha"""

sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word)for word in words if word not in set(stopwords.words('spanish'))]
    sentences[i] = ' '.join(words)