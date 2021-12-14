# paul clear status: complete

#rise anually = 1.8

#table format
#year \t rise (in mm)
print('Year\tRise (in millimeters)')
print('------------------------------')

#For year_of_rise in range (1,26) and print
for yearOf in range (1,26):
    riseAmount = yearOf * 1.8
    print (yearOf, '\t',format(riseAmount,'.2f'))



