testcases=int(input("enter the number of test cases"))
l=[]
n=int(input("Enter the number of elements you want to enter in the list: "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)
print("The given list is: ",l)
c=0
for i in l:
    if i%2==0:
        c+=1
print("The number of even numbers in the list is: ",c)
print("The number of odd numbers in the list is: ",n-c)
