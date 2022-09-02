#10. Write a program to check whether a number is prime or not.

#A prime number is a whole number greater than 1 with only two factors=themselves
#  and 1

num=int(input("Enter the number:= "))
i=2
d=num//2
while i<d:
    if num%i==0:
        print(num,"not a prime number")
        break
    else:
        print(num,"is a prime number")
        break