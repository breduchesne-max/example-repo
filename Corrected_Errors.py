'''errors.py file first'''
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") #missing parentheses
print ("\n") 

'''syntax error, missing parentheses and indentation error."

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" 
age = int(age_Str)     
print("I'm" + str(age) + "years old.")

'''#indentation error with these three lines. The print line was incorrect syntax'''

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"
total_years = int(years_from_now)
print("In 3 years, I'll be " + str(total_years) + " years old.")


''' indentation error with the three lines above, and a type error because you can't add an int and a str together. 
syntax error on second line.  missing int() function and parentheses.  There was also no print line'''

print ("The total number of years:" + str(total_years))

'''indentation error and missing parentheses'''

# Variable to calculate the total number of months from the given number of years and printing the result
total_months = total_years * 12
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

'''missing parentheses and indentation error.  Also, the total_months variable is not being calculated correctly.  
It should be total_years * 12 + 6 to account for the additional 6 months.'''

#HINT, 330 months is the correct answer


'''errors2.py file second'''
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a " + animal + ". It is a " + str(number_of_teeth) + " and it has " + animal_type + " teeth"

print (full_spec)