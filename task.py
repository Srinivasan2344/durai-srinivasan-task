#task 1
a = 10
b = 6
print(a & b)
# task 2
x = 12
y = 5
print(x | y)
#task 3
num = 8
print(~num)
#task 4
a = 15
b = 9
print(a ^ b)
#task 5
num = 7
print(num << 2)
#task 6
num = 20
print(num >> 1)
#task 7
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#print(a & b)
#task 8
#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))
#print(a ^ b)
#task 9
s = "hi"
print(s * 4)
#task 10
s = "python"
print(s * 3)
#task 11
a = "super"
b = "man"
print(a + b)
#task 12
a = "hello"
b = " "
c = "world"
print(a + b + c)
#task 13
name = input("Enter name: ")
print(name * 5)
#task 14
a = input("Enter first string: ")
b = input("Enter second string: ")
print(a + b)
#task 15
name = input("Enter your name: ")
print(type(name))
#task 16
age = int(input("Enter your age: "))
print(age)
#task 17
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
#task 18
m1 = int(input("Enter first mark: "))
m2 = int(input("Enter second mark: "))
avg = (m1 + m2) / 2
print("Average:", avg)
#task 19
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = 3*a*2 + b - 2
print("Result:", result)
#task 20
num = input("Enter a number: ")
print("Before type casting:", type(num))
num = int(num)
print("After type casting:", type(num))
#task 21
num = input("Enter a number: ")
print("Last digit:", num[-1])
#task 22
num = int(input("Enter a number: "))
print("Unit digit:", num % 10)
#task 23
num = int(input("Enter a number: "))
print("Number after removing last digit:", num // 10)
#task 24
num = int(input("Enter a number: "))
second_last = (num // 10) % 10
print("Second last digit:", second_last)
#task 25
num = int(input("Enter a 5 digit number: "))
print("Last digit:", num % 10)
#task 26
if 10 >= 5:
    print("10 is greater than or equal to 5")
#task 27
num = int(input("Enter a number: "))
if num > 50:
    print("Number is greater than 50")
#task 28
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible")
#task 29
num = int(input("Enter a number: "))
if num > 100:
    print("Number is greater than 100")
#task 30
num = int(input("Enter a number: "))
if num >= 0:
    print("Number is positive or zero")
#task 31
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
#task 32
marks = int(input("Enter your marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")
#task 33
num = int(input("Enter a number: "))
if num >= 0:
    print("Positive number")
else:
    print("Negative number")
#task 34
num = int(input("Enter a number: "))
if num > 10:
    print("Number is greater than 10")
else:
    print("Number is not greater than 10")
#task 35
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")
#task 36
marks = int(input("Enter marks: "))
age = int(input("Enter age: "))

if marks >= 60:
    if age >= 17:
        print("Admission Granted")
    else:
        print("Admission Rejected")
else:
    print("Admission Rejected")
#task 37
age = int(input("Enter age: "))
height = int(input("Enter height: "))
weight = int(input("Enter weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected for sports")
        else:
            print("Not selected")
    else:
        print("Not selected")
else:
    print("Not selected")
#task 38
num = int(input("Enter number (1-7): "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
#task 39
num = int(input("Enter number (1-3): "))

match num:
    case 1:
        print("Red")
    case 2:
        print("Blue")
    case 3:
        print("Green")
    case _:
        print("Invalid number")
#task 40
num=int(input("enter the number 1 to 4 :"))   
match num:
    case 1:
        print("apple")
    case 2:
        print("mango")
    case 3:
        print("orange")
    case 4:
        print("banana")
