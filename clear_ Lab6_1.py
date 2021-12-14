#paul clear status:complete

#random number gen
import random


#user input of num random numbers file will hold.
#at least one, no more than 100
#user input of minimum and maximum values of numbers
#minimum must be 0-499
#max must be >min and <500

#main function
def main():
    file = open('labfile.txt', 'w')
    
    quantity = int(input('How many random numbers to generate (1-100)? '))
    while quantity < 1 or quantity > 100:
        quantity = int(input('The number must be in the range 1-100.'))

    minVal = int(input('How many random numbers to generate (1-499)? '))
    while minVal < 1 or minVal > 499:
        minVal = int(input('The number must be in the range 1-499.'))

    maxVal = int(input('How many random numbers to generate (' + str(minVal) + '-500)? '))
    while maxVal < minVal or maxVal > 500:
        maxVal = int(input('The number must be in the range 1-499.'))

    for i in range (quantity):
        r = random.randint(minVal, maxVal)
        file.write(str(r) + "\n")

    file.close()
    print('The file was created successfully.')

main()
