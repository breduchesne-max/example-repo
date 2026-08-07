# Create a new Python file called age-quiz.py. The program you create in this file will be used to output a variety of responses determined by the data the user enters.
# Write code to take in a user's age and store it in an integer variable called age.
# Assume that the oldest someone can be is 100; if the user enters a higher number, output the message: "Sorry, you're dead."
# If the user is 65 or older, output the message: "Enjoy your retirement!"
# Ifthe user is 40 or over, output the message: "You're over the hill."
# If the user is 21, output the message: "Congrats on your 21st!"
# If the user is under 13, output the message: "You qualify for the kiddie discount."
# For any other age, output the message: "Age is but a number."

age = int(input("Please enter your age: "))

if age > 100 :
    print ("Sorry, you're dead.")


if age <= 13 :
    print("You qualify for the kiddie discount")
    

if age >= 65 and age <= 99 :
    print("Enjoy your retirement!")


if age >= 40 and age <= 64 :
    print("You're over the hill.")

else :
    print("Age is just a number.")
