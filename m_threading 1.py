import threading

def cube(n):
    c=(n*n*n)
    print("Cube of the number: ",c)

def square(n):
    sq=(n*n)
    print("Square of a number: ",sq)

#creating thread
t1=threading.Thread(target=cube(),args=(5,));
t2=threading.Thread(target=square(),args=(5,));

#starting thread
t1.start()
t2.start()

#completing thread
t1.join()
t2.join()
