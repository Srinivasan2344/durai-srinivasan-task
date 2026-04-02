#task 1

class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   # parent constructor call
        self.dept = dept
        self.fees = fees

class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)
        self.duration = duration

s = Student("durai", 101, "CSE", 50000)
f = Faculty("srinivasan", 102, 40000)
t = TempFaculty("ravi", 103, 30000, "6 months")

print(s.name, s.id, s.dept, s.fees)
print(f.name, f.id, f.salary)
print(t.name, t.id, t.salary, t.duration)

#task 2
class AbstractUser:

    def get_details(self):
        raise NotImplementedError("Subclass must implement this method")


class User(AbstractUser):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"User: {self.name}, ID: {self.id}"


class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


s = Student("srinivasan", 101, "CSE", 50000)
f = Faculty("durai", 102, 40000)

print(s.get_details())
print(f.get_details())

#task 3

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

students = [
    Student("Arun", 50000),
    Student("Bala", 30000),
    Student("Charan", 70000)
]

faculties = [
    Faculty("durai", 40000),
    Faculty("srinivasan", 60000),
    Faculty("ravi", 35000)
]

students.sort(key=lambda x: x.fees)

print("Students sorted by fees:")
for s in students:
    print(s.name, s.fees)

faculties.sort(key=lambda x: x.salary)

print("\nFaculties sorted by salary:")
for f in faculties:
    print(f.name, f.salary)

#task 4

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


students = [
    Student("Arun", 50000),
    Student("Bala", 30000),
    Student("Charan", 70000)
]

names = list(map(lambda s: s.name, students))

print(names)

#task 5

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


students = [
    Student("Arun", 50000),
    Student("Bala", 30000),
    Student("Charan", 70000)
]

faculties = [
    Faculty("durai", 40000),
    Faculty("srinivasan", 60000),
    Faculty("ravi", 25000)
]

high_fee_students = list(filter(lambda s: s.fees > 50000, students))

print("High Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))

print("\nHigh Salary Faculty:")
for f in high_salary_faculty:
    print(f.name, f.salary)

#task 6

from functools import reduce

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees

class Faculty:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

students = [
    Student("Arun", 50000),
    Student("Bala", 30000),
    Student("Charan", 70000)
]

faculties = [
    Faculty("durai", 40000),
    Faculty("srinivasan", 60000),
    Faculty("ravi", 25000)
]


total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
print("Total Fees:", total_fees)

total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)
print("Total Salary:", total_salary)

#task 7

class Student:
    def __init__(self, name, fees):
        self.name = name
        self.fees = fees


def process_users(users, func):
    return list(map(func, users))

students = [
    Student("Arun", 50000),
    Student("Bala", 30000),
    Student("Charan", 70000)
]

def get_name(s):
    return s.name


def high_fee(s):
    return s.fees > 50000


names = process_users(students, get_name)
print("Names:", names)

high_fee_students = list(filter(high_fee, students))
print("High Fee Students:")
for s in high_fee_students:
    print(s.name, s.fees)

# final challenge task

from functools import reduce

# Base Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.id}"


# Student Class
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)
        self.dept = dept
        self.fees = fees

    def get_details(self):
        return f"Student: {self.name}, ID: {self.id}, Dept: {self.dept}, Fees: {self.fees}"


#Faculty Class
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary

    def get_details(self):
        return f"Faculty: {self.name}, ID: {self.id}, Salary: {self.salary}"


#Data
students = [
    Student("Arun", 101, "CSE", 50000),
    Student("Bala", 102, "ECE", 30000),
    Student("Charan", 103, "CSE", 70000)
]

faculties = [
    Faculty("durai", 201, 40000),
    Faculty("srinivasan", 202, 60000),
    Faculty("ravi", 203, 25000)
]


# Print All Details (map)
print("---- All Students ----")
list(map(lambda s: print(s.get_details()), students))

print("\n---- All Faculties ----")
list(map(lambda f: print(f.get_details()), faculties))


# Sorted Data (by fees & salary)
students.sort(key=lambda s: s.fees)
faculties.sort(key=lambda f: f.salary)

print("--- Sorted Students (by fees) ----")
for s in students:
    print(s.name, s.fees)

print("\n---- Sorted Faculties (by salary) ----")
for f in faculties:
    print(f.name, f.salary)


# Filtered Data
high_fee_students = list(filter(lambda s: s.fees > 50000, students))
high_salary_faculty = list(filter(lambda f: f.salary > 30000, faculties))

print("---- High Fee Students ----")
for s in high_fee_students:
    print(s.name, s.fees)

print("---- High Salary Faculty ----")
for f in high_salary_faculty:
    print(f.name, f.salary)


# Total Fees & Salary (reduce)
total_fees = reduce(lambda acc, s: acc + s.fees, students, 0)
total_salary = reduce(lambda acc, f: acc + f.salary, faculties, 0)

print("\nTotal Fees:", total_fees)
print("Total Salary:", total_salary)