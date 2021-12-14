#paul clear status: complete

#loops asks for following info until user chooses to quit (press Enter at prompt)
#course number, meeting room, meeting time, instructor name

#program creates a dictionairy containing course numbers as keys, rooms as values
#second dictionary containing course numbers as keys, meeting times as values
#third dictionary course numbers as keys, instructor names as values
#every time info about a course is added, it hsould be added to the three dicts

course_rooms = {}
course_times = {}
course_instructor = {}

#once enter is pressed at the course number prompt
#the program should start a loop which continues to ask for a course number
#until user chooses to quit by pressing enter

while True:
    courseNum = input('Enter a new course number or press Enter to stop: ')
    if courseNum == "":
        break
    course_rooms[courseNum] = input('Enter the course meeting room: ') 
    course_times[courseNum] = input('Enter the course meeting time: ')
    course_instructor[courseNum] = input("Enter the course instructor's name: ")

#every time a course number is entered
#program should display courses meeting room, meet time, and instr name
#if the course is not in the dictionary,  a message should be displayed
while True:
    courseInt = input('Enter a course number of interest or press Enter to stop: ')
    if courseInt == "":
            break
#other method?
    #courseInt = course_rooms.get(courseNum,' is an invalid course number')
    if courseInt in course_rooms:
        print('The meeting room is: ',course_rooms[courseInt])
        print('The meeting time is: ',course_times[courseInt])
        print('The instructor name is: ',course_instructor[courseInt])
    else:
        print("This is an invalid course number")

##    if courseInt == courseNum:
##        print('The meeting room is: ',course_rooms[courseNum])
##        print('The meeting time is: ',course_times[courseNum])
##        print('The instructor name is: ',course_instructor[courseNum])
##    else:
##        print(courseInt,' is an invalid course number')

#output and dialog
#enter a new course number or press Enter to stop: CS101
#Enter the course meeting room: 3004
#Enter the course meeting time: 8 A.M.
#Enter the course instructor's name: Haynes
#Enter a new course number or press Enter to stop:

#Enter a course number of interest or press Enter to stop: NT110
#NT110 is an invalid course number
#Enter a course number of interest or press Enter to stop: CS101
#The meeting room is: 3004
#The meeting time is: 8 A.M.
#The instructor name is: Haynes
#...
##Enter a course number of interest or press Enter to stop:

