#mini project 1
employees = []

# Add
def add_emp():
    emp = {
        "name": input("Name: "),
        "age": int(input("Age: ")),
        "role": input("Role: "),
        "salary": float(input("Salary: "))
    }
    employees.append(emp)

# Display
def show_emp():
    for emp in employees:
        print(emp)

# Update
def update_emp():
    name = input("Enter name to update: ")
    for emp in employees:
        if emp["name"] == name:
            emp["age"] = int(input("New Age: "))
            emp["role"] = input("New Role: ")
            emp["salary"] = float(input("New Salary: "))

# Delete
def delete_emp():
    name = input("Enter name to delete: ")
    for emp in employees:
        if emp["name"] == name:
            employees.remove(emp)

# Menu
while True:
    print("\n1.Add 2.Show 3.Update 4.Delete 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_emp()
    elif ch == "2":
        show_emp()
    elif ch == "3":
        update_emp()
    elif ch == "4":
        delete_emp()
    elif ch == "5":
        break

#mini project 2

# Input
name = input("Enter name: ")
m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))

# Store in dictionary
student = {
    "name": name,
    "marks": [m1, m2, m3]
}

# Calculate
total = sum(student["marks"])
avg = total / 3

# Grade
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 50:
    grade = "C"
else:
    grade = "Fail"

# Output
print("\n--- Report Card ---")
print("Name:", student["name"])
print("Marks:", student["marks"])
print("Total:", total)
print("Average:", avg)
print("Grade:", grade)

#mini project 3

cart = []

# Add product
def add_item():
    name = input("Product name: ")
    price = float(input("Price: "))
    qty = int(input("Quantity: "))

    item = {"name": name, "price": price, "qty": qty}
    cart.append(item)

# Display items
def show_cart():
    total = 0
    print("\n--- Cart ---")
    for item in cart:
        print(item["name"], "-", item["price"], "x", item["qty"])
        total += item["price"] * item["qty"]
    print("Total Bill:", total)

# Remove item
def remove_item():
    name = input("Enter product name to remove: ")
    for item in cart:
        if item["name"] == name:
            cart.remove(item)

# Menu
while True:
    print("\n1.Add 2.Show 3.Remove 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_item()
    elif ch == "2":
        show_cart()
    elif ch == "3":
        remove_item()
    elif ch == "4":
        break

#mini project 4

# Users data
users = {
    "durai": "9876543",
    "sri": "78775887"
}

# Login input
uname = input("Username: ")
pwd = input("Password: ")

# Validation
if uname in users and users[uname] == pwd:
    print("Login Successful")
else:
    print("Login Failed")

#mini project 5

names = input("Enter visitor names (comma separated): ").split(",")

visitors = set(names)   # remove duplicates

print("Unique Visitors:", visitors)
print("Total Unique Visitors:", len(visitors))

#mini project 6

# Input
name = input("Enter name: ")
product = input("Enter product: ")

# Formatted sentence
print(f"{name} bought {product}")

# Padding
print(name.ljust(10))   # left align
print(product.rjust(10))   # right align
print(name.center(10))  # center align

#mini project 7

account = {}

# Create account
def create_acc():
    name = input("Name: ")
    bal = float(input("Initial Balance: "))
    account["name"] = name
    account["balance"] = bal

# Deposit
def deposit():
    amt = float(input("Amount to deposit: "))
    account["balance"] += amt

# Withdraw
def withdraw():
    amt = float(input("Amount to withdraw: "))
    if amt <= account["balance"]:
        account["balance"] -= amt
    else:
        print("Insufficient balance")

# Check balance
def check_balance():
    print("Balance:", account.get("balance", 0))

# Menu
while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Balance 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        create_acc()
    elif ch == "2":
        deposit()
    elif ch == "3":
        withdraw()
    elif ch == "4":
        check_balance()
    elif ch == "5":
        break

#mini project 8

votes = {}

# Voting
while True:
    name = input("Enter candidate name (type 'stop' to end): ")
    if name == "stop":
        break

    votes[name] = votes.get(name, 0) + 1

# Display votes
print("\nVotes:", votes)

# Find winner
winner = max(votes, key=votes.get)
print("Winner:", winner)

#mini project 9

students = {}

# Add student
def add_student():
    name = input("Student name: ")
    courses = input("Enter courses (comma separated): ").split(",")
    students[name] = courses

# Update courses
def update_courses():
    name = input("Enter student name: ")
    if name in students:
        courses = input("Enter new courses: ").split(",")
        students[name] = courses

# Display
def show_students():
    for name, courses in students.items():
        print(name, "->", courses)

# Menu
while True:
    print("\n1.Add 2.Update 3.Show 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        update_courses()
    elif ch == "3":
        show_students()
    elif ch == "4":
        break

#mini project 10

def number_tool(n):
    print("Binary:", format(n, "b"))
    print("Octal:", format(n, "o"))
    print("Hex:", format(n, "x"))
    print("With commas:", f"{n:,}")
    print("Scientific:", f"{n:.2e}")

num = int(input("Enter number: "))
number_tool(num)
