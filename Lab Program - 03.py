""" 
Write python programs
      a. To print all prime numbers between N to M.
      b. To find the largest among three numbers, input by user.
      c. To find GCD two numbers, input by user.    
"""      

import os, time
from termcolor import colored

os.system("cls")
print(colored("Basic Python Programs:\n", "red") +
      "01. To print the prime numbers between specific intervals. (N to M)  \n"
      "02. Largest among the specified three numbers. \n"
      "03. Greatest common divisor (GCD) using while loop and recursion. \n"
      "00. Exit \n")

action = input("Please specify the action you want to perform: ")
os.system("cls")

#a -------------------------
#To print the prime numbers between specified intervals.
def prime_interval():
    n = int(input("Please specify the limit you want to print the prime numbers from: "))
    m = int(input("Please specify the limit you want to print the prime numbers upto: "))
    print("\nThe prime numbers between " + colored(str(n), "cyan") + " to " + colored(str(m), "cyan") + " are:")

    for prime in range(n, m+1):
        if prime > 1 :
            for i in range(2, prime):
                if prime%i == 0:
                    break
            else:
                print(colored(prime, "red") , end=" ")

        elif n<=1 or m<=1:
            print("Err: The number you specified is less than 1.")
            break

#b -------------------------
#Largest among the specified three numbers.
def largest_number():
    x = int(input("Please specify the first number: "))
    y = int(input("Please specify the second number to compare: "))
    z = int(input("Please specify the third number to compare: "))

    if x==y or y==z or z==x:
        print("can't compare two equal numbers")
    else:
        if x>y and x>z:
            print("\nThe largest among the given three numbers " + colored(x, "cyan") + " , " + colored(y, "cyan") + " and " + colored(z, "cyan") + " is: " + colored(x, "red") + " \n ")
        elif y>x and y>z:
            print("\nThe largest among the given three numbers " + colored(x, "cyan") + " , " + colored(y, "cyan") + " and " + colored(z, "cyan") + " is: " + colored(y, "red") + " \n ")
        else:
            print("\nThe largest among the given three numbers " + colored(x, "cyan") + " , " + colored(y, "cyan") + " and " + colored(z, "cyan") + " is: " + colored(z, "red") + " \n ")

#c -------------------------
#Greatest common divisor using while loop.
def GCD(x, y):
    while y != 0:
        x, y = y, x%y
    return x

#Greatest common divisor using recursion.
def GCD_rec(x, y):
    if y == 0:
        return x
    else:
       return GCD(y, x%y)

#switch---------------------
def switch():
    if action == "1" or action == "01" :
        os.system("cls")
        prime_interval()

    elif action == "2" or action == "02" :
        os.system("cls")
        largest_number()

    elif action == "3" or action == "03" :
        os.system("cls")
        x = int(input("Please specify the first number: "))
        y = int(input("Please specify the second number to compare: "))
        os.system("cls")
        print("" + colored("\nUsing While-loop:\n", "red") + "The GCD of the two numbers " + colored(x, 'cyan') + " and " + colored(y, 'cyan') + " is " + colored(GCD_rec(x, y), 'red'))
        print(colored("\nUsing recursion:\n", "red") + "The GCD of the two numbers " + colored(x, 'cyan') + " and " + colored(y, 'cyan') + " is " + colored(GCD_rec(x, y), 'red') + " \n ")

    elif action == "0" or action == "00" :
        os.system("cls")
        print(colored("Terminated", "red"))
        time.sleep(0.5)
        os.system("cls")
        exit()

    else:
        print(colored("The action you're trying to perform is invalid. Please try again later.", "red"))
switch()
