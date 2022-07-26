num=input("Enter the number ")
a=len(num)
sum=0
i=0
while i<a:
    b=num[i]
    c=int(b)**a
    sum=sum+c
    i+=1
print(sum)
if int(num)==sum:
    print("ARMSTRONG")
else:
    print("NOT ARMSTRON")