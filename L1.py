from datetime import datetime
datetime.now()
from datetime import datetime, timezone, timedelta
gmt7 = timezone(timedelta(hours=7))
now = datetime.now(gmt7)
print("Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S %Z%z"))

print("Hello, World!")
print("This is a simple Python program.")
print("Let's do math with Python.")
print('You have 4 exercises to complete.')
print('Exercise 1: Find the value of x = 1 + 1')
print('What is the value of x?')
print('Type your answer below and press Enter.')
answer = input()

wait = input("Press Enter to see the answer...")


#function definition
def find_x_1():
    x = 1 + 1
    print("The value of x is:", x)
#function call
find_x_1()