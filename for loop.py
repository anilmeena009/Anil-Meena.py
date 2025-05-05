# Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.

# print("pizza-100, burger-50, sandwich-30")
# a=input("Enter the item: ")
# b=int(input("Enter the quantity: "))
# # if a=="pizza" or a=="burger" or a=="sandwich":
# if a=="pizza":
#       price=100*b
# elif a=="burger":
#       price=50*b
# elif a=="sandwich":
#       price=30*b
# else:
#       print("invalid item")
# if price>1000:
#          discount=price*0.1
#          final_price=price-discount
#          print("discount is :",discount)
#          print("final price after discount:",final_price)
# elif price>=500 and price<=1000:
#          discount=price*0.05
#          final_price=price-discount
#          print("discount is :",discount)
#          print("final price after discount:",final_price)
# else:
#       print("no discount")

# -----------------------------------------------------------------------
# Write a program that categorizes a person based on their age:
# Infant (0-1 year)
# Toddler (2-4 years)
# Child (5-12 years)
# Teenager (13-19 years)
# Adult (20-59 years)
# Senior (60 years and above)


# age = int(input("Enter the age: "))

# if age >= 0 and age <= 1:
#    category = "Infant"
# elif age >= 2 and age <= 4:
#    category = "Toddler"
# elif age >= 5 and age <= 12:
#    category = "Child"
# elif age >= 13 and age <= 19:
#    category = "Teenager"
# elif age >= 20 and age <= 59:
#    category = "Adult"
# elif age >= 60:
#    category = "Senior"
   
# else:
#    print("Invalid age")

# print("The person is categorized as:", category)
# -----------------------------------------------------------------------
# Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
# for Monday, 2 for Tuesday, etc.).
# number = int(input("Enter a number (1-7): "))

# if number == 1:
#    day = "Monday"
# elif number == 2:
#    day = "Tuesday"
# elif number == 3:
#    day = "Wednesday"
# elif number == 4:
#    day = "Thursday"
# elif number == 5:
#    day = "Friday"
# elif number == 6:
#    day = "Saturday"
# elif number == 7:
#    day = "Sunday"
# else:
#    day = "Invalid input"

# print("The day of the week is:", day)

# -----------------------------------------------------------------------
# Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in
# kilograms) and height (in meters). Then categorize the BMI into:
# Underweight (BMI < 18.5)
# Normal weight (18.5 <= BMI < 24.9)
# Overweight (25 <= BMI < 29.9)
# Obesity (BMI >= 30)
# Use the formula: BMI = weight / (height ** 2)


# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meter: "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#    category = "Underweight"
# elif 18.5 <= bmi < 24.9:
#    category = "Normal weight"
# elif 25 <= bmi < 29.9:
#    category = "Overweight"
# else:
#    category = "Obesity"
# print("Your BMI is:",bmi)
# print("You are categorized as:" ,category)

# -------------------------------------------------------------------------
# n=int(input("Enter a number: "))
# for i in range(1,n+1):
#    print(i)


# -------------------------------------------------------------------------
# n=int(input("Enter a number: "))
# for i in range(n,0,-1):
#    print(i)

# -------------------------------------------------------------------------
# ch=64
# end=90
# for i in range(ch,end):
#    ch+=1
#    print(chr(ch),end="")
# print(i)


# -------------------------------------------------------------------------
# n=100
# for i in range(1,n+1):
#       if i%2==0:
#          print(i)


# -------------------------------------------------------------------------
# conunt the number of digits in a number
# n = input("Enter a number: ")
# count = 0
# for i in range(1, len(n)+1):
#     count += 1
# print("The number of digits is:", count)


# -------------------------------------------------------------------------
# n =int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     digit = n % 10
#     sum += digit
#     n=n // 10
# print("The sum of the digits is:",i, sum)


# -------------------------------------------------------------------------
# print the reverse of a number
# num = int(input("Enter a number: "))
# reverse = 0
# for i in range(len(str(num))):
#    digit = num % 10
#    reverse = reverse * 10 + digit
#    num = num // 10
# print("The reverse number is:", reverse)


# -------------------------------------------------------------------------
# n = int(input("Enter the base number: "))
# b=2
# result = 1
# for i in range(b):
#    result *= n

# print(f"{n} raised to power  is: {result}")


# -------------------------------------------------------------------------
# find the factors of a number
# num = int(input("Enter a number: "))
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")
# print("are the factors of",num)


# -------------------------------------------------------------------------
# calculate the factorial of a number
# 
# --------------------------------------------------------------------------
# find LCM of two numbers using for loop
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# n=a*b
# if a > b:
#    c = a
# else:
#    c = b


# for i in range(c,n+1):
#    if i % a == 0 and i % b == 0:
#       lcm = i
#       break

# print(f"The LCM of {a} and {b} is: {lcm}")


# --------------------------------------------------------------------------
# check prime between 1 to n
# n = int(input("Enter a number: "))
# for i in range(2,n+1):
#    is_prime = True
#    for j in range(2,i):
#       if i % j == 0:
#          is_prime = False
#          break
#    if is_prime:
#       print(i, end=" ")
# print("are the prime numbers")
# --------------------------------------------------------------------------
# Check whether a number is prime or not

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# --------------------------------------------------------------------------
# all prime factors of a number
num = int(input("Enter a number: "))
for i in range(2, num + 1):
    if num % i == 0:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
print("Prime factors:", num)