num=input("Enter the number ")
i=-1
b=0-len(num)
sum=""
while b<=i:
    a=num[i]
    sum=sum+a
    i+=1
print(sum)



a=int(input("enter"))
rev=0
temp=a
while temp>0:
    b=temp%10
    rev=rev*10+b
    temp=temp//10
if a==rev:
    print(rev,"palindrome ")
else:
    print(rev,"not palindrome")
 