#Paul Clear - status: complete

# enter the 4 serving recipe for spaghetti sauce

#2 cup tomato sauce 1/3 cup of tomato paste (.333) 2 clove garlic 1 tbsp oregano
# these ammounts will be divided by 4 to produce single serving amounts

2 / 4     # cup tomato sauce
.333 / 4  # cup tomato paste
2 / 4     # cloves garlic
1 / 4     #tablespoon oregano


# divide by 4 to break down recipe into a "per serving" format. use named
# constants to identify ingredients and single (or "per") serving ratio.

# single serving amounts
tomato_sauce_per_serv = .5
tomato_paste_per_serv = .08325 
garlic_clove_per_serv = .5
oregano_tbsp_per_serv = .25

# write equation in program to multiply by desired input - number of servings
# user needs. Round to 2nd decimal point.

desired_servings = float(input('Enter how many servings of spaghetti sauce you would like to make? '))
print("To make", end=' ')
print(desired_servings, end=' ')
print("servings of spaghetti sauce, you will need:")
print(format(desired_servings * tomato_sauce_per_serv, '.2f'), 'cups of tomato sauce')
print(format(desired_servings * tomato_paste_per_serv, '.2f'), 'cups of tomato paste')
print(format(desired_servings * garlic_clove_per_serv, '.2f'), 'cloves of garlic clove')
print(format(desired_servings * oregano_tbsp_per_serv, '.2f'), 'tbsp of oregano')

