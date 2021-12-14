# Paul Clear Program Status: complete

#ask the user to enter the number of packages purchased.
#if user enters a fraction, code should convert to a whole number
#if an invalid number is entered, "invalid number of packages!" must be shown
packagesPurchased = int(input('Enter the number of packages purchased: '))

#if number entered is valid (positive number, greater than zero)
while packagesPurchased <= 0:
    print ('Invalid number of packages!')
    packagesPurchased=int(input("Enter a positive number: "))
    

#define software package price
software_package = 149.00

# define purchase qty & discount percentage
# qty       disc
# 150 or more  40%
# 100-149   30%
# 50-99     20%
# 10-49     10%
# 1-9       none



#nested/multi-nested section
#if packages purchased 150 or greater
if packagesPurchased >= 150:
    discount_amount = (packagesPurchased * software_package) * 0.4 
    total = (packagesPurchased * software_package) - discount_amount 
#display the dollar amount of
#the discount and the total amount of purchase after discount
    


# 100-149
elif packagesPurchased >= 100:
    discount_amount = (packagesPurchased * software_package) * 0.3 
    total_after_discount = (packagesPurchased * software_package) - discount_amount
    
# 50-99
elif packagesPurchased >= 50:
    discount_amount = (packagesPurchased * software_package) * 0.2 
    total_after_discount = (packagesPurchased * software_package) - discount_amount
   
# 10-49
elif packagesPurchased >= 10:
    discount_amount = (packagesPurchased * software_package) * 0.1 
    total_after_discount = (packagesPurchased * software_package) - discount_amount

# 1-9
else:
    total_without_discount = packagesPurchased * software_package

print('Discount amount: $', format(discount_amount,',.2f'))
print('total: $', format(total_after_discount,',.2f'))

#example output/sample dialog
#Enter the number of packages purchased: 53
#Discount amount: $1,579.40
#Total after discount: $6,317.60

