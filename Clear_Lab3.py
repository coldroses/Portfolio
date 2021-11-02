# Paul Clear Program Status: complete

#ask the user to enter the number of packages purchased.
#if user enters a fraction, code should convert to a whole number
#if an invalid number is entered, "invalid number of packages!" must be shown
packagesPurchased = float(input('Enter the number of packages purchased: '))

#if number entered is valid (positive number, greater than zero)
if packagesPurchased < 0:
    print ('Invalid number of packages!')

#define software package price
software_package = 149.00

# define purchase qty & discount percentage
# qty       disc
# 150 or more  40%
# 100-149   30%
# 50-99     20%
# 10-49     10%
# 1-9       none

buy_150_or_more = 0.40
buy_100 = 0.30
buy_50 = 0.20
buy_10 = 0.10
buy_1 = 1


#nested/multi-nested section
#if packages purchased 150 or greater
if packagesPurchased >= 150.0:
    discount_amount = (packagesPurchased * software_package) * buy_150_or_more 
    total_after_discount = (packagesPurchased * software_package) - discount_amount 
#display the dollar amount of
#the discount and the total amount of purchase after discount
    print('Discount amount: $', format(discount_amount,',.2f'))
    print('Total after discount: $', format(total_after_discount,',.2f'))


# 100-149
elif packagesPurchased >= 100.0 and packagesPurchased <= 149.0:
    discount_amount = (packagesPurchased * software_package) * buy_100 
    total_after_discount = (packagesPurchased * software_package) - discount_amount
    print('Discount amount: $', format(discount_amount,',.2f'))
    print('Total after discount: $', format(total_after_discount,',.2f'))

# 50-99
elif packagesPurchased >= 50.0 and packagesPurchased <= 99.0:
    discount_amount = (packagesPurchased * software_package) * buy_50 
    total_after_discount = (packagesPurchased * software_package) - discount_amount
    print('Discount amount: $', format(discount_amount,',.2f'))
    print('Total after discount: $', format(total_after_discount,',.2f'))

# 10-49
elif packagesPurchased >= 10.0 and packagesPurchased <= 49.0:
    discount_amount = (packagesPurchased * software_package) * buy_10 
    total_after_discount = (packagesPurchased * software_package) - discount_amount
    print('Discount amount: $', format(discount_amount,',.2f'))
    print('Total after discount: $', format(total_after_discount,',.2f'))

# 1-9
else:
    packagesPurchased >= 1.0 and packagesPurchased <= 9.0
    total_without_discount = packagesPurchased * software_package
    print('Total: $', format(total_without_discount, ',.2f'))

#example output/sample dialog
#Enter the number of packages purchased: 53
#Discount amount: $1,579.40
#Total after discount: $6,317.60

