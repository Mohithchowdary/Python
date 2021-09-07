'''Write Python program:
    a. Implement python script to show the usage of various operators available in python
    b. Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs. 12.00 per hour for every hour worked above 40 hours. Assume that employee do not work for fractional part of an hour.
'''

import os, time
from termcolor import colored

a,b = 5,4 
r = 'red'

os.system('cls')
print(colored("Python Programs:", r) + """
01. Usage of various python operators.
02. Overtime pay of 10 employees.
03. Exit""")

#a. python operators --------
def arthimetic(): # +, -, *, /, %, **, //
    print(colored('01. Arthimetic Operators:', r))

    add = a+b
    sub = a-b
    div = a/b
    mul = a*b
    mod = a%b
    expo = a**2
    fld = a//b

    print(
    ' a = ' + str(a) + ',' + ' b = ' + str(b),
    '\n\n addition (+): ' + str(add),
    '\n subtraction(-): ' + str(sub),
    '\n division (/): ' + str(div),
    '\n multiplication (*): ' +  str(mul),
    '\n modulus (%): ' + str(mod),
    '\n exponential (**): ' + str(expo),
    '\n floor division (//): ' + str(fld),
    )

def assignment(): # +=, -=, *-, /=, %=, **=, //=, |=, ^=, >>=, <<= 
    a,b = 5,4
    print(colored('\n02. Assignment Operators:', r),
    '\n a = ' + str(a) + ',' + ' b = ' + str(b) + '\n')
    
    a,b = 5,4
    a += b
    print(' a += b: ' + str(a))
    
    a,b = 5,4 
    a -= b
    print(' a -= b: ' + str(a))
    
    a,b = 5,4 
    a *= b
    print(' a *= b: ' + str(a))
    
    a,b = 5,4 
    a /= b
    print(' a /= b: ' + str(a))
    
    a,b = 5,4 
    a %= b
    print(' a %= b: ' + str(a))
    
    a,b = 5,4 
    a //= b
    print(' a //= b: ' + str(a))
    
    a,b = 5,4   
    a **= b
    print(' a **= b: ' + str(a))
    
    a,b = 5,4 
    a |= b
    print(' a |= b: ' + str(a))

    a,b = 5,4 
    a ^= b
    print(' a ^= b: ' + str(a))
    a >>= b

    a,b = 5,4 
    print(' a >>= b: ' + str(a))
    
    a,b = 5,4 
    a <<= b
    print(' a <<= b: ' + str(a))

def comparison(): # ==, !=, >, <, >=, <=
    print(colored('\n03. Comparison Operators: ', r))
    equal_to = bool(a==b)
    not_equal = bool(a!=b)
    greater_than = bool(a>b)
    less_than = bool(a<b)
    greater_equal = bool(a>=b)
    less_equal = bool(a<=b)

    print(
    ' a = ' + str(a) + ',' + ' b = ' + str(b),
    '\n\n equal_to (==): ' + str(equal_to),
    '\n not_equal (!=): ' + str(not_equal),
    '\n greater_than (>): ' + str(greater_than),
    '\n less_than: (<)' + str(less_than),
    '\n greater_equal (>=): ' + str(greater_equal),
    '\n less_equal: (<=)' + str(less_equal)
    )

def logical(): #and, or, not
    print(colored('\n04. Logical Operators:', r))

    and_ = bool((a == 5) and (b > 4))
    or_ = bool((a == 5) or (b == 5))
    not_ = bool(not(a == 10) and (b == 10))

    print(
    ' a = ' + str(a) + ',' + ' b = ' + str(b),
    '\n\n and: ' + str(and_),
    '\n or: ' + str(or_),
    '\n not: ' + str(not_)
    )

def identity(): #is, is not - compares the locations
    print(colored('\n05. Identity Operators:', r))
    print(' Memory location of a: ' + str(id(a)) + '\n Memory location of b: ' + str(id(b)))
    print('\n is: ' + str(bool(a is b)))
    print(' is not: ' + str(bool(a is not b)))

def membership(): #in, not in
    
    names = ['Mohith', 'Anonimo', 'Siri', 'Iris']

    print(colored('\n06. Membership Operators: ', r) + ' \n names = ' + str(names))
    print('\n Mohith (in) names: ' + str('Mohith' in names))
    print(' Iris (not in) names: ' + str('Iris' not in names))

def bitwise(): #&, |, ^, ~, <<, >> - Binary comparision
    print(colored('\n07. Bitwise Operators: ', r))

    AND = a&b
    OR = a|b
    XOR = a^b
    NOT = ~a
    left_shift = a<<b
    right_shift = a>>b

    print(
    ' a = ' + str(a) + ',' + ' b = ' + str(b),
    '\n\n AND (&): ' + str(AND),
    '\n OR (|): ' + str(OR),
    '\n XOR (^): ' + str(XOR),
    '\n NOT (~): ' +  str(NOT),
    '\n left_shift (<<): ' + str(left_shift),
    '\n right_shift (>>): ' + str(right_shift),
    '\n\n\n'
    )
    
#b. overtime pay of 10 employees --------
def overtime_pay():
    employees, payout = 10, 0
    for i in range(1, employees+1):
        work_hours = int(input(f"{colored(i, r)}. Please specify the work time of the employee (in hours): "))
        if work_hours > 40:
            sal = (work_hours-40)*12.00
            payout += sal
            print(f"Paid: {colored(sal, r)} Rs/- for additional {colored(work_hours-40, r)} working hours.")
            time.sleep(1.5)
            os.system("cls")
        elif work_hours <= 40: 
            print(colored("didn't meet our minimum requirements. Must be greater than 40 working hours.", r))
            time.sleep(1.5)
            os.system("cls")
        else: 
            print(colored("Something went wrong please try again.", r))

    os.system('cls')
    print(colored("Overall Overtime pay of all the ", r) + str(employees) + colored(" employees is: ", r) + str(payout) + " Rs/-")

#switch---------------------
def switch(): 
    action = input('\nPlease specify the action you want to perform: ') 
    if action == '01' or action == '1':
        os.system('cls')
        print("Python Operators:\n")
        arthimetic()
        assignment()
        comparison()
        logical()
        identity()
        membership()
        bitwise()

    elif action == '02' or action == '2':
        os.system("cls")
        print(colored('Overtime Pay: \n', r))
        overtime_pay()
    elif action == "00" or action == "0":
        exit()
    else:
        print(colored("The action you're trying to perform doesn't exist. Please try again later.", r))
switch()
