# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:22:11 2021

@author: MTAEXAM
"""

scort = []
while True:
    inscort = int(input())
    if inscort == "" or inscort < 0:
        break
    else:
        scort.append(inscort)
        scort.sort()
        print(scort)
        scort.reverse()
        print(scort)
        
        