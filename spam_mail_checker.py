# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:47:04 2023

@author: KIIT
"""

import pandas as pd
messages = pd.read_csv('C:/Users/KIIT/Downloads/sms+spam+collection/SMSSpamCollection',sep = '\t',names=["labels","message"])

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

# Initialize the stemmer and lemmatizer
ps = PorterStemmer()
#wordnet = WordNetLemmatizer()

# Assuming you have defined 'paragraph' earlier
#sentences = nltk.sent_tokenize(messages)
corpus = []

for i in range(0,len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['message'][i])
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if word not in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the bag of words model
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()

y = pd.get_dummies(messages['labels'])
y = y.iloc[:,1].values

# train test split

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# Create an instance of the Multinomial Naive Bayes classifier
spam_detect_model = MultinomialNB()

# Train the model on the training data
spam_detect_model.fit(x_train, y_train)

# Make predictions on the test data
y_pred = spam_detect_model.predict(x_test)

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)





