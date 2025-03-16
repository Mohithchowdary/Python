'''
2. Write programs to implement conditional operations on following:
   a. Python program to find the sum and average of natural numbers up to n where n is provided by the user.
   b. Python program to find factorial, and Fibonacci of a number, received by user, with iterative as well as recursive process.
'''

import os
from termcolor import colored

os.system('cls')
b, r, w = "cyan", "red", "white"

print(colored("Programs based on conditional operations", r) + "\n01. Sum and average of 'n' natural numbers.  \n02. Factorial of a positive number. \n03. Fibonacci Series")
action = input("Please specify the action you want to perform: ")
os.system('cls')

#a -------------------------
#sum using for loop
def sum_for(n):
   if n<0 or n==0:
       print(colored("cannot calculate the sum and average for negative numbers.", r))
  
   else:
       sum, i = 0, 1
       for i in range(i, n+1):
           sum = sum + i
           i = i+1
       return sum

#sum using while loop
def sum_while(n):
   if n<0 or n==0:
       print(colored("cannot calculate the sum and average for negative numbers.", r))
   else:
       sum, i = 0, 1
       while i<=n:
           sum = sum + i
           i = i+1
       return sum

#b -------------------------
#factorial iteration:
def fac_iter(n):
   if n<0:
       print(colored("factorial does not exist for negative numbers", r))
   elif n==0:
       return 1
   else:
    i, fac = 1, 1
    while i<=n:
       fac = fac*n
       n = n-1 #decremental order
    return fac

#factorial recursion:
def fac_rec(n):
   if n == 0 or n == 1 :
       return 1
   else :
       return n*(fac_rec(n-1)) #calls

#fibonacci iteration:
def fib_iter(n):
   a = 0
   b = 1
   if n == 0:
       return 0
   elif n == 1:
       return 1
   elif n < 0:
       print(colored("Please enter valid positive integers.", r))
   else:
       print(colored("\nFibonacci sequence upto ", r) + colored(n, w) + colored(" using iteration: ", r))
       print(a, end=' ')
       print(b, end=' ')
       for i in range(2,n):
           c = a + b
           a = b
           b = c
           print(c, end=' ')
          
#fibonacci recursion:
def fib_rec(n):
   print(colored("\n\nFibonacci sequence upto ", r) + colored(n, w) + colored(" using recursion:",r))
   def fib_rec(n):
       if n == 0:
           return 0
       elif n == 1:
           return 1
       elif n<0:
           print(colored("Please enter valid postive integers.", r))
       else:
           return fib_rec(n-2) + fib_rec(n-1)

   for i in range(n):
       print(fib_rec(i), end=' ')

#switch---------------------
if action == '1' or action == '01' :
   n = int(input("Please specify the number to perform the action: "))
   os.system('cls')
  
   print(colored("\nusing for-loop:", r) + "\nThe sum of the natural numbers upto " + colored(n, b) + " is " + colored(str(sum_for(n)), r)
   + "\nThe average of the sum of natural numbers upto " + colored(n, b) + " is " + colored(str(int(sum_for(n)/n)), r))

   print(colored("\nusing while-loop:", r) + "\nThe sum of the natural numbers upto " + colored(n,b) + " is " + colored(str(sum_while(n)), r)
   + "\nThe average of the sum of natural numbers upto " + colored(n, b) + " is " + colored(str(int(sum_while(n)/n)), r))
   print("\n")

elif action == '2' or action == '02' :
   n = int(input("Please specify the number: "))
   os.system('cls')
   print(colored("\nusing iteration:", r) + "\nThe factorial of the given number " + colored(n, b) + " is " + colored((fac_iter(n)), r))
   print(colored("\nusing recursion:", r) + "\nThe factorial of the given number " + colored(n, b) + " is " + colored((fac_rec(n)), r))
   print("\n")

elif action == '3' or action == '03' :
   n = int(input("Please specify the number: "))
   os.system('cls')
   fib_iter(n)
   fib_rec(n)
   print("\n")

else:
   print(colored("The action you're trying to perform is invalid. Please try again.", r))
   exit()
