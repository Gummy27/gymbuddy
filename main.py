from tkinter import *
from WorkoutPlan import WorkoutPlan

class Exercise_navigator():
    def __init__(self, size):
        self.index = 0
        self.size = size

    def next(self):
        if self.index + 1 < self.size:
            self.index += 1

    def back(self):
        if self.index - 1 > 0:
            self.index -= 1

workout = WorkoutPlan()

win = Tk()
win.geometry("300x500")

banner = Label(win, text="This is a banner")
banner.pack(fill=Y)

# Valmynd yfir hvaða dag þú ert á í planinu.
days_frame = Frame(win)

days_buttons = []
for x in range(len(workout.days)):
    button = Button(days_frame, text=f"Day {x}")
    button.pack(fill=Y)
    days_buttons.append(button)

# Æfingin sem þú ert á
exercise_frame = Frame(win)

index = 0
exercise_label = Label(exercise_frame, text=workout.days[0][index])
exercise_label.pack()

navigator = Exercise_navigator(len(workout.days[0]))

back_button = Button(exercise_frame, text="Back", command=navigator.back)
back_button.pack()

exercise_frame.pack()

win.mainloop()




