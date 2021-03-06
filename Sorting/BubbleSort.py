# -*- coding: utf-8 -*-
"""
Author: Vamsi Yalamanchili
Date: 20-Nov-2021
Purpose: Script for Bubble Sort

Time complexity: 
    Best Case:    O(n)            #Already Sorted Array as input
    Average case: O(n^2)
    Worst case:   O(n^2)
Space complexity: Use same list - Inplace        
"""

import random
from random import seed 
import time

def bubbleSort(inpList):

    len1 = len(inpList)
   
    for k in range(1,len1-1):
        flag = 0                                #If already sorted, i.e. there were no swaps happened then return.
        for i in range(0,len1-1):
            if (inpList[i] > inpList[i+1]):
                temp = inpList[i]               #Swap side by side elements
                inpList[i] = inpList[i+1]
                inpList[i+1] = temp
                flag = 1
        if flag == 0:
            return inpList
    return inpList

#Function to print the List
def printList(inpList):
    print(inpList)
#    for i in inpList:
#        print(i, end=",")
#    print()

if __name__ == "__main__":   
    seed(122)

    #Generate n random numbers
    inputList = random.sample(range(1, 10000), 100)

    print("Input List: ", end="\n")
    printList(inputList)

    start_time = time.time()
    
    #Call the Sort function - pass Input list to be sorted
    bubbleSort(inputList)

    print("--- %s seconds for Bubble Sort of 100 elements---" % (time.time() - start_time))
    
    print("Sorted List: ", end="\n")
    printList(inputList)