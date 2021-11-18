# -*- coding: utf-8 -*-
"""
Author: Vamsi Yalamanchili
Date: 17-Nov-2021
Purpose: Script for Merge Sort
"""

import random
from random import seed 

#Rescursive Function to Split the Data, Sort and then Merge again
def mergeSort(inpList,n):
    if(n>1):
        mid = n//2  #get the integer floor value only
        leftList  = inpList[:mid]
        rightList = inpList[mid:]

        leftSortedList = mergeSort(leftList,len(leftList))
        rightSortedList = mergeSort(rightList,len(rightList))
      
        finalList = mergeList(leftSortedList,rightSortedList)  
        return finalList
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
    inputList = random.sample(range(1, 1000), 100)

    print("Input List: ", end="\n")
    printList(inputList)

    #Call the Sort function
    sortedList = mergeSort(inputList, len(inputList))

    print("Sorted List: ", end="\n")
    printList(sortedList)