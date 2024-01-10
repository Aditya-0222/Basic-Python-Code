# Reverse of number using recursion
s = 0
def reverse(n):
    global s
    if(n>0):
        r=n%10
        s=s*10+r
        n=n//10
        reverse(n)
    return s

#calling
n=int(input("Enter a number"))
x=reverse(n)
print("Reverse is %d "%x)
if(x==n):
    print("No is palindrom")
else:
    print("No is not palindrom")
