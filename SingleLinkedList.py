# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    24-Nov-2021
Purpose: This script will implement the Single Linked List(SLL) concept
         Insert a new element into the SLL at the end
         Print the SLL
         Find size of the SLL         
         Delete an element from the SLL
         Sort the SLL
         Search for an element in the SLL
"""
import random
from random import seed

class Node:
    
    def __init__(self,value = None):
        self.value = value
        self.nextNode = None

class SingleLinkedList:
    
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        
        if self.head == None:
            self.head = Node(value)
        else:
            self.__insert(self.head,value)
    
    def __insert(self,curr_node,value):
        
        if curr_node.nextNode == None:
            curr_node.nextNode = Node(value)
        else:
            self.__insert(curr_node.nextNode,value)
    
    def printSingleLinkedList(self):
        
        if self.head != None:
            self.__printSingleLinkedList(self.head)
        else:
            print("Single Linked List is Empty")
    
    def __printSingleLinkedList(self,curr_node):

        print(curr_node, curr_node.value,curr_node.nextNode)        
        if curr_node.nextNode != None:
            self.__printSingleLinkedList(curr_node.nextNode)
    
    def size(self):
        
        if self.head != None:
            return self.__size(self.head,0)
        else:
            return 0
    
    def __size(self, curr_node,cnt):
        
        cnt += 1
        if(curr_node.nextNode != None):
            cnt = self.__size(curr_node.nextNode,cnt)
        return cnt
            
def fillSingleLinkedList(sll_obj):
    
    seed(123)
    
    inputList = random.sample(range(1,100),10)
    
    print("Input Data: ", inputList)
    
    for i in inputList:
        sll_obj.insert(i)

if __name__ == "__main__":
    
    sll_obj = SingleLinkedList()
    
    fillSingleLinkedList(sll_obj)
    
    sll_obj.printSingleLinkedList()
    
    print("Size of the Single Linked List:", sll_obj.size())
