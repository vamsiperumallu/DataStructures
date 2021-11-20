# -*- coding: utf-8 -*-
"""
Author: Vamsi Yalamanchili
Date: 17-Nov-2021
Purpose: Script for Merge Sort

Time complexity: 
    Worst case: O(nlogn)
Space complexity: O(n) - Not Inplace
"""

import random
from random import seed 
import time

#Rescursive Function to Split the Data, Sort and then Merge again
def mergeSort(inpList):
    
    n = len(inpList)
    if(n>1):
        mid = n//2  #get the integer floor value only
        leftList  = inpList[:mid]
        rightList = inpList[mid:]

        leftList = mergeSort(leftList)
        rightList = mergeSort(rightList)
        
        inpList = mergeList(leftList,rightList)  
        return inpList
    else:
        return inpList

def mergeList(leftList,rightList):
    leftLen = len(leftList)
    rightLen = len(rightList)
    
    i = j = 0
    finalList = []
    
    #Traverse through both lists and fill finalList with Sort order
    while i < leftLen and j < rightLen:
        if leftList[i] < rightList[j]:
            finalList.append(leftList[i])
            i += 1
        else:
            finalList.append(rightList[j])
            j += 1
  
    # Checking for leftover elements
    while i < leftLen:
        finalList.append(leftList[i])
        i += 1
  
    while j < rightLen:
        finalList.append(rightList[j])
        j += 1
    return finalList
        
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
    #Call the Sort function
    inputList = mergeSort(inputList)
    
    print("--- %s seconds for Merge Sort of 100 elements---" % (time.time() - start_time))

    print("Sorted List: ", end="\n")
    printList(inputList)