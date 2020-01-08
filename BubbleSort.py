# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:25:28 2020

@author: Prashant Verma
"""

a=[11,-8,13,28,5]
print(a)
for p in range(len(a)-1):
    for i in range(len(a)-1-p):
        j=i+1
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)    
    