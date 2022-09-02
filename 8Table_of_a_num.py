# Write a program to print a table of a number entered from the user.
num=int(input("Enter the number::=  "))
i=1
while i <= 10:
    print(num,"*",i,"=",num*i)
    i+=1