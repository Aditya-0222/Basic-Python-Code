#factorial of number using recursion

def factorial(n):
    if(n==0):
        return 1
    else:
        f=n*factorial(n-1)     #function calling itself
        return f

#calling
n=int(input("Enter a number"))
x=factorial(n)
print("Factorial is ",n,"is ",x)
