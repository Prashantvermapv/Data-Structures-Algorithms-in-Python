# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 13:27:15 2019

@author: Prashant Verma
"""
class Element():
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList():
    def __init__(self,head=None):
        self.head=head
        
    def append(self,new_element):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_element
        else:
            self.head=new_element
    def get_position(self,position):
        count=1
        if position<count:
            return None
        if self.head:
            current=self.head
            while current: 
                if count==position:
                    return current.value
                current=current.next
                count+=1
            return None
        else:
            return None
    def insert(self,new_element,position):
        count=1
        current=previous=self.head
        if position==1:
            e=Element(new_element)
            e.next=current
            self.head=e
            return

        if self.head:
            while current:
                if count==position:
                    e=Element(new_element)
                    e.next=current
                    previous.next=e
                previous=current
                current=current.next
                count+=1
        else:
            e=Element(new_element)
            self.head=e 
    def delete(self,value):
        current=previous=self.head
        if value==self.head.value:
            self.head=current.next
            return
        if self.head:
            while current:
                if current.value==value:
                    previous.next=current.next
                previous=current
                current=current.next

                    
my=LinkedList()
e1=Element(200)
e2=Element(100)
e3=Element(222)
my.append(e1)
my.append(e2)
my.append(e3)
my.delete(222)
print(my.get_position(4))
my.insert(32,3)
print(my.get_position(1))
my.insert(3222,3)
print(my.get_position(2))
my.insert(3222,1)
print(my.get_position(3))