l=[]
n=int(input("Enter the number of elements you want to emter in the list: "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)
print("The given list is: ",l)
l.sort()
print("The list after sorting is: ",l)
print("The second largest number in the list is: ",l[-2])
