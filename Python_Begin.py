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


