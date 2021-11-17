#paul clear status: complete
#each function should begin with a short comment explaining what it does
#use named constants for all number values that will not be changed in
#the program

#5 different food critics, numeric score 0-10. higher rating is better avg
#must be 0-10
#error message for negative:
#Error: the score must be from 0 to 10

#two functions: main & determine_stars

#main loop accepts input of five numeric ratings from the user using loop
def main():
    average = 0 
    for i in range (0,5):
        num = float(input('Enter the number of stars from 0-10: '))
        while num < 0 or num > 10:
            num = float(input('The value must be 0-10. Try again: '))
        average += num
    average /= 5
    determine_stars(average)
                
       
   
        #print('The score must be from 0 to 10')
    

#pass numeric average to determine_stars function
#displays the number of stars based on numeric average
def determine_stars(average):
    if average >= 9.0:
        starNum = '*****'
    elif average >= 8.0:
        starNum = '****'
    elif average >= 7.0:
        starNum = '***'
    elif average >= 6.0:
        starNum = '**'
    elif average >= 5.0:
        starNum = '*'
    else:
        starNum = 'no stars'
    print('Your score of', format(average, '.2f'), 'gives the rating',starNum)

#9.0 or higher *****
#8.0 - 8.9  ****
#7.0 - 7.9 ***
#6.0 - 6.9 **
#5.0 - 5.9 *
#Below 5.0 no stars

main()

#display numeric average (rounded to 2 decimals) and number of stars
#your score of _.__ gives the rating _____
