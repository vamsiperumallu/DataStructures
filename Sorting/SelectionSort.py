# -*- coding: utf-8 -*-
"""
Author: Vamsi Yalamanchili
Date: 20-Nov-2021
Purpose: Script for Selection Sort

Time complexity: 
    Best Case:    O(n)            #Already Sorted Array as input
    Average case: O(n^2)
    Worst case:   O(n^2)
Space complexity: Use same list - Inplace        
"""

import random
from random import seed 
import time

def selectionSort(inpList):

    len1 = len(inpList)
   
    for k in range(0,len1):
        minIndex = k

        for i in range(k+1,len1):                   #Find minimum of the list
            if (inpList[minIndex] > inpList[i]):
                minIndex = i
            
        if (minIndex != k):
            temp = inpList[k]                       #Swap side by side elements
            inpList[k] = inpList[minIndex]
            inpList[minIndex] = temp
        
    return inpList

#Function to print the List
def printList(inpList):
    print(inpList)
#    for i in inpList:
#        print(i, end=",")
#    print()

if __name__ == "__main__":   
    seed(111)

    #Generate n random numbers
    inputList = random.sample(range(1, 100), 20)

    print("Input List: ", end="\n")
    printList(inputList)

    start_time = time.time()
    
    #Call the Sort function - pass Input list to be sorted
    selectionSort(inputList)

    print("--- %s seconds for Selection Sort of 100 elements---" % (time.time() - start_time))
    
    print("Sorted List: ", end="\n")
    printList(inputList)