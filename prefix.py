str1=input("Enter a string: ")
str2=input("Enter the prefix to be added before each word: ")
str1=str1.split()
for i in str1:
    print(str2+i,end=' ')
