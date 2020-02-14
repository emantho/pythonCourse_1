#1) Print
'''print('Hello World')
print('*' * 10)'''

#2) Variables
"""
price = 10 #this is a integer
rating = 4.9 # This is a float
first_name = 'Eder' # This is a string
is_published = False # This is a boolean > siempre inician con mayuscula (capital)
print(price)

#-- Excercise --
#Check a patient first_name first_named josn Smith, he´s 20 years old and is a new patient
first_name = 'John Smith'
age = 20
new_patient = True
"""

#3 Getting input
"""
first_name = input('What is your first_name: ') #recibe las entradas de teclado, puede llevar un mensaje
print('Hi ' + first_name)

#-- Excercise --
# Ask tow persons first_name and favourite color. Then, print a message like "Eder likes Red"
full_first_name = input('What is your first_name? ')
color = input('What is your favorite color? ')
print(full_first_name + "'s favorite color is " + color )
"""

#Type convertion
"""
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2019 - int(birth_year) # Is required to convert string to int, float or bool to make math operations
print(age)

# -- Excercise -- 
#Ask a user thir weight (in pounds), convert it to kilograms and print on the temrinal
init_weight = float(input('Whats is youe Weight (lbs): '))
total_weight = init_weight * 0.45
print('Your weight in Kg is: ' + str(total_weight))
"""

#Strings
"""
course = "Python's for beginners" # Double quotes are used for the apostrophe
# For print an multiline message we nust use (""" """) 
"""
"""
course2 = 
"""
"""
Hi Eder,
Here is our first email to you.
    Thank you.

The support team
"""
# For use index
"""
course3 = 'Python for beginners'
          #0123456 < This is the index position, begin in 0
          #1234567 < This is the space position, begin in 1
print(course3[1]) #this will print "y" for index 
print(course3[0:3]) # this will print pyt, for index 0 but space 
            #[start_index:end_index] 
course4 = 'Jennifer'
          #01234567
          #12345678
       #(-)87654321 < index en sentido contrario u orden negativo
print(course4[1:-1]) # This will print index 1 to minus 1 = ennife
"""

#Formatted Strings
"""
first = 'Eder'
last = 'Manjarres'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder' #Use of formatted strings, shorter and better organized
print(message)
print(msg)
"""

#StringMethods
"""
course = 'Python for beginners'
print(len(course)) #Use for count and is a general propose method
# course.capitalize > It's posible use many others methods like lower, upper etc
course2 = course.replace('beginners', 'Absolute beginners') # Replace string inside string
print(course2)
print('Python' in course) # IN operator produce a boolean value
"""

#Arithmetic Operations
"""
print(2 + 3) # Addition
print(2 - 3) # 
print(2 * 3) #Multiplication
print(2 / 3) # Divition
print(2 // 3) # Divition, return int
print(2 % 3) # Module, return reminder of divition
print(2 ** 3) # exponential o power
x = 10
x += 3 # is the same as x = x + 3. It´s posible do it with -=, *=, /= and so on
print(x)
"""

# operations precendent
"""
exponentiation 2**3
multiplication or division
addition or sustraction
"""

# Math function
"""
import math # This make available all math bibliotec

x = 2.9
print(round(x))
print(abs(x))

print(math.ceil(2.9))
"""

# If Statements
'''if it´s hot
    It´s a hot day
    Drink plenty of water
Otherwise if it´s cold
    it´s a cold day
    waer warm clothes
oherwise
    it´s a lovely day

hot_day = False
cold_day = False

if hot_day == True:
    print('It´s a Hot day, drink plenty of water' )
elif cold_day == True:
    print('It´s a Cold day, wear warm clothes')
else:
    print('It´s a lovely day')'''

# Excercise
""" Price house is $1M
    if buyer has GOOD CREDIT
        they need to put down 10%
    otherwise
        they need to put down 20%
    print the down payment

price = 1000000
buyer_good = True
if buyer_good:
    down_pay = price * .1
else:
    down_pay = 1000000 * .2
    
print(f'Down payment is: ${down_pay}')
'''
# Logicals Operators
'''
#If aplicant has high income AND good credit, is elegible for loan
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit: #AND can be repaced for OR, in this case if will be valid only wheter one conditions is true
    print('Elegible for loan')

else:
    print('Not elegible for loan')
"""
# AND: both; OR: at least one; NOT: invert the condition TRUE on FALSE 

# Comparisons operators
'''
    # If tempperature is greater than 30 > it's a hot day
    # otherwise if it´s less than 30 > it's a cold day
    # otherwise it's neither hot or cold

temp = 29
if temp >= 30:
    print("It's a hot day")
elif temp <= 30:
    print("It's a cold day")
else:
    print("It's a lovely day")
'''
# >=, <=, ==, !=

# Excercise
"""
if first_name is less than 3 characters long
    first_name must be at least  characters
otherwise if it´s more than 50 characters long 
    first_name must be a maximum of 50 characters
otherwise
    first_name looks good

full_first_name = input('Please enter your full first_name: ')
if len(full_first_name) < 3:
    print('first_name must be at least 3 characters')
elif len(full_first_name) >= 50:
     print('first_name can be maximum of 50 characters')
else:
    print('first_name looks good')
"""

# Project: Weight Converter
"""
#Ask for weight and then ask for convert into L or K
weight = float(input('What is your weight: '))
unit = input('Convert into (L)bs or (K)g: ')

if unit.lower() == "l":
    weight = weight * 0.45
    
elif unit.lower() == "k":
    weight = weight / 0.45
    
print(weight)
"""

# While loops
'''
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print('done')
'''
# Guessing Game > build a guessing game 3 times to find a number (9) shows "You win!" else "you lose"
'''
i = 0
while i < 3: # times to excecute limited to 3 
    i += 1
    number = int(input('Enter a number: '))
    if number == 9:
        print('You win!!')
        break
    # print(i)
    # print('Try again!!')
    # print()
else:
    print('GAME OVER')
'''

# Car Game > 
'''commands = """Welcome to this game, this is the command list:
start = Start the car
stop = Stop de car
quit = Exit the game
"""

print(commands)
action = ''
started = False
stoped = False
while True: # Will excecute until find a break
    action = input('Enter an action: ').lower()

    if action == 'start':
        if started:
            print('Car is already started')
        else:
            print('Starting the car')
            started = True
    
    elif action == 'stop':
        if started == False:
            print('Car is alredy stopped')
        else:
            print('Stoping the car')
            started = False

    elif action == 'quit': # This action will finish the loop
        break

    else:
        #action != 'start' or action != 'stop' or action != 'quit'
        print("Sorry i don't undesrstand" )

print('GAME OVER')'''

# For Loops
"""
for item in ['Eder', 'Diana', 'Emilia']: #itering from a list limited of item
    print(item)

for item in range (0, 10, 2): #will iterate from 0 to 10 by 2 steps #range(5, 10):will iterate from 5 to 10 range(10) > will iterate 10 times
    print(item)
Excercise > Print all prices
prices = [10, 20, 30]
cost = ''
total = 0
i = 0
for price in prices:
    print(f'item {i} cost {price}')
    i += 1
    total += price
print(f'Total: {total}')
"""

# Nested Loops

'''for x in range(4):
    for y in range(3):
        print(f"{x}, {y}")'''

# Excercise > print a letter F using 'x' in a list

'''numbers = [5,2,5,2,2]
for i in numbers:
    print('X' * i) '''

#List

'''first_name = ['Eder', 'Diana', 'Emilia', 'Luciana','Jeronimo']
print(first_name) # Print all items
print(first_name[2:4]) # print item from index 3 to 4 > no modify
first_name[0] = 'Emilio' # Modify the list
print(first_name)'''

# Write a program to find the largest number in a list

'''prices = [1, 3 , 5, 7 , 10, 4, 0]
largets = prices[0]
for i in prices:
    if i > largets:
        largets = i
print(largets)'''

# 2D List > Bulding a Matrix
'''matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix) # This will print all the matrix
print(matrix[0]) # this will print only the first row
print(matrix[1][2]) # This will print the index 2 of row 1'''

# List Methods

'''numbers = [5, 6, 7, 8, 10, 0, 50, 8]
numbers.append(1) # Add an item to the final / Ajouter un element a la fin
print(numbers)
numbers.insert(0, 15) # Add an item in the position indicate / Ajouter un element a la position indiquee
print(numbers)
numbers.remove(10) # Erase item (value) indicate
print(numbers)
numbers.pop() # Erase index selected or default the last item
print(numbers) 
print(numbers.index(8)) # Print index of value, if it is finded
print(6 in numbers) # boolean answer for the value searched
print(numbers.count(8)) # Quantity of value repeated
print(numbers.sort()) # Returns none 
numbers.sort()
print(numbers) # Order ascending
numbers.reverse()
print(numbers) # Order descending
numbers2 = numbers.copy()
numbers.append(99)
print(numbers) # Order descending
print(numbers2) # Order descending
numbers.clear() # Erase all items in list
print(numbers)

# Exercise > Write a program to remove the duplicate in a list

numbers = [5, 6, 7, 8, 10, 0, 50, 8] # List whit repeated numbers
uniques = [] # List to copy no repeated numbers
for number in numbers: # iterate in general list
    if number not in uniques: # Search for NOT repeated numbers only
        uniques.append(number) # Add if condition is true
print(uniques)
'''
# Tuples > cannot muted or modified, are usefull when dont want some modify list

'''number = (1, 2, 3) # Only can use method count and index
print(number[0])'''

# Unpacking
'''coordinates = (1, 2, 3) # Can be used whit list too
x, y, z = coordinates
print(x)
print(y)
print(z)'''

# Dictionaries
'''customer = {
    'first_name': 'Eder Manjarres',
    'age': 33,
    'is_verified': True
}
customer['first_name'] = 'Diana Pinzon'
customer['birthdate'] = 'Dic 12 1985'
print(customer)'''

#Excercise > Phone number in "int" converto to "string"
'''phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + ":"
print(output)
'''

# Others example dicctionaries 
'''message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😀",
    ":(": "😥"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)'''


# -_-_-_- Functions _-_-_-
'''
def greet_user():
    print('hi there')
    print('Welcome aboard')


print('start')
greet_user()
print('Finish')'''

# Functions with Parameters
'''def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('start')
greet_user('Eder', 'Manjarres')
greet_user('Diana', 'Pinzon')
print('Finish')
'''
# Keywords Arguments
'''def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('start')
greet_user(last_name = 'Manjarres', first_name = 'Eder') 
greet_user('Diana', last_name = 'Pinzon')
print('Finish')'''

# Return Statement
'''def square(number):
    return number * number

result = square(float(input('> '))) # can be printed directly 
print(result)

'''

# Reusable function
'''def emojis_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😥"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")

print(emojis_converter(message))'''

# Exceptions
'''try: 
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("invalid Value")
'''
# Clases
'''class Point:  #the classes begin with capital letter
    def _init__(self, x, y):
        self.x = x
        self.y = y

    def move(self): # Never a function inside a class would be empty, instead use "self"
        print("move")
    
    def draw(self):
        print("draw")


point = Point(10, 50)
print(point.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("john Smith")
john.talk()

nombre = input("")
nombre = Person(nombre)
nombre.talk()'''

# Inheritance
'''class Mammal: # Mother class who give functions to sons or others class to no repeat this
    def walk(self):
        print("walk")

class Dog(Mammal): # Son's class that receives the functions 
    def bark(self):
        print("Bark")

class Rat(Mammal):
    pass # this is necessary for no leave an empty class

class Cat(Mammal):
    def be_annoying(self):
        print("Annoying")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()'''

# Modules
# Function moves to a new file name converters.py
'''def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45

import converters # We can import the module converters with all his functions
print(converters.kg_to_lbs(70))

import kg_to_lbs from converters
from converters import lbs_to_kg'''

from utils import find_max
items = [3,1,6,9,4,6]
print(find_max(items))