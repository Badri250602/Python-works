n=int(input())
l=[]
for _ in range(n):
    x=input().split()
    cmnd=x[0]
    args=x[1:]
    if cmnd !="print":
        cmnd+="("+ ",".join(args) +")"  #here the braces,commas are concatenated using join(args) and '+' operator
        eval("l."+cmnd)       #eval()function makes it as expression (i.e l.insert(args)) eg: l.insert(0,5)
    else:
        print(l)

#alternate method
'''n=int(input())
l=[]
for _ in range(n):
    x=input().split()
    cmnd=x[0]
    args=x[1:]
    if cmnd !="print":
        eval('l.{0}{1}'.format(cmnd,tuple(map(int,args))))  #shortcut method
    else:
        print(l)'''