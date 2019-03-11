#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:50:38 2019

@author: Meenal
"""

import os
from collections import Counter
import codecs

def make_dict():
    mail = "emails/"  
    files = os.listdir(mail)  

    emails = [mail + email for email in files]   

    words= [] 

    c = len(emails) 

    for email in emails :
        f= codecs.open(email, "r",encoding='utf-8', errors='ignore')
        words += f.read().split(" ")
        print (c)
        c-= 1
    
    
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""  
    dictionary = Counter(words)    
    del dictionary [""]
    return (dictionary.most_common(2000))
