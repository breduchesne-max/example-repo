# Create a new Python file in the task folder called award.py.
# Design a program that determines the award a person competing in a triathlon will receive.
# Your program should accept user inputs for the times (in minutes) of all three triathlon events, 
# namely swimming, cycling, and running, 
# then calculate and output the total time to complete the triathlon.
# The award a participant receives is based on the total time taken to complete the triathlon. 
# Determine the award that the participant will receive based on the following criteria:
# 0-100 minutes : Provincial colours
# 101-105 minutes : Provincial half colours
# 106-110 minutes : Provincial scroll
# 111+ minutes : No award
# Output the award they will receive or 'No award'. For example: Award: Provincial scroll or No Award

Swim_time = int(input("Enter your Swim Time: "))
Cycle_time = int(input("Enter your Cycling time: "))
Running_time = int(input("Enter your Run time: "))

Total_time = Swim_time + Cycle_time + Running_time

print("Your Total time is :" , Total_time)

if Total_time <= 100 :
    print ("Provincial colours")

elif Total_time <= 105 :
    print("Provincial half colours")

elif Total_time <=106 :
    print("Provincial scroll")

elif Total_time >= 111 :
    print("No award")