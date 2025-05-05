# year=8500

# while(year%4==0 and year%400==0):
#     if(year%101!=0):
#         print("Leap Year")
# else:
#      print("Not a Leap Year")
#-------------------------------------------------------------------
# question 1   
# n = int(input("Enter n number"))
# i = 1
# while i <= n:
#     print(i )
#     i=i+1
#-------------------------------------------------------------------
# question 2
# n = int(input("Enter the number  "))
# i = 1
# while(n>=i):
#     print(n)
#     n-=1
#-------------------------------------------------------------------
# question 3
# ch='a'
# while(ch<='z'):
#     print(ch ,end=' ')
#     ch=chr(ord(ch)+1)
#-------------------------------------------------------------------
# question 4

    
    
# n = 1
# while n<=100:
#     if n%2==0:
#         print(n ,end=',')
#     n+=1
#-------------------------------------------------------------------
# question 5
# n=int(input("Enter the number "))
# sum=0
# i=1
# while(i<=n):
#     if(i%2!=0):
#         sum=sum +i
#     i+=1
# print("sum of odd no. ",sum)
#-------------------------------------------------------------------
# question 6
# n=int(input("Enter the digits "))
# count=0
# while(n!=0):
    # n=n//10
    # count=count+1
# print("no. of digits. ",count)

#-------------------------------------------------------------------
# Program to check if a number is an Armstrong number
n = int(input("Enter a number: "))
temp = n
sum = 0
order = len(str(n))

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if n == sum:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
#-------------------------------------------------------------------