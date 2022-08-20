testcases=int(input("Enter the number of test cases : - "))
for i in range(testcases):
	l=[]
	num=int(input("Enter the number of integers that you want to insert into the list : - "))
	if(num<6):
		break
	else:
		for n in range(num):
			data=int(input("Enter the data that you want to insert into the list : - "))
			if(data==" "):
				break
			else:
				l.append(data)
	print("The initial list is :- ",l)
	odd=[]
	even=[]
	length=len(l)
	d=0
	for j in l:
		if(j%2==0):
			#d=l[j]
			even.append(j)
		else:
			#d=l[j]
			odd.append(j)
	print("Displaying the odd list : - ",odd)
	print("Displaying the even list : - ",even)
	oddlength=len(odd)
	evenlength=len(even)
	sub=[]
	s=0
	last=0
	if(oddlength!=evenlength):
		if(oddlength>evenlength):
			for k in range(evenlength):
				s=odd[k]-even[k]
				sub.append(s)
				last=k
			for m in range(last+1,last+(oddlength-evenlength)+1):
				even.append(0)
				s=odd[m]-even[k]
				sub.append(s)
		elif(evenlength>oddlength):
			for k in range(oddlength):
				s=odd[k]-even[k]
				sub.append(s)
				last=k

			for m in range(last+1,last+(evenlength-oddlength)+1):
				odd.append(0)
				s=odd[m]-even[m]
				sub.append(s)		
	else:
		for k in range(oddlength):
			s=odd[k]-even[k]
			sub.append(s)
	sub=sub.sort()
	print("The sorted sublist is : - ",sub)
	
		
