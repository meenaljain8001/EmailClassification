#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:50:38 2019

@author: Meenal
"""

import os
from collections import Counter
import codecs

def make_dataset(dictionary):
    mail = "emails/" 
    files = os.listdir(mail)  

    emails = [mail + email for email in files]

    
    features_data = []
    labels = []
    c = len(emails) 
    for email in emails :
        data = []
        f= codecs.open(email, "r",encoding='utf-8', errors='ignore') 
        words = f.read().split(' ')
        for i in dictionary :
            data.append(words.count(i[0]))
        feature_data.append(data)
        if "ham" in email :
            labels.append(0)
        if "spam" in email:
            labels.append(1)
        print(c)
        c = c-1
    return feature_set, labels
