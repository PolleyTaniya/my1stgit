

import tkinter
from graphics import Canvas
import random


    
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    #describing the game with graphics
    
    print("FIRST YOU CHOOSE A DOOR")
    print()
    print("WE WILL OPEN A DOOR WHICH ONE HAS A GOAT")
    
    # Making 3 doors 

    canvas.create_rectangle(50, 50, 150, 190,"darkorange", "Black")
    canvas.create_rectangle(200, 50, 300, 190, "darkorange", "Black")
    canvas.create_rectangle(350, 50, 450, 190, "darkorange", "Black")

    # adding some text 

    text3 = '"SWITCH or NO SWITCH?"'
    text4 = "Okay, let's see!"

    canvas.create_text(70, 80, font='Arial',  font_size = 30, text= "1", color='indigo')
    canvas.create_text(220, 80, font='Arial', font_size = 30, text= "2", color='indigo')
    canvas.create_text(370, 80, font='Arial', font_size = 30, text= "3", color='indigo')
    canvas.create_text(60, 220, font='Arial'"Bold", font_size = 20, text= '!!! 2 Goats   one Car!!!', color='green')
    canvas.create_text(50, 300, font='Arial', font_size = 24, text= text3, color='red')
    canvas.create_text(120, 400, font='Arial', font_size = 40, text= text4, color='Blue')
    

    
    print("Now you have 2 doors left to open")
    print()
    print("If you want the car.....")
    print("should you switch your 1st choice?")
    print("mmm.....")
    print("We will repeat the whole game again again")

    #asking the user to input the number of simulations

    count = ''
    while count == '':
        try:
            count = repeat = int(input("Enter the number of simulations: "))
        except ValueError:
            print("That's not a number!")

    print()
    print()

    behind_doors = ["goat", "goat", "car"]
    open_door = []

    #for random choice of switch or no switch

    switch = ["Yes", "No"]
    switch_win = 0
    no_switch_win = 0

    for i in range(repeat):

        random.shuffle(behind_doors)
        
        #random picking of a box numbered 0, 1, 2

        choice1 = random.randint(0, 2)
        
        car_idx = behind_doors.index("car")
        
    #open door consists of the door numbers which contains goat only, Monty is going to open one of them so it should not contain the car.
        for i in range(3):
            if behind_doors[i] == "goat":
                open_door.append(i)
        
        
    #conditioning on different choices of the first pick

    #if the first picked door has a car behind it

        if choice1 == car_idx:
            
            monty_door = random.choice(open_door)

            
            switch_ans = random.choice(switch)
            if switch_ans == "No":
                no_switch_win += 1
            else:
                no_switch_win += 0
    
    #if the first picked door has a goat behind it

        elif choice1 != car_idx:

            if open_door[0] == choice1:
                monty_door = open_door[1]
            else:
                monty_door = open_door[0]

            

            switch_ans = random.choice(switch)
            if switch_ans == "Yes":
                switch_win += 1
            else:
                switch_win += 0

    # here we show whether we should switch or not for the maximum win probability by attemting the game a large number of time

    total_win = switch_win + no_switch_win

    # Percentage of the win while switching 

    switch_win_percentage = switch_win*100/total_win

    # Percentage of the win while not switching 

    no_switch_win_percentage = no_switch_win*100/total_win

    # Printing the numbers

    print("If you switch your first choice the percentage of winning the car is: ", round(switch_win_percentage, 3))
    print()
    print()
    print("If you do not switch your first choice the percentage of winning the car is: ", round(no_switch_win_percentage, 3))
    print()
    if switch_win_percentage > no_switch_win_percentage:
        print("So switching is important:)")

    else:
        print("You don't really need to switch.")

if __name__ == '__main__':
    main()