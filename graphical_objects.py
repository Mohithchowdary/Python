import os
import matplotlib.pyplot as plt

def a():
    rect=plt.Rectangle((0,0),200,200,fc='r')
    plt.gca().add_patch(rect)

    rect=plt.Rectangle((50,50),100,100,fc='w')
    plt.gca().add_patch(rect)

    rect=plt.Rectangle((75,75),50,50,fc='r')
    plt.gca().add_patch(rect)

    plt.axis('scaled')
    plt.show()

def b():
    plt.figure()
    plt.axis([0,25,25,0])
    curr=plt.gca()
    for i in range(0,5):
        for j in range(0,5):
            if ((i+j)%2==0):
                curr.add_patch(plt.Rectangle((i*5,j*5),5,5,color='white'))
            else:
                curr.add_patch(plt.Rectangle((i*5,j*5),5,5,color='black'))
    plt.show()

os.system('cls')
print("python programs for following graphical objects:",
    "\n   01. A set of concentric squares, alternating red and white in a graphics window, that is, 200 pixels wide by 200 pixels high.",
    "\n   02. To create a 5x5 rectangle whose top left corner is at (row*5, col*5)."
)

action = input("\nPlease specify the action you want to perform: ")

match action:
    case "1" | "01":
        a()
    case "2" | "02":
        b()
    case _:
        print("The action you're trying to perform does not exist.")
