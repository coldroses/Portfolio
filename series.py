#calculate teh sum of a series of numbers entered by user

maximum = 5 #the maximum number

#initialize an accumulator variable
total = 0.0

#explain concept to user
print('This program calculates the sum of')
print(maximum, 'numbers you enter.')

#get numbers, accumulate
for counter in range(maximum):
        number = int(input('Enter a number: '))
        total = total + number

        #Display the total of the numbers.
        print('The total is', total)
