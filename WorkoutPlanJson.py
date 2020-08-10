import json

days = []
with open('Data/file.csv', 'r') as f:
    for index, x in enumerate(f.read().split('\n')):
        days.append([])
        for aefing in x.split(',')[:-1]:
            if aefing != [' ']:
                name, reps, sets = aefing.split(':')
                days[index].append([name, reps, sets])


dictionary = {}
for index, day in enumerate(days):
    for exercise in day:
        name, reps, sets = exercise
        exerciseDict = {
            "name" : name,
            "reps" : reps,
            "sets" : sets,
            "best" : '0'
        }
    dictionary["day"+str(index)] = exerciseDict


with open("sample.json", "w") as file:
    json.dump(dictionary, file)
