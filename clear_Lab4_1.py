#paul clear status: incomplete ... can't get "middle" section & indentation to work

#accumulator
totalExpenses = 0.0
expenses = .001
# budgetDiff = 0

#user input monthly budget]
#amount must be greater than zero and positive
monthlyBudget = int(input('Enter amount budgeted for the month: '))

#while loop to validate
while monthlyBudget < 1.0:
    monthlyBudget = int(input('Enter a positive amount: '))
    format(monthlyBudget, '.2f')
#working through this portion

#while loop asking for expenses
#must be positive number
# 0 will end budget input ("0 to quit")
while expenses != 0:
    expenses = int(input("Enter an amount spent (enter 0 to quit): "))

    while expenses < 0:
        expenses = int(input('Enter a non-negative amount spent: '))
    totalExpenses += expenses



#print total budget, total spend, difference
print('Monthly budget: $',format(monthlyBudget,',.2f'))
print('Spent: $',format(totalExpenses,',.2f'))

#budgetDiff
budgetDiff = monthlyBudget - totalExpenses

#if-elif-else budget calculation
#if positive
if monthlyBudget > totalExpenses:
    print('You are $',budgetDiff , 'under budget. WELL DONE!')

#if negative
elif monthlyBudget < totalExpenses:
    print('You are $',budgetDiff , 'over budget. PLAN BETTER NEXT TIME!')
#budget breaking even
else:
    print("You're right on budget! Excellent!")



#budgeted:
#spent:
#you are $xxx.xx over budget. PLAN BETTER NEXT TIME!
    
