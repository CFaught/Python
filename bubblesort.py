#Author: Caleb Faught
# bubblesort.py
# simple bubble sort algorithm


#function declaration that implements bubble sort to an array as the argument.
def bubblesort(anarray):
    length = len(anarray)
    for i in range(length):
        for j in range(length - 1):
            if anarray[j] > anarray[j + 1]:
                anarray[j], anarray[j + 1] = anarray[j + 1], anarray[j]
                print(anarray)
#make an array that is out of order: 
notinorder = [0, 3, 5, 9, 2, 7, 6, 8, 1, 4]
print(notinorder)

#call function with our out of order array as an argument
bubblesort(notinorder)


