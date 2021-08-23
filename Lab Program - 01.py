"""
1. Write programs to implement the following operations:
   a. To elaborate variables and their data types such as int, float, boolean, string, list, set, dictionary and tuples; swap two numbers.
   b. To perform mathematical operations such as addition, subtraction, multiplication, division, modulo, and power; also explore the operator precedence.
"""

import os

#a
a, b = "5", "4"
f = float("10.854")
list = ["19BTRCY054", "Mohith", "21",]
set = {"1", "2", "3", "a" , "bc"}
tuple = ("054", "19BTR", "2000")
dict = {"Name":"Mohith", "USN":"19BTRCY054"}

os.system('cls')

print(
 "\n int:", int((f)), type(int(f)), id(f), "\n",
 "float:", f, type(f), id(f), "\n",
 "string:", a, type(a), id(a), "\n",
 "boolean:", bool(a==b), type(bool(a==b)), id(bool(a==b)), "\n",
 "list:", list, type(list), id(list), "\n",
 "set:",set, type(set), id(set), "\n",
 "tuple:", tuple, type(tuple), id(tuple), "\n",
 "dict:", dict, type(dict), id(dict), "\n",
  sep=" ", end="\n -------------"
)

print("\n** Swapping **\nBefore swap: " + a, b)
a,b = b,a
print("After swap: {0}, {1}" .format(a, b), end="\n\n -------------")

#b
print("\n** Arthimetic Operations **")
a,b = 5,4 
add = a+b
sub = a-b
div = a/b
mul = a*b
mod = a%b
expo = a**2
fld = a//b

print(
    " addition: " + str(add) + "\n",
    "subtraction: " + str(sub) + "\n",
    "division: " + str(div) + "\n",
    "multiplication: " +  str(mul) + "\n",
    "modulus: " + str(mod) + "\n",
    "exponential: " + str(expo) + "\n",
    "floor division: " + str(fld) + "\n",
    "\nA code by Mohith Chowdary | 19BTRCY054"
)
