from tkinter import *
import WorkoutPlan

def bua_til_aefingar(name, reps, sets):
    with open("aefingar.json", 'a+') as json_file:
        x = {
            "name": name,
            "sets": sets,
            "reps": reps
        }
        json.dump(x, json_file)

def greinaskil():
    print("------------------------")

test = WorkoutPlan()

production = False
while production:
    select = int(input("Hvaða dag ertu á? : "))
    if select == 0:
        break
    else:
        aefingar = test.day(select-1)
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

win = Tk()
frameControls = Frame(win)
frameControls.grid(row=1)



win.mainloop()




