#task 1
for i in range(1, 51):
    print(i)
#task 2
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
#task 3
for i in range(1, 101):
    if i % 2 != 0:
        print(i)
#task 4
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)
#task 5
total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)
#task 6
for i in range(50, 0, -1):
    print(i)
#task 7
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count =", count)
#task 8
for i in range(1, 11):
    print(i * i)
#task 9
for i in range(1, 11):
    print(i ** 3)
#task 10
n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)
#task 11
i = 1
while i <= 20:
    print(i)
    i += 1
#task 12
n = int(input("Enter number: "))
fact = 1
i = 1

while i <= n:
    fact *= i
    i += 1

print("Factorial =", fact)
#task 13
num = int(input("Enter number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print("Reversed number =", rev)
#task 14
num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits =", count)
#task 15
text = ""

while text != "stop":
    text = input("Enter something (type 'stop' to end): ")
#task 16
for i in range(1, 5):
    print("*" * i)
#task 17
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()
#task 18
for i in range(1, 6):
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)
    print()
#task 19
for i in range(3):
    for j in range(3):
        print(chr(65 + j), end=" ")
    print()
#task 20
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()
#task 21
s = input("Enter string: ")
count = 0
for i in s:
    count += 1
print("Total characters:", count)
#task 22
s = input("Enter string: ")
count = 0

for ch in s:
    if ch.lower() in "aeiou":
       count += 1

print("Vowels:", count)
#task 23
s = input("Enter string: ")
count = 0

for ch in s:
    if ch.isalpha() and ch.lower() not in "aeiou":
        count += 1

print("Consonants:", count)
#task 24
s = input("Enter string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed:", rev)
#task 25
s = input("Enter string: ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#task 26
s = input("Enter string: ")

print("First 5:", s[:5])
print("Last 3:", s[-3:])
print("Reverse:", s[::-1])
print("Every 2nd:", s[::2])
print("Removed first & last:", s[1:-1])
#task 27
lst = [10, 20, 30, 40, 50]
print("Sum =", sum(lst))
#task 28
print("Max =", max(lst))
#task 29
print("Min =", min(lst))
#task 30
count = 0
for i in lst:
    count += 1
print("Count =", count)
#task 31
a = int(input("Enter element: "))

if a in lst:
    print("Exists")
else:
    print("Not Exists")
#task 32
lst = []
lst.append(10)
lst.append(20)
lst.append(30)
print(lst)
#task 33
lst.insert(1, 99)
print(lst)
#task 34
lst.remove(20)
print(lst)
#task 35
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Reversed:", rev)
#task 36
lst = [5, 2, 9, 1, 3]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted:", lst)
