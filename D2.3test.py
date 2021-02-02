# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:32:01 2021

@author: MTAEXAM
"""

dict1 = {'A':"內向穩重",'B':"外向樂觀",'O':"堅強自信",'AB':"聰明自然"}
bloodtype = input("輸入血型：")
name = dict1.get(bloodtype)
if name == None:
    print("Error")
else:
    print(name)