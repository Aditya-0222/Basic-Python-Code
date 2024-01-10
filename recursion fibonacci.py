# fibbonacci series 1 2 3 5 8 13  ......n using recursion

a=0
b=1
def fibbo(n):
    global a,b
    if(n==0):
        return
    else:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        fibbo(n-1)


#calling
n=int(input("Enter the limit"))
fibbo(n)
