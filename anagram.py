str1=input("Enter first string: ")
str2=input("Enter another string: ")
str1=str1.lower()
str2=str2.lower()
str1=str1.replace(" ","")
str2=str2.replace(" ","")
if (len(str1)==len(str2)):
    sort1=sorted(str1)
    sort2=sorted(str2)
    if (sort1==sort2):
        print("They are anagram.")
    else:
        print("They are not anagram.")
else:
    print("They are not anagram.")


