import csv

class WorkoutPlan():
    def __init__(self):
        self.days = []
        with open('file.csv', 'r') as f:
            for index, x in enumerate(f.read().split('\n')):
                self.days.append([])
                for aefing in x.split(',')[:-1]:
                    if aefing != [' ']:
                        name, reps, sets = aefing.split(':')
                        self.days[index].append(Aefing(name, reps, sets))

    def __str__(self):
        strengur = ""
        for index, x in enumerate(self.days):
            strengur += f"day {index+1}\n"
            for i in x:
                strengur += f"   {i}\n"

        return strengur

    def selection(self):
        for x in range(len(self.days)):
            print(f"Day {x+1}")

    def day(self, index):
        return self.days[index]

class Aefing():
    def __init__(self, name, reps=0, sets=0):
        self.name = name
        self.reps = reps # Hve oft æfingin er gerð í einu
        self.sets = sets # Hve mikið af reps þú gerir.

    def __str__(self):
        return f"{self.name}: {self.reps} reps og {self.sets} sets."

def greinaskil():
    print("------------------------")
