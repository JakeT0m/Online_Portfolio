"""A group of functions that calculates the Population Standard Deviation."""

import math

def Main():
    a = [-5, 1, 8, 7, 2]
    [sd, var, mean] = findStandardDeviation(a)
    print("SD: ", sd, "   Var: ", var, "   Mean: ", mean)
    #Expected output is SD:  4.673328578219169    Var:  21.84    Mean:  2.6 for the starting list of [-5, 1, 8, 7, 2]
    
    
def findStandardDeviation(array):
    """Take a list in, calculate the population standard deviationthe, variance and mean. Returns these as a list in that order."""
    #STEP 1: Find the mean of the list
    mean = totalList(array)/len(array)
    
    #STEP 2: Subtract the mean from the list
    array = subtractList(array, mean)
    
    #STEP 3: Square the Values and Voltages
    array = squareList(array)
    
    #STEP 4: Add all squared difference
    differenceSummed = totalList(array)
    
    #STEP 5: Divide this by the number of samples to find the variance
    variance = differenceSummed / len(array)

    #STEP 6: Square root it
    standardDeviation = math.sqrt(variance)
    
    return [standardDeviation, variance, mean]


def subtractList(array, subtractor):
    """Take a list in and subtracts each member of the list by the subtractor, returns the new list."""
    result = [None] * len(array)          #creates an empty list with the length of 'array'. This speeds up the process by not changing the size of 'result' each iteration
    for i in range(len(array)):
        result[i] = array[i]-subtractor   #subtracts the subtractor from each index in the array. Stores this in result
    return result

def totalList(array):
    """Take a list in and find the total, returns the new list."""
    result = 0
    for i in range(len(array)):
        result = result + array[i]        #adds each value in the passed in array to result
    return result

def squareList(array):
    """Take in list as array, squares each member, return the new array."""
    result = [None] * len(array)
    for i in range(len(array)):
        result[i] = array[i]*array[i]     #squares each member of array and stores them in the result list
    return result

Main()
