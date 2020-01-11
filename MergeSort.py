# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:58:49 2020

@author: Prashant Verma
"""

def MergeSort(arr):
    if len(arr)>1:
        m=len(arr)//2
        larr=arr[:m]
        rarr=arr[m:]
        MergeSort(larr)
        MergeSort(rarr)
        i=j=k=0
        while(i<len(larr) and j<len(rarr)):
            if(larr[i]>rarr[j]):
                arr[k]=rarr[j]
                j+=1
            else:
                arr[k]=larr[i]
                i+=1
            k+=1
        while(i<len(larr)):
            arr[k]=larr[i]
            i+=1
            k+=1
        while(j<len(rarr)):
            arr[k]=rarr[j]
            j+=1
            k+=1
    print(arr)

MergeSort([5,7,1,12,9])
[5]
[7]
[5, 7]
[1]
[12]
[9]
[9, 12]
[1, 9, 12]
[1, 5, 7, 9, 12]