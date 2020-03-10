from tkinter import *
from WorkoutPlan import *

workout = WorkoutPlan()

while True:
    select = int(input("Hvaða dag ertu á? : "))
    if select == 0:
        break
    else:
        aefingar = workout.day(select - 1)
        index = 0
    while True:
        arrows = input("Next or Back or Done? : ").lower()
        if arrows == "back":
            if index-1 >= 0:
                index -= 1
                print(aefingar[index])
            else:
                print("this is not a valid action")
        elif arrows == "next":
            if index+1 < len(aefingar):
                index += 1
                print(aefingar[index])

            else:
                print("this is not a valid action")
        if arrows == "done":
            break
        greinaskil()