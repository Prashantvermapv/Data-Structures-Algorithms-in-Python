# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 21:12:31 2020

@author: Prashant Verma
"""

def binary_search(input_array, value):
    min=0
    max=len(input_array)-1
    print(max,min)
    while max>=min:
        mid=(min+max)//2
        print(mid)
        if value>input_array[mid]:
            min=mid+1
        elif value<input_array[mid]:
            max=mid-1
        else:
            return mid
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))