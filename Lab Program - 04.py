'''
Write a python program to:
    a. Elaborate string operations such as string declaration, traversing, slicing, concatenating, and sorting.
    b. Implement a python script to check if the element is the list or not by using linear search or binary search.
    c. Implement a python script to arrange the elements in sorted order using Bubble, Selection, Insertion and Merge sorting techniques.
'''

import os, time
os.system("cls")

#4a. String declaration, traversing, slicing, concatenating, and sorting.
def working_with_strings():
    #string-declaration (using assignment ops)
    name = 'Mohith Chowdary' #single-quotes
    headline = "An explorer with creative and technical skills." #double-quotes
    description ='''
    I'm a 21 year old, self-taught graphic designer and video editor based in India. 
    I am also into development side currently pursuing degree in computer science engineering.'''

    #string-concatenation (string1 + string2)
    print("\nString-declaration and string-concatenation:\n" +
          " Name: " + name,
          "\n Headline: " + headline,
          "\n Description: ", description)

    #string-slicing [start:stop:step]
    slice_n = name[0:6] #normal
    slice_r = name[::-1] #inverse
    print("\nslicing: \n slice[0:6]: " + slice_n + "\n slice[::-1]: " + slice_r)

    #string-traversing
    print("\nString traversing:")
    for index in range(len(name)-1):
        print(index , end="  ")
    print("")
    for i in range(len(name)):
        print(name[i], end="  ")
    print("")

    #string-sorting
    print("\n\nString sorting:")
    print("before: ", name)
    print("after: ","".join(sorted(name)))

#4b. To check whether the element is present in the list using binary and linear search.
#Linear Search
def linear_search(list, value): 
    for index in range(0, len(list)-1):
        if list[index] == value:
            return index
    else:
        return -1

#Binary Search
def binary_search(list, value): 
    list = sorted(list)
    begin_index = 0
    end_index = len(list)-1

    while begin_index <= end_index:
        midpoint_index = (begin_index + end_index)//2
        if list[midpoint_index] == value:
            return midpoint_index
        
        elif list[midpoint_index] > value:
            end_index = midpoint_index - 1            
        
        elif list[midpoint_index] < value:
            begin_index = midpoint_index + 1
    return -1

#4c. Bubble, Selection, Insertion and Merge sort techniques.
#bubble-sort
def bubble_sort(): 
    sorted = False
    while not sorted:
        sorted = True
        for index_value in range(0, len-1):
            if list[index_value] > list[index_value+1]:
                list[index_value], list[index_value+1] = list[index_value+1], list[index_value]
                sorted = False
    return list

#selection-sort
def selection_sort(): 
    for index_value in range(0, len-1):
        min_value = index_value

        for x in range(index_value+1, len):
            if list[x] < min_value:
                min_value = x

        if min_value != index_value:
            list[min_value], list[index_value] = list[index_value], list[min_value]
    return list

#insertion-sort
def insertion_sort():
    for index_value in range(1, len-1):
        min_value = list[index_value]

        while list[index_value-1] > min_value and index_value > 0:
            list[index_value-1], list[index_value] = list[index_value], list[index_value-1]
    return list
        
#merge-sort
def merge_sort():
    left_arr = list[:len//2]
    right_arr = list[len//2:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i, j, k = 0, 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            list[k] = left_arr[i]
            i +=1
        else:
            list[k] = right_arr[j]
            j +=1
        k += 1

    while i < len(left_arr):
        list[k] = left_arr[j]
        i += 1
        k += 1

    while j < len(right_arr):
        list[k] = right_arr[j]
        j += 1
        k += 1

    return list

#switch_case #3.10 -- update
print(""" 
Python Programs:
    01. Working with Strings such as String declaration, traversing, slicing, concatenating and sorting.
    02. Search an element in a list by using Linear & Binary search algorithms.
    03. Sorting a list using Bubble, Selection, Insertion, and Merge sort techniques.
    """)
action = input("Please specify the action you want to perform: ")
os.system("cls")
match action:
    case "1" | "01": #4a
        working_with_strings() 

    case "2" | "02": #4b
        list = []
        elements = int(input("Please specify the no. of elements you want to enter: "))

        for i in range(1, elements+1):
            x = int(input(f"{i}. Element: "))
            list.append(x)

        value = int(input("Please specify the element you want to search: "))
        os.system("cls")
        print("\nLinear Search: \n- Index and elements - (user specified order.)")
        for i in range(0, len(list)):
            print(i, end=" ")
        print("")
        for i in range(0, len(list)):
            print(list[i], end = " ")
        print("\n")

        if linear_search(list, value) == -1:
            print(f"Linear Search:  The value '{value}' you're looking for isn't available.")
        else:
            print(f"Linear Search:The value '{value}' you're looking for is found at {linear_search(list, value)} index.")        

        print("\nBinary Search: \n- Index and elements - (Sorted in increasing order before finding the element in the list)")
        for i in range(0, len(list)):
            print(i, end=" ")
        print("")
        for i in range(0, len(list)):
            print(list[i], end = " ")
        print("\n")

        if binary_search(list, value) == -1:
            print(f"Binary Search: The value '{value}' you're looking for isn't available.")
        else:
            print(f"Binary Search: The value '{value}' you're looking for is found at {binary_search(list, value)} index.")
        print("")

    case "3" | "03": #4c
        list = []
        elements = int(input("Please specify the no. of elements you want to enter: "))

        for i in range(1, elements+1):
            x = int(input(f"{i}. Element: "))
            list.append(x)

        len = len(list)
        os.system("cls")
        print("\nbefort_sorting: \n   list =", list)
        print("\nafter_sorting:")
        print("   bubble_sort    =", bubble_sort())
        print("   selection_sort =", selection_sort())
        print("   insertion_sort =", insertion_sort())
        print("   merge_sort     =", insertion_sort())
        print("")

    case _:
        print("The action you're trying to perform does not exist. Please try again choosing the right action.")
