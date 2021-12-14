#paul clear program status: complete

#accept user input of a list of numbers and a number 'n'
#then prog displays all numbers in the list greater than 'n'

import math

#should have two functions
#main function should call display_larger function
#and pass two arguments: numbers stored in a list and number 'n'
def main():
    
#display_larger func should accept two paraments from main
#use a loop to compare all the numbers in the list to 'n'
    try:
        list1=[]
        count = 0
        elQuant = -1
        while elQuant <= 0:
            elQuant = float(input('Enter the number of elements in the list: '))
            if elQuant <= 0:
                print('The number must be one or more')
        elQuant = math.ceil(elQuant)
        for count in range(elQuant):
            element = int(input('Enter a number: '))
            list1.append(element)
        n = int(input('Enter the number you wish to test if the list' +
                     ' elements are greater than: '))
        display_larger(list1, n)

#if number is larger than n, store in second list w numbers
#greater than "n"
       
            
#display larger should then display resultant list of numbers

#elements in list must be an int and >= 1
#if decimcal is entered, round to nearest int
#each element must be a number, including n
        
#use try and except clauses to handle ValueError and
#unspecified error exceptions
#test for invalid cases, enter bad data


    except ValueError:
        print('Incorrect data type: a number was expected. Program terminated.')
    except Exception:
        print('Error. Program terminated.')

def display_larger(list1, n):
    list2 = []
    for item in list1:
        if item > n:
            list2.append(item)
    print('These numbers are greater than', n, ':', list2)
main()


#sample dialog
#enter the number of elements in the list: -4
#the number must be 1 or more.
#enter the number of elements in the list: 5.7
#enter a number: 3.14
#enter a number: 2.178
#enter a number: 4
#enter a number: 6.564
#enter a number: 9.21
#enter a number: 5
#enter the number you wish to test if the list elements are
#greater than: 4.1257
#these numbers are greater than 4.1257: [6.564, 9.21, 5.0]

