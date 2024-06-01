# a "counting" array
arrayOfMatrixPositions = []

# there's a maximum value that my array can be. this is equivalent to the length of my column of my matrix. 
# let's pretend I have a 4x3 matrix to start with. 4 columns and 3 rows. 
"""
Read As:
    1 4 7 10
    2 5 8 11
    3 6 9 12
"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


"""Crazy Important"""
hatSequence = [6, 3, 1, 5, 2, 4, 7]
alphabeticalness = [6, 3, 1, 5, 2, 4, 7]
alphabeticalnessOrderOfIndexes = [2, 4, 1, 5, 3, 0, 6] 
#  9, 5, 1, 7, 2, 6, 10, 8, 3, 4
# 2, 4, 8, 9, 1, 5, 3, 7, 0, 6
hatSequenceAlphabet = []

index = 0
for number in hatSequence:
    hatSequence[index] = (number - 1) * 2
    hatSequenceAlphabet.append(alphabet[hatSequence[index]])
    index += 1

print(*hatSequence)

hatSequenceNumberMatrix = []

for col in range(len(hatSequence)):
    a = []
    firstValue = hatSequence[col] 
    #print("\n {0} \n".format(firstValue))
    valueMinus = -4
    for value in range(9):
        if firstValue + valueMinus < 0:
            a.append(firstValue + valueMinus + 26)
        else:
            a.append(firstValue + valueMinus)
        valueMinus += 1
    hatSequenceNumberMatrix.append(a)

print(*hatSequenceNumberMatrix)

for value in range(len(hatSequenceNumberMatrix[0])):
    for col in range(len(hatSequenceNumberMatrix)):
        pass
        #letterMatrix[col][value] = alphabet[matrix[col][value]]
        #print(hatSequenceNumberMatrix[col][value], end=" ")
    #print()

#matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10], [10, 11, 12, 13], [14, 15, 16, 17]]

matrix = hatSequenceNumberMatrix

for value in range(len(matrix[0])):
    for col in range(len(matrix)):
        pass
        #letterMatrix[col][value] = alphabet[matrix[col][value]]
        #print(matrix[col][value], end=" ")

# my counting array will then be as long as the number of columns my matrix has 
# so populate those positions with zeros. 

for column in range(len(matrix)):
    arrayOfMatrixPositions.append(0)

#print(*arrayOfMatrixPositions)

# the max number that any position can be is equal to the length of one the arrays in the matrix (the row)

maxNumber = len(matrix[0]) - 1
#print (maxNumber)



# I need a function that all it does it iterate a column of the counter array by one

def interateColumnByOne(column):
    #print(*arrayOfMatrixPositions)
    arrayOfMatrixPositions[column] += 1
    #print("Iterated by One: ")
    #addtoArray(arrayOfMatrixPositions)
    #          print(*arrayOfMatrixPositions)

# I need a function that all it does it tell if I CAN iterate a column of the counter array by one

def canInterateColumnByOne(column):
    if arrayOfMatrixPositions[column] + 1 > maxNumber:
        #print("Can't interate col by one: {0}".format(column))
        #print(column)
        #print(arrayOfMatrixPositions[column])
        return False
    #print("Can interate col by one")
    return True

# So if it is valid for me to iterate then let's iterate
# I need to keep doing this until the maxNumber is reached

def iterateAColumnCompletely(column):
    while arrayOfMatrixPositions[column] < maxNumber:
        if canInterateColumnByOne(column):
            interateColumnByOne(column)
            #print(*arrayOfMatrixPositions)

def isThereALeftColumnToInterate(column):
    checkCol = column - 1
    while checkCol >= 0:
        if arrayOfMatrixPositions[checkCol] < maxNumber:
            #print("Yes there's a column to the left to iterate. Column # {0}".format(checkCol))
            return True
        else:
            checkCol -= 1
    #print("No there's not a column to the left to iterate")
    return False

def whatLeftColumnToIterate(column):
    checkColumn = column
    while checkColumn >= 0:
        if arrayOfMatrixPositions[checkColumn] < maxNumber:
            #print("What left column to iterate")
            #print(checkColumn)
            return checkColumn
        else:
            checkColumn -= 1

# then I need to tell it to iterate the previous row by one
# so as long as there isn't a column to the right of my current iterating row iterate until I reach the max



"""
def myLoop(currentColumn):
    # if we're in the last column, iterate, when do ask the column to the left if we can +1, if so iterate again
    if currentColumn == len(arrayOfMatrixPositions):
        while canInterateColumnByOne(currentColumn):
            interateColumnByOne(currentColumn)
# if that's not true then I want to check is there a row to the left that isn't at max that we can iterate too?
    if isThereALeftRowToInterate(currentColumn):
        currentColumn -= 1
        # then for every column to the right I want to set to zero
        for column in range(currentColumn + 1, len(arrayOfMatrixPositions)):
            arrayOfMatrixPositions[column] = 0
            print("Set to Zero: ")
            print(*arrayOfMatrixPositions)
        interateColumnByOne(currentColumn)

while currentColumn >= 0:
    myLoop(currentColumn)
    currentColumn -= 1
    print(currentColumn)
"""




# Always iterate the last column, when it's done. ask the column to the left if we can +1. if so, then do that reset 
# last to 0 and iterate again. if the column directy to the left is at max then ask the column to the left of that if it can
# plus one, then reset all to the right as 0 and repeat

array = []
def addtoArray(currentArrayofMatrixPositions):
    tempArray = []
    for position in range(len(currentArrayofMatrixPositions)):
        value = currentArrayofMatrixPositions[position]
        tempArray.append(value)
    array.append(tempArray)

def myLoop(column):
    #print(column)
    while canInterateColumnByOne(column):
        #print(*arrayOfMatrixPositions)
        interateColumnByOne(column)
        addtoArray(arrayOfMatrixPositions)
        #print("from myLoop")
        #print(*arrayOfMatrixPositions)

    #if arrayOfMatrixPositions[column] >= maxNumber:
    if isThereALeftColumnToInterate(column):
        if canInterateColumnByOne(whatLeftColumnToIterate(column)):
            currentCol = whatLeftColumnToIterate(column)
        # then for every column to the right I want to set to zero
            for number in range(currentCol + 1, len(arrayOfMatrixPositions)):
                #print("I get to the for loop")
                arrayOfMatrixPositions[number] = 0
                #print(*arrayOfMatrixPositions)
                #print("Set to Zero: ")
                #print(*arrayOfMatrixPositions)
            #print(*arrayOfMatrixPositions)
            #addtoArray(arrayOfMatrixPositions)
            interateColumnByOne(currentCol)
            addtoArray(arrayOfMatrixPositions)
            #print(*arrayOfMatrixPositions)
            #addtoArray(arrayOfMatrixPositions)
            #print("anytime there is an iterateColumn by one I want to add this to my array")
            #currentColumn = len(arrayOfMatrixPositions) - 1


def allColumnsAreAtMaxNumber():
    number = 0
    for col in arrayOfMatrixPositions:
        number += col
    #print(number)
    return number

currentColumn = len(arrayOfMatrixPositions) - 1
#while arrayOfMatrixPositions[2] < maxNumber:
addtoArray(arrayOfMatrixPositions)
#            print(*arrayOfMatrixPositions)
while allColumnsAreAtMaxNumber() != maxNumber * len(arrayOfMatrixPositions):
    #(*arrayOfMatrixPositions)
    #print ("i is {0}".format(i))
    myLoop(currentColumn)
#for item in array:
    #pass
    #print(item)


# #alphabeticalness = [9,5,1,7,2,6,10,8,3,4]
# hatSequence = [9, 5, 1, 7, 2, 6]

# then take array and the matrix and map the matrix to the array
matrixToArray = []
for index in range(len(array)):
    tempA = array[index]
    #print(tempA)
    tempB = []
    for indexoftempA in range(len(tempA)):
        tempB.append(matrix[indexoftempA][tempA[indexoftempA]])
    

    # then check if tempB (the array of the hatSequence numbers based on the array index and array position of tempA)
    # has the alphabeticalness of the hatsequence
    # #alphabeticalness = [9,5,1,7,2,6,10,8,3,4]
    # find the position in the alphabeticalness that should come first
    #print(*tempB)
    #alphabeticalnessOrderOfIndexes  = [2, 4, 1, 5, 3, 0]
    iAmTheAlphabeticalness = True
    for index in range(len(alphabeticalnessOrderOfIndexes)):
        #print(value)
        value = alphabeticalnessOrderOfIndexes[index]
        if value < len(tempB) and index + 1 < len(alphabeticalnessOrderOfIndexes):
            if iAmTheAlphabeticalness:
                if tempB[value] < tempB[alphabeticalnessOrderOfIndexes[index + 1]]:
                    #print("yes")
                    iAmTheAlphabeticalness = True
                else:
                    iAmTheAlphabeticalness = False
                    break
    #print(*tempB)
    if iAmTheAlphabeticalness:
        #print(*tempB)
        matrixToArray.append(tempB)


    
    
        
    
    

    #print(tempB)
    
    
    #matrixToArray.append(matrix[place][value])
    #for position in range(len(array[spot])):
    #print("yee")
    #print(*array[spot])
    #matrixToArray.append(matrix[position][array[spot][position]])
    #matrixToArray.append(matrixToArray[array[spot]][spot])

writeThisArrayToFile = []
for thing in matrixToArray:
    #for ya in range(len(thing)):
    tempC = thing
    for thong in range(len(tempC)):
        tempC[thong] = alphabet[tempC[thong]]
    #print(*tempC)

    strin = ""
    for place in range(len(tempC)):
        strin += tempC[place]
    #print(strin)
    writeThisArrayToFile.append(strin)


with open('Desktop/Python/possibleAnswersToHeadlinePuzzle.txt', 'w') as f:
    for line in writeThisArrayToFile:
        f.write(f"{line}\n")





"""
iterateAColumnCompletely(currentColumn)
# when I iterate a column competely, I need to say the current column is now one to the left
currentColumn -= 1
#print(currentColumn)
interateColumnByOne(currentColumn)
# then each column to the right needs to be reset to 0

while 
if currentColumn < len(arrayOfMatrixPositions) - 1:
    iterateAColumnCompletely(currentColumn)
    currentColumn += 1

"""
#array

#def addOne ():
