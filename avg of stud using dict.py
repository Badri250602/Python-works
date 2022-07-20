#creating a dict and printing average marks
n=int(input())  #no. of students
marks={}  #marks is a dictionary
for _ in range(n):
    name,*line=input().split()  #*line is a list without brackets
    scores=list(map(float,line)) #line(iterator) is mapped to float and made into a list
    marks[name]=scores     #name-keys and scores-values
    
query_name=input()
tot_marks=sum(marks[query_name])
avg_marks=tot_marks/3
print("%0.2f"%(avg_marks))  #gives only two significant digits
