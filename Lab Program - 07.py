'''
Write python program to show following plots using Matplotlib library.
    1. To read total profit of all months and show it using a line plot where 
        . x axis should be month number
        . y axis should be named as total profit.
    
    2. To get total profit of all months and show line plot with the following style properties:
        . Line Style dotted and Line-color should be red.
        . Show legend at the lower right location.
        . X label name = Month Number.
        . Y label name = Sold units number.
        . Add a circle marker.
        . Line marker color as red.
        . Line width should be 3.
'''



import os
from numpy import arctan
import pandas as pd
import matplotlib.pyplot as plt  

data = pd.read_csv("company_sales_data.csv")

#a. To read the total profit of all months and display the plotted graph.
def all_months():
    profitList = data ['total_profit'].tolist()
    monthList  = data ['month_number'].tolist()
    plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
    
    # x-axis = Month number
    plt.xlabel('Month number')

    # y-axis = total profit
    plt.ylabel('total profit')
    
    plt.xticks(monthList)
    plt.title('Company profit per month')
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()

#b. To get the total profit of all_months with specified properties and display the plotted graph.
def all_properties():
    print("2")
    profitList = data ['total_profit'].tolist()
    monthList  = data ['month_number'].tolist()

    # X label name = Month Number
    plt.xlabel('Month Number')

    # Y label name = Sold units number
    plt.ylabel('Sold units number')

    #add a circle marker with width 3 and color red.
    plt.plot(monthList, profitList, 
        label = 'Profit data of last year', 
        color='r', marker='o', markerfacecolor='k', 
        linestyle='--', linewidth=3)
      
    plt.legend(loc='lower right')
    plt.title('Company sales data of last year')
    plt.show()

os.system('cls')

print('''Write python program to show following plots using Matplotlib library.
    1. To read total profit of all months and show it using a line plot where 
        . x axis should be month number
        . y axis should be named as total profit.
    
    2. To get total profit of all months and show line plot with the following style properties:
        . Line Style dotted and Line-color should be red.
        . Show legend at the lower right location.
        . X label name = Month Number.
        . Y label name = Sold units number.
        . Add a circle marker.
        . Line marker color as red.
        . Line width should be 3.
''')

action = input('Please specify the action you want to perform: ')

match action:
    case '01' | '1':
        all_months()
        os.system('cls')
    case '02' | '2':
        all_properties()
        os.system('cls')
    case _:
        os.system('cls')
        print("The action you're trying to perform is invalid.")
