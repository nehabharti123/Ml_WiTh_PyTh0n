# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 00:49:07 2023

@author: KIIT
"""

import nltk

from gensim.models import Word2Vec
from nltk.corpus import stopwords

import re

paragraph = """RT @JavedMahar7: Sindh Wildlife dept: Sukkur team, headed by Adnan Khan recovered around 1800 trapped from wild; common myna, common sparro…
RT @newhumanitarian: A view of Tropical Cyclone Bulbul approaching Bangladesh and India's West Bengal. Authorities in both countries have b…
RT @cnnbrk: About 500,000 people have been evacuated from Bangladesh's coastal region, as the nation waits for Cyclone Bulbul to hit, an of…
RT @cnni: Around 500,000 people have been evacuated from Bangladesh's coastal region, as the nation waits for Cyclone Bulbul to hit, the co…
RT @cnnbrk: About 500,000 people have been evacuated from Bangladesh's coastal region, as the nation waits for Cyclone Bulbul to hit, an of…
RT @ANI: India Meteorological Department (IMD): Cyclone #BulBul is likely to weaken gradually &amp; move Northwards and cross West Bengal-Bangl…
RT @Indiametdept: The VSCS ‘Bulbul’ at 2030 hrs IST near 21.4°N &amp; 88.3°E about 40km ESE of Sagar Islands. The land fall process has started…
RT @vishwamTOI: IMD’s update: The very severe cyclonic storm #Bulbul to cross West Bengal - Bangladesh Coasts between Sagar Islands (West B…
RT @ANI: India Meteorological Department (IMD): Cyclone #BulBul is likely to weaken gradually &amp; move Northwards and cross West Bengal-Bangl…
#CycloneBulbulUpdate ফাঁকা করে দেওয়া হয়েছে সব হোটেল, পর্যটকশূন্য সমুদ্র সৈকত, দীঘায় কমছে ঝড়ের দাপট https://t.co/sQd7qi13cl
Cyclone 'BULBUL' may cast severe damage to life &amp; property from 9th Nov to 10th Nov. It is advised to restrict move… https://t.co/Cn4r3xGyGW
Medyo Makulot at masalimuot ang Bagyo nayan.  Hahahahahaha https://t.co/n0A5pqWjWy
At the control room of Kolkata Municipal Corporation, for closely monitoring the situation as Cyclone Bulbul is abo… https://t.co/7U8xOV3Vnr
RT @bbcweather: Very Severe Cyclonic Storm BULBUL will affect West Bengal and Bangladesh this weekend. Wind gusts may reach 150kph but rain…
RT @parthasri201475: 🌀Why cyclones weaken after landfall?"""

#preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
for i in range(len(sentences)):
    sentences[i]=[word for word in sentences[i] if word not in stopwords.words('english')]
model = Word2Vec(sentences,min_count=1)
model = model.wv.vocab
vector = model.wv[' Corporation']   

