testcases=int(input("enter the number of test cases"))
for l in range(testcases):
	l=[]
	numbers=int(input("enter the number of elements that you want to insert in the list"))
	for j in range(numbers) :
	 	data =int (input("enter the data you want to insert"))
	 	l.append(data)
	print("displaying the initial list",l)
	l[0],l[len(l)-1] = l[len(l)-1],l[0]
	print("displaying the final list",l)
	 
