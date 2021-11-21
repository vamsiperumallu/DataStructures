# -*- coding: utf-8 -*-
"""
Author: Vamsi Yalamanchili
Date: 20-Nov-2021
Purpose: Script for Quick Sort

Time complexity: 
    Average case: O(nlogn)
    Worst case:   O(n^2)
Space complexity: Use same list - Inplace        
"""

import random
from random import seed 
import time

#Rescursive Function to Split the Data, Sort
def quickSort(inpList, start, end):
    if(start < end):
        pivotIndex = partition(inpList, start, end)
        quickSort(inpList, start, pivotIndex-1)          #Calling the quickSort with left of Pivot
        quickSort(inpList, pivotIndex+1, end)            #Calling the quickSort with right of Pivot
            
def partition(inpList, start, end):
    pivot = inpList[end]
    pIndex = start
    
    for i in range(start, end):
        if(inpList[i] <= pivot):
            
            #Swap the element at pIndex with element at i
            temp = inpList[pIndex]
            inpList[pIndex] = inpList[i]
            inpList[i] = temp
            pIndex += 1
    
    #Swap the element at pIndex with element at the end (pivot)
    temp = inpList[pIndex]
    inpList[pIndex] = inpList[end]
    inpList[end] = temp        
    return pIndex
        
#Function to print the List
def printList(inpList):
    print(inpList)
#    for i in inpList:
#        print(i, end=",")
#    print()

if __name__ == "__main__":   
    seed(111)

    #Generate n random numbers
    inputList = random.sample(range(1, 1000000), 100)

    print("Input List: ", end="\n")
    printList(inputList)

    start_time = time.time()
    #Call the Sort function - pass Input list, Starting Index and End Index
    quickSort(inputList, 0, len(inputList)-1)

    print("--- %s seconds for Quick Sort of 100 elements---" % (time.time() - start_time))
    
    print("Sorted List: ", end="\n")
    printList(inputList)