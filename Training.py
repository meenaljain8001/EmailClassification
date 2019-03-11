#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:50:38 2019

@author: Meenal
"""

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle


def text_model(features, labels):
    x_train,x_test,y_train,y_test = train_test_split(features, labels, test_size = 0.2)
    classifier = MultinomialNB()
    classifier.fit(x_train,y_train)

    predict = classifier.predict(x_test)

    print(accuracy_score(y_test, predict))

    #save the model
    filename = "SpamClassification.sav"
    pickle.dump(classifier, open(filename, 'wb'))
    return filename
