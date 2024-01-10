def asm(a,b):
    c=a+b
    d=a-b
    e=a/b
    return(c,d,e)

p,q,r=asm(50,20)
print("add",p)
print("sub",q)
print("div",r)
