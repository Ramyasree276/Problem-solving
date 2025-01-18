str1= input("enter string: ")
i=0
j= len(str1) -1
str = list(str1)
while(i<j):
    str[i],str[j]=str[j],str[i]
    i += 1
    j-= 1
print(str)
str2 = ''.join(str)
print(str2)
if(str1== str2):
    print("Palindrome")
else:
    print("not a palindrome")