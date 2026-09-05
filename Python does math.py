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

hello = input("Press Enter to continue to the next exercise...")
print('Exercise 2: Find the value of x = 20 - 40')
print('What is the value of x?')
print('Type your answer below and press Enter.')
answer = input()
wait = input("Press Enter to see the answer...")

#function definition
def find_x_2():
    x = 20 - 40
    print("The value of x is:", x)
#function call
find_x_2()

hello = input("Press Enter to continue to the next exercise...")
print('Exercise 3: Find the value of x = 5 * 9')
print('What is the value of x?')
print('Type your answer below and press Enter.')
answer = input()
wait = input("Press Enter to see the answer...")

#function definition
def find_x_3():
    x = 5 * 9
    print("The value of x is:", x)
#function call
find_x_3()


hello = input("Press Enter to continue to the next exercise...")
print('Exercise 4: Find the value of x = 100 / 0')
print('What is the value of x?')
print('Type your answer below and press Enter.')
answer = input()
wait = input("Press Enter to see the answer...")

#function definition
def find_x_4():
    x = 100 / 0
    print("The value of x is:", x)
#function call
find_x_4()