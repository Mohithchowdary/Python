'''
6. Write Python programs using NumPy and Pandas:
    a. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
    b. To create a 4x2 integer array and prints its attributes.
    c. For the given numpy array return array of odd rows and even columns.
    d. To add the two NumPy arrays and modify a result array by calculating the square root of each element.
'''

import os
import pandas as pd
import numpy as np

#a. Display a DataFrame from a specified dictionary data which has the index labels.
def DataFrame():
    data = {
        "Name": ["Mohith", "Iris", "Anonimo", "Siri", "Spoorthi"],
        "USN": ["19BTRCY054", "19BTRCX034","19BTRCY041","19BTRCE005","19BTRSE021", ],
        "Gender": ["Male", "Female", "Male", "Female", "Female"],
        "Program": ["B.Tech"],
        "Percentage":[82, 91, 99, 88, 79]
    }

    print(
        "data = {\n"
          "        Name: ", data["Name"], "\n",
          "         USN: ", data["USN"], '\n',
          "      Gender: ", data["Gender"], "\n",
          "     Program: ", data["Program"], "\n",
          "  Percentage: ", data["Percentage"], "\n",
          "}"
        )

    serial_no = []
    for i in range(len(data["Name"])):
        serial_no.append(i+1)

    print("\nDataFrame using Pandas:\n" , pd.DataFrame(data, index=serial_no))
    print()

#b. To create a 4x2 integer array and prints its attributes.
def intarray_4x2():
    print("4x2 Integer array using NumPy:\n", np.empty([4,2], dtype=np.int8))
    print()

#c. For the given numpy array return array of odd rows and even columns.
def oddr_evenc():
    array = np.array([[1, 2, 3, 4, 5],
                      [6, 8, 7, 2, 9],
                      [3, 6, 8, 4, 1],
                      [1, 5, 0, 4, 2]])

    print("array: \n", array)
    print("\nodd rows from the array:")
    print(array[1::2])
    print("\neven coloumns from the array:")
    print(array[:, 1::2])
    print()
    
#d. To add the two NumPy arrays and modify a result array by calculating the square root of each element.
def add_sqrt():
    array_a = np.array([[1, 2, 3, 4, 5],
                        [6, 8, 7, 2, 9],
                        [3, 6, 8, 4, 1],
                        [1, 5, 0, 4, 2]])

    array_b = np.array([[2, 4, 6, 8, 3],
                        [3, 4, 3, 1, 6],
                        [7, 9, 5, 3, 2],
                        [0, 5, 2, 7, 4]])

    print("array_a: \n", array_a, "\n")
    print("array_b: \n", array_b, "\n")
    print("addition of two NumPy arrays (array_a + array_b): \n", array_a + array_b, "\n")
    print("square_root of each element in the array using NumPy: \n", np.int0(np.sqrt(array_a + array_b)), "\n")

    
os.system("cls")

#prompt_menu
print('''
Python program using NumPy and Pandas:
    01. Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
    02. To create a 4X2 integer array and prints its attributes.
    03. For the given NumPy array return array of odd rows and even columns.
    04. To add the two NumPy arrays and modify a result array by calculating the square root of each element.
''')

action = input("Please specify the action you want to perform: ")

os.system("cls")

#match-case 3.10 --update
match action:
    case "1" | "01":     
        DataFrame()
    case "2" | "02":
        intarray_4x2()
    case "3" | "03":
        oddr_evenc()
    case "4" | "04":
        add_sqrt()
    case _:
        print("The action you're trying to perform does not exist. Please try again choosing the right action.")
