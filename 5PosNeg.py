l=[]
n=int(input("Enter the number of elements you want to enter in the list: "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)
print("The given list is: ",l)
pc=nc=0
for i in l:
    if i>0:
        pc+=1
    elif i<0:
        nc+=1
print("The number of positive numbers in the list is: ",pc)
print("The number of negative numbers in the list is: ",nc)
