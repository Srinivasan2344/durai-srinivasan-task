class User:
    def __init__(self):
        self.__user_name = None   # private variable
        self.__pwd = None         # private variable

    # setter method
    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print("Registering user:", self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)


u1 = User()

#  Set values
u1.set_user("john", "1234")

u1.register()
u1.login()

#task 2

# Parent Class
class User:
    def register(self):
        print("User Registered")

    def login(self):
        print("User Logged in")


# Child Class 1
class Student(User):
    def student_greet(self):
        print("Hello Student")


# Child Class 2
class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")


# Multilevel Child
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")


#  Objects
s = Student()
f = Faculty()
t = TempFaculty()

print("---- Student ----")
s.register()          # from parent
s.login()             # from parent
s.student_greet()     # own method

print("\n---- Faculty ----")
f.register()
f.login()
f.faculty_greet()

print("\n---- Temp Faculty ----")
t.register()             # from User
t.login()                # from User
t.faculty_greet()        # from Faculty
t.tempFaculty_greet()    # own method

#task 3

# Parent Class
class User:
    def greet(self):
        print("Welcome User")


# Child Class - Student
class Student(User):
    def greet(self):   # overriding
        print("Welcome Student")


# Child Class - Faculty
class Faculty(User):
    def greet(self):   # overriding
        print("Welcome Faculty")


#  Objects
student = Student()
faculty = Faculty()

#  Method Calls
student.greet()
faculty.greet()

#task 4

class User:

    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

#  Object
user = User()

#  Method Chaining
user.login().greet().register()

#task 5
class User:
    users_count = 0   # class variable

    def __init__(self, name, pwd):
        self.__name = name     # encapsulation
        self.__pwd = pwd
        User.users_count += 1  # increment count

    # getter
    def get_name(self):
        return self.__name

    # method chaining
    def login(self):
        print("logined:", self.__name)
        return self

    def register(self):
        print("registered:", self.__name)
        return self

    # method to override
    def greet(self):
        print("Welcome User")
        return self


# Student class
class Student(User):
    def greet(self):   # overriding
        print("Welcome Student")
        return self


# Faculty class
class Faculty(User):
    def greet(self):   # overriding
        print("Welcome Faculty")
        return self


#  Objects
s1 = Student("john", "1234")
f1 = Faculty("smith", "5678")

#  Method Chaining
s1.login().greet().register()

print("-----")

f1.login().greet().register()

#  Total users
print("Total Users:", User.users_count)