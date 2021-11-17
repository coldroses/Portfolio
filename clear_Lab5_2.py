#paul clear status: complete

#formula for object falling d=1/2gt**2
#d = distance in meters
#g = 9.8m/s**2 (gravitational constant)
#t = time in seconds object has been falling

#calculate distance in meters based on object's falling time

#import distance before main function
from distance import falling_distance 

#main function
#ask user number of seconds object has been falling
#start for loop calls falling_distance function
#passes number of seconds from 1 to the rounded number of seconds
#object has been falling
#must be a positive number, non-zero
def main():
    timeSec = float(input('Enter falling time in seconds: '))
    while timeSec <= 0:
        timeSec = float(input('The value must be positive. Try again: '))
    timeSecInt = int(timeSec)
    r = timeSec % timeSecInt
    if r >= .5:
        timeSecInt += 1
    print('Time\tFalling distance (meters)')
    print('-------------------------------')
    for i in range (1, timeSecInt + 1):
        print(i, '\t', format(falling_distance(i), '.2f'))

#falling_distance function on another module
#calculate and return distance in meters
#distance():
    
#main function displays the return distance
#distance values rounded to two decimals

main()


#need table
# Time     Falling distance
# -------------------------
# 1             10
# 2
# etc          etc
