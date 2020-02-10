# #1) Print
# print('Hello World')
# print('*' * 10)

#2) Variables
"""
price = 10 #this is a integer
rating = 4.9 # This is a float
name = 'Eder' # This is a string
is_published = False # This is a boolean > siempre inician con mayuscula (capital)
print(price)

#-- Excercise --
#Check a patient name named josn Smith, he´s 20 years old and is a new patient
name = 'John Smith'
age = 20
new_patient = True
"""

#3 Getting input
"""
name = input('What is your name: ') #recibe las entradas de teclado, puede llevar un mensaje
print('Hi ' + name)

#-- Excercise --
# Ask tow persons name and favourite color. Then, print a message like "Eder likes Red"
full_name = input('What is your name? ')
color = input('What is your favorite color? ')
print(full_name + "'s favorite color is " + color )
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
    print('It´s a lovely day')

# Excercise
""" Price house is $1M
    if buyer has GOOD CREDIT
        they need to put down 10%
    otherwise
        they need to put down 20%
    print the down payment
"""
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

# AND: both; OR: at least one; NOT: invert the condition TRUE on FALSE 
'''

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

# >=, <=, ==, !=

# Excercise
"""
if name is less than 3 characters long
    name must be at least  characters
otherwise if it´s more than 50 characters long 
    name must be a maximum of 50 characters
otherwise
    name looks good
"""
full_name = input('Please enter your full name: ')
if len(full_name) < 3:
    print('Name must be at least 3 characters')
elif len(full_name) >= 50:
     print('Name can be maximum of 50 characters')
else:
    print('Name looks good')
'''

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
commands = """Welcome to this game, this is the command list:
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

print('GAME OVER')




"""
#Ejercicio general - Agenda contactos
nombre = input('ingrese su nombre completo: ')
fecha_nac = input('Ingrese su fecha de nacimiento (dd/mm/aaaa): ')
num_celular = input('Ingrese su número de celular: ')

msg = f'{nombre} nació el {fecha_nac} y su número de telefono es: {num_celular}'
print(msg)
for nom in nombre:
    print(nombre)
    for fec in fecha_nac:
        print(fecha_nac)
        for num in num_celular:
            print(num_celular)
"""


