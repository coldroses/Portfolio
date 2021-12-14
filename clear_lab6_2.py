#paul clear status: complete

def main():

    try:
        readFile = open('labfile.txt','r')
        total = 0
        count = 0
        print('Reading the file... done.')
        #line = readFile.readline()
        #count = len(readFile.readline())
        #while line != '':
        for amount in readFile:
            amount = int(amount)
            #line = readFile.readline()
            total += amount
            count += 1
            #print(amount)
        print('Read from the file: ',count,' numbers')

        
        print('Total of the numbers: ', total)
        
        avg = total / count
        print('Average of the numbers: ', avg)

        readFile.close()
            
    except IOError:
        print("Reading the file... this filename doesn't exist. Program terminated.")
    except ValueError:
        print("Reading the file... incorrect data type. Program terminated.")
    except ZeroDivisionError:
        print("Average of the numbers: can't be calculated.")
    except Exception:
        print('Reading the file... other error occurred. Program terminated')
main()

#output (no exceptions)
# Reading the file... done.
# Read from the file: 80 numbers.
# Total of the numbers: 5600
# Average of the numbers: 70.00

#IOError exception(file doesn't exist):

#reading the file... this filename doesn't exist. Program terminated.

#ValueError exception(bad data in the file):

#Reading the file... incorrect data type. Program terminated.

#ZeroDivisionError exception (empty file)

#Reading the file... done.
#Read from the file: 0 numbers.
#Total of the numbers: 0
#Average of hte numbers: can't be calculated.

