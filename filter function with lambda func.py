# Filter function with lambda expression

mylist=[10,7,8,12,66,23,88,67]
mylist1=list((filter(lambda x:(x%2==0),mylist)))
print(mylist1)
mystring="Data Flair provide free course"
str1=list(filter(lambda v:(v=='a' or v=='e'or v=='i' or v=='o' or v=='u'),mystring))

print(str1)
