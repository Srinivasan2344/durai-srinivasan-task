#task 1
def create_user(name, age, role):
    user = {
        "name": name.title(),   
        "age": age,
        "role": role
    }
    return user
users = []
users.append(create_user("durai", 22, "developer"))
users.append(create_user("arun", 25, "tester"))
users.append(create_user("bala", 23, "analyst"))
for user in users:
    print(user)

#task 2

def calculate_total(*numbers):
    total = sum(numbers)
    
    if len(numbers) > 0:
        average = total / len(numbers)
    else:
        average = 0
    return total, average
result = calculate_total(10, 20, 30, 40)
print("Total:", result[0])
print("Average:", result[1])

#task 3

def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")
system_config(mode="debug", version="1.0", user="durai")

#task 4 

def factorial(n):
    if n < 0:
        return "Factorial not defined negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(1))   
print(factorial(-3))  

#task 5

n = 5
square_gen = (i * i for i in range(n))   # generator
square_list = [i * i for i in range(n)]  # list
print("Type of list:", type(square_list))
print("Type of generator:", type(square_gen))
print("\nList Output:")
print(square_list)
print("\nGenerator Output:")
for value in square_gen:
    print(value)

#task 6

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input (enter numbers only)")

finally:
    print("Program Completed")

#task 7


users = [
    {"name": "Durai", "age": 22, "role": "Developer"},
    {"name": "Arun", "age": 25, "role": "Tester"},
    {"name": "Bala", "age": 23, "role": "Analyst"}
]
file = open("team_data.txt", "w")

for user in users:
    line = f"{user['name']}, {user['age']}, {user['role']}\n"
    file.write(line)
print("Before closing:", file.closed)

file.close()
print("After closing:", file.closed)
file = open("team_data.txt", "r")

print("\nFile Content:")
for line in file:
    print(line.strip())

file.close()