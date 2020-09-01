#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import pandas

#şifrelenecek düz metin 
plain_text=" bu metin sutunlu transpozisyon sifreleme ile sifrelenecektir"
#key değeri kadar sütuna sahip olacak
key=4
#şifrelenen metni key uzunluğundaki sütunlara yazmak için liste
ciphertext=['']*key
#print(ciphertext) -> ['', '', '', '']

for column in range(key):
    pointer=column
    while pointer<len(plain_text):
        ciphertext[column] += plain_text[pointer]
        print(ciphertext)
        pointer +=key
print(ciphertext)
print(' '.join(ciphertext))
