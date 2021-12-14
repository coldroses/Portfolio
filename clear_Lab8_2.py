#paul clear program status: incomplete

#should print the date format as: March 12, 2018

#main
#accept the input of the date mm/dd/yyyy
#calls function isdate, pass string as argument
#must store the month names in a tuple
def main():
    exactDate = input("Enter a date in format mm/dd/yyyy: ")
    isdate(exactDate)
    days = exactDate.split('/')
    if days[0] == '01':
        print('The date is January,', days[1], days[2])
    elif days[0] == '02':
        print('The date is February,', days[1], days[2])
    elif days[0] == '03':
        print('The date is March,', days[1], days[2])
    elif days[0] == '04':
        print('The date is April,', days[1], days[2])
    elif days[0] == '05':
        print('The date is May,', days[1], days[2])
    elif days[0] == '06':
        print('The date is June,', days[1], days[2])
    elif days[0] == '07':
        print('The date is July,', days[1], days[2])
    elif days[0] == '08':
        print('The date is August,', days[1], days[2])
    elif days[0] == '09':
        print('The date is September,', days[1], days[2])
    elif days[0] == '10':
        print('The date is October,', days[1], days[2])
    elif days[0] == '11':
        print('The date is November,', days[1], days[2])
    elif days[0] == '12':
        print('The date is December,', days[1], days[2])
#isdate
#accept string from main
# verify month, day, year contain all digits and that "/" separates them.
#optionally, the month range 01-12 and proper day range each month may also
#be verified
def isdate(exactDate):
    try:
            intValues = []
            month31 = [1, 3, 5, 7, 8, 10, 12]
            month30 = [4, 6, 9, 11]
            values = exactDate.split("/")
            if len(values) != 3:
                return False
            for v in values:
                for ch in v:
                    if not ch.isdigit():
                        return False
                intValues.append(int(v))
            if intValues[0] <= 0 or intValues[0] > 12:
                return False
            if intValues[1] < 1:
                return False
            if intValues[2] < 1:
                return False
            if intValues[0] in month31:
                if intValues[1] > 31:
                    return False
            elif intValues[0] in month30:
                if intValues[1] > 30:
                    return False
            else:
                if intValues[1] > 28:
                    return False
            return True
    except ValueError:
        print('Invalid date entered.')
    except Exception:
        print('Error. Program terminated.')

main()

#sample dialog/output
#Enter a date in the format mm/dd/yyyy: 01162021
#Invalid date entered.
#Enter a date in the format mm/dd/yyyy: p1/16/w021
#Invalid date entered.
#Enter a date in the format mm/dd/yyyy: 01/16/2021
#The date is January 16, 2021
