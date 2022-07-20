'''marks = {}
n = int(input())
for x in range(n):
    name = input()
    mark = float(input())
    
    if mark in marks:
        marks[mark].append(name)
    else:
        marks[mark] = [name]

all_marks = list(set(marks.keys()))
all_marks.sort()
names_ordered = marks[all_marks[1]]
names_ordered.sort()

for name in names_ordered:
    print(name)'''

#creating a dictionary
marksheet={}
n=int(input())
for x in range(n):
    name=input()
    mark=float(input())

    if mark in marksheet:
        marksheet[mark].append(name)

    else:
        marksheet[mark]=[name]

marklist=set(marksheet.keys())
list_marklist=list(marklist)
list_marklist.sort()
namelist=marksheet[list_marklist[1]]
namelist.sort()

for names in namelist:
    print(names)






























