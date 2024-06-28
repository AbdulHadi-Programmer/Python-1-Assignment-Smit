# Ans 1
print("Abdul Hadi Salman \n 19/01/2006")

# Ans 2:
name = "Abdul Hadi"
age = 18
is_student = True
print(name, age, is_student)

# Ans 3:
a = 100
b = 4

# Arithmatic Operators:
print(a+b) # Addition
print(a-b) # Substraction
print(a*b) # Multiplication
print(a/b) # Division
print(a%b) # Modulus

# Comparison Operator:
# == (Equal)
# != (Not equal)
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)
print(5 == 5)
print(10 != 7)
print(3 > 5)
print(9 < 5)
print(10 >= 10)
print(9 <= 99)


# Logical Operator:
# and
# or
# not
print(5 == 5 and 10 == 10)
print(3 == 3 or 7 == 5)
print(not True)

# Assignment Operator:

# = (Assign)
# += (Add and assign)
# -= (Subtract and assign)
# *= (Multiply and assign)
# /= (Divide and assign)
# %= (Modulus and assign)
# **= (Exponentiation and assign)
# //= (Floor division and assign)

a = 10
a += 45
print(a)
a -= 30
print(a)
a *= 10
print(a)
a /= 5
print(a)
a %= 7
print(a)
a = 3
a **= 2
print(a)
a //= 3 
print(a)

# Ans 4:
eng = 75
isl = 67
math = 84
total = 300
percent = (eng + isl + math ) / 300 *100
print(percent)

## Part 2: Python Basics (Conditional Statement)
# Ans 1:
# A company decided  to give bonus of 5% to employee is more than 5 years. Ask user for thier salary and year of service and print the net bonus amount.
emp1 = 6 # 6 years exp

if emp1 >= 5:
    print("Emp1 has more than 5 years of experience")
    salary1 = int(input("Enter your Salary: "))
    bonus = salary1 * 1.05
    print(f'The Increase Salary with bonus is : {bonus}')

# Ans 2:
# Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
age = int(input("Enter the age of the person: "))
if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

# Ans 3:
# Write a program to check whether a number entered by user is even or odd.
# Accept number from user
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# Ans 4:
# Write a program to check whether a numer is divisible by 7 or not. 
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")

# Ans 5:
# Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".
number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Hello")
else:
    print("Bye")


# Ans 6:
# Write a program to display the last digit of a number. 
# Accept number from user
number = int(input("Enter a number: "))
last_digit = number % 10
print("The last digit of the number is:", last_digit)

# Ans 7:
# Take values of length and breadth of a rectangle from user and print if it is square and rectangle.
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
if length == breadth:
    print("It is a square")
else:
    print("It is a rectangle")

# Ans 8:
# Take two int values from user and print the greatest among them. 
def greatest(a, b):
    return max(a, b)

print(greatest(9, 45))
# Ans 9:
# A Shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity = int(input("Enter the quantity of items: "))
cost_per_unit = 100
total_cost = quantity * cost_per_unit
if total_cost > 1000:
    total_cost = total_cost * 0.90
print("The total cost is:", total_cost)

# Ans 10:
# A School has following rules for grading system:
# Below 25 - F
# 25 to 45 - E
# 45 to 50 - D
# 50 to 60 - C
# 60 to 80 - B
# Above 80 - A
# Ask user to enter marks and print the corresponding grade.
print()
print()
eng = 47
comp = 87
urdu = 78
grade = (eng + comp + urdu) / 300 * 100

if grade > 80:
    print(grade, "A")
elif 60 < grade <= 80:
    print(grade, "B")
elif 50 < grade <= 60:
    print(grade, "C")
elif 45 < grade <= 50:
    print(grade, "D")
elif 25 < grade <= 45:
    print(grade, "E")
elif grade <= 25:
    print(grade, "F")
else:
    print("Wrong Input")


# Ans 11:
# A Student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Numbers of classes held.
# Numbers of classes attended.
# And print
# percentage of class attended
# Is Student is allowed to sit in exam or not 
total_classes = int(input("Enter the number of classes held: "))
attended_classes = int(input("Enter the number of classes attended: "))
attendance_percentage = (attended_classes / total_classes) * 100
print(f"Attendance percentage: {attendance_percentage}%")

if attendance_percentage >= 75:
    print("The student is allowed to sit in the exam.")
else:
    print("The student is not allowed to sit in the exam.")

# Ans 12:
# Modify the above question to allow student to sit if he/she has medical cause or not ('Y' or 'N') and print accordingly.
is_medical_cause = input("Enter 'Y' if the student has a medical cause and 'N' if not: ").upper()

if attendance_percentage >= 75 or is_medical_cause == 'Y':
    print("The student can sit in the exam.")
else:
    print("The student cannot sit in the exam.")

# Ans 13:
# Write a program to check if a year is leap year or not.
# If a year is divisible by 4 then it is leap year but if leap year but if the year is century year like 2000, 1900, 2100 then it must be divible by 400.
year = int(input("Enter the year to check leap year or not: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a Leap Year")
else:
    print("Its not a leap year")

# Ans 14:
# Ask User to enter age, gender(M or F), martial (Y or N) and then using following rules print their place of service.
# If employee is female then she will work only in urban areas.
# If employee is a male and age is in between 20 to 40 then he may work in Anywhere
# if employee is male and age is in between 40 to 60 then he will work in urban areas only. And any other input of age should print "Error"
age = int(input("Enter the Employee age: "))
gender = input("Enter Gender M for Male and F for female: ").upper()
Martial_status = input("Are you Married: Y for yes and N for No: ").upper()
if gender == 'F':
    print("\nEmployee are female")
    print("The Female only work in Urban Areas.\n")
elif gender == 'M' and ( age >= 20 and age <= 40):
    print("He can Work in anywhere like Urban and Rural")
elif gender == 'M' and ( age >= 40 and age <= 60):
    print("The Employee can only work in Urban Areas")
else:
    print("Error")

# Ans 15:
# Write a program to calculate the electricity bill (accept number of unit from user) according to the following critiria:
# Unit Price upto 100 units no charge Next 200 units Rs 5 per unit. After 200 units Rs 10 per unit 
# (For Example if input unit is 350 than total bill amount is Rs. 3500 
# (For Example if input uni is 97 than total bill amount is Rs.0 
# (For Example if input unit is 150 than total bill amount is Rs. 750 
# unit = int(input("Enter the Eletricity Unit per month: "))
unit = 350
def calculate_bill(unit):
    if unit <= 100:
        print("Your Bill is 0 Rs")
    elif unit >= 100 and unit <= 200:
        bill = unit * 5 
        print(f"The Unit {unit} and Your Bill is {bill}")
    elif unit >= 200:
        bill = unit * 10
        print(f"The Unit {unit} and Your Bill is {bill}")

calculate_bill(350)
calculate_bill(97)
calculate_bill(150)

# Ans 16:
# Take input of age of 3 people by user and determine oldest and youngest among them.
people1 = int(input("Enter the Age of People1: "))
people2 = int(input("Enter the Age of People1: "))
people3 = int(input("Enter the Age of People1: "))
def find_young():
    return int(min(people1, people2, people3))
print(find_young())

def find_oldest():
    return int(max(people1, people2, people3))
print(find_oldest())