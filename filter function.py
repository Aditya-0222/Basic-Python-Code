def even_odd(n):
    if n%2==0:
        return True
    else:
        return False


def prime_no(n):
     i=2
     f=0
     while(i<n):
         if(n%i==0):
             f=1
         i=i+1
     if(f==0):
         return True
     else:
         return False

mylist=[10,7,8,12,9,33,45,13,15,17]

mylist1=list(filter(prime_no,mylist))

print(mylist1)
