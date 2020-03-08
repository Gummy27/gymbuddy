import csv
from textract import process

data = [words for words in str(process('Notes_200302_161724_0fd.docx')).split('\\n') if words != ''][2:-1]

'''
with open('file.csv', 'a+') as f:
    for x in data:
        if x[0:-2] != 'Day':
            strp = []
            name = ""
            for i in x.split(' '):
                try:
                    int(i)
                    strp.append(int(i))
                except:
                    if strp == []:
                        name += f"{i} "
                    pass
                   # print(i, end=" ")
            f.write(f"{name.strip()}:{strp[0]}:{strp[1]},")
        else:
            f.write('\n')
'''