# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    24-Nov-2021
Purpose: This script will implement the Binary Tree concept
         Insert a new element into a tree
         Find the height of the tree
         Search for an element

Time complexity: 
    Worst case: O(height)
"""
import random
from random import seed

"""
This a class to define a node. we know a node can have a Value, Left Child and Right Child.
Use this class whenever we need to insert any new element into the Tree
"""
class Node:
    
    def __init__(self, value = None):
        self.value = value
        self.leftChild = None
        self.rightChild = None

"""
This a class to define the BinarySearchTree and its functions. 
"""        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value,self.root)

    #Private function, Can be called from this class only. This is also a recursive function.
    def _insert(self,value,curr_node): 

        #If the new value is less than current node value and leftChild is not available.
        #Then assign the new node (value) as LeftChild to the Current node
        #Otherwise, do recursive call to traverse next level
        if(value < curr_node.value):
            if (curr_node.leftChild == None):
                curr_node.leftChild = Node(value)
            else:
                self._insert(value,curr_node.leftChild)         

        #If the new value is greater than current node value and rightChild is not available.
        #Then assign the new node (value) as rightChild to the Current node
        #Otherwise, do recursive call to traverse next level
                
        elif(value > curr_node.value):
            if (curr_node.rightChild == None):      
                curr_node.rightChild = Node(value)
            else:
                self._insert(value,curr_node.rightChild)
        if(curr_node == value):
            print("Value already present")

    def printTree(self):
        
        if self.root != None:
            self._printTree(self.root)
        else:
            print("Tree is empty!!!")
    
    #Private function, Can be called from this class only. This is also a recursive function.
    def _printTree(self,curr_node):
        
        if curr_node != None:
            self._printTree(curr_node.leftChild)
            print(curr_node.value)
            self._printTree(curr_node.rightChild)           

def fillBinaryTree(tree):
       
    seed(111)
    
    #Generate 10 random numbers
    inputList = random.sample(range(1, 100), 10)
    
    print("Input data", inputList)
    for i in inputList:
        tree.insert(i)
    
if __name__ == "__main__":
        
    tree = BinarySearchTree()
    fillBinaryTree(tree)
    tree.printTree()    
        
