from tkinter import *
from WorkoutPlan import WorkoutPlan

class Exercise_navigator():
    def __init__(self, size):
        self.index = 0
        self.size = size

    def next(self):
        if self.index + 1 < self.size:
            self.index += 1
        print(self.index)

    def back(self):
        if self.index - 1 > 0:
            self.index -= 1
        print(self.index)

class GUI():
    def __init__(self, class_win):
        self.workout = WorkoutPlan()
        self.index = 0
        self.size = len(self.workout.days[0])

        self.navigator = Exercise_navigator(len(self.workout.days[0]))

        # Initializing
        # Frames
        self.exercise_frame = Frame(class_win)
        self.button_frames = Frame(class_win)

        # Labels
        self.exercise_label = Label(self.exercise_frame, text=self.workout.days[0][self.index])

        # Buttons
        self.back_button = Button(self.button_frames, text="Back", command=self.button_back)
        self.next_button = Button(self.button_frames, text="Next", command=self.button_next)


        # Packing
        # Frames
        self.exercise_frame.grid(row=0)
        self.button_frames.grid(row=1)

        # Labels
        self.exercise_label.grid(sticky=E)

        # Buttons
        self.back_button.grid(row=0, column=0, sticky=E)
        self.next_button.grid(row=0, column=1, sticky=E)


    def button_next(self):
        if self.index + 1 < self.size:
            self.index += 1
            self.exercise_label.config(text=self.workout.days[0][self.index])

    def button_back(self):
        if self.index + 1 > 0:
            self.index -= 1
            self.exercise_label.config(text=self.workout.days[0][self.index])






win = Tk()
win.geometry("300x500")

interface = GUI(win)

win.mainloop()




