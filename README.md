# CountingArray
Used to generate possible solutions to the headline puzzle's hat word based on the alphabetical order in the word using the Australian Method. See https://thephoenixsociety.org/hl/SoYouWantToDoTheHeadlinePuzzle.pdf page 37, 50, and the entire document for explanation. 

**PLEASE CHANGE FOR YOURSELF**: Change only the three arrays below """Crazy Importtant""" and the file destination path of the generated json file on line 290. 
hatSequence = [6, 3, 1, 5, 2, 4, 7]
alphabeticalness = [6, 3, 1, 5, 2, 4, 7]
alphabeticalnessOrderOfIndexes = [2, 4, 1, 5, 3, 0, 6] 

where hat sequence descirbes the order that the alphabet appears in a given word (so apple is 1, 4, 5, 3, 2) , alphabeticalness is the same as the hat sequence, and alphabeticalnessOrderOfIndexes is the index number of the hatsequence that the numbers are sequential from low to high (so in the arrays above 1 appears in the 3rd spot of the array so it's in the 2nd array spot since arrays count from 0, 2 is in the array's 4 spot, etc.)

This creates an array of numbers in ascending order based on how long the user sets the hat sequence array. Then it maps it to the alphabet and displays all possible combinations of words based on the hat sequence. Careful that the longer the array, the longer it takes. Then it prints it out to a json file. 
