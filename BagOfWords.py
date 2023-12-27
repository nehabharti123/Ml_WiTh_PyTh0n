# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:17:44 2023

@author: KIIT
"""


import nltk


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

# cleaning the texts
# re is for regular expression
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

# Initialize the stemmer and lemmatizer
ps = PorterStemmer()
wordnet = WordNetLemmatizer()

# Assuming you have defined 'paragraph' earlier
sentences = nltk.sent_tokenize(paragraph)
corpus = []

for i in range(len(sentences)):
    review = re.sub('[^a-zA-Z]', ' ', sentences[i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the bag of words model
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
