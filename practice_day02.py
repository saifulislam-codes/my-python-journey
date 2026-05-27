# **1. Variables & Data Types**
# 1. Swap two variables without using a temporary variable (Using Pythonic way).
a = int(input("Enter your number : "))
b = int(input("enter your number : "))

a = a + b
b = a - b
a = a - b

print(a)
print(b)

# 2. Take user's first name, last name, and age, then print them in a single sentence using concatenation.
first_name = input("Enter first name: ")
last_name = input("Enter last name : ")

name = first_name + last_name
age = int(input("enter your age : "))

print(f"my name is {name} , and my age is {age}")

# 3. Check the data type of `input()` by default and convert it to float.x 
x = int(input("enter any number : "))
print(float(x))

# 4. Assign a single value to three variables simultaneously and print them.
a = b = c = int(input("Enter your num : "))
print(a)
print(b)
print(c)

# 5. Take an integer input, convert it to a float, then to a string, and check its final type.
x = int(input("Enter x : "))
print("this is an integer num : ", x)
print(float(x))
print(str(x))

# 6. Create a variable with an invalid name (e.g., starting with a number) and observe the error, then fix it.


# 7. Swap three variables: `a` goes to `b`, `b` goes to `c`, and `c` goes to `a`.
a= int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

temp = b 
b = a 
a = c
print("a is : ", b)
print("b is : " , c )
print("c is : ", a)


# 8. Take a string input like "123" and convert it into an integer. What happens if the input is "abc"? Handle it conceptually.
x = input("Enter number as a string : ")
if x.isdigit():
    number = int(x)
    print(number)
else:
    print("abc can not be acceptable")
        

# 9. Create a program that initializes an integer, a float, a string, and a boolean, then prints all of them in a single line separated by a pipe (`|`).
my_int = int(input("Enter integer : "))
my_float = float(input("enter float : "))
my_str = input("enter string: ")
my_bool = True

print(my_int , my_float , my_str , my_bool)

# 10. Calculate the simple interest given Principal, Rate of Interest, and Time as inputs.
principal = float(input("Enter principal : "))
rate = float(input("Enter rate : "))
time = float(input("Enter time : "))

interest = (principal * rate * time) /100 
print("the interest is : ", interest)
total_ammount = interest + principal
print("the total ammount is : ", total_ammount)

# 11. Take a user's birth year, calculate their age, and dynamically assign it to a variable.
boy = int(input("Enter your boy: "))
age = 2026 - boy 
print(age)

# 12. Create a variable storing a large number (e.g., 1000000000) using underscores for readability and print it.
large_number = 1_000_000_000
print(large_number)

# 13. Input two boolean values from the user (True/False) and store their logical `AND` result in a variable.
bool1 = True
bool2 = False
bool = bool1 and bool2
print(bool)

# 14. Declare a constant variable for the value of Pi ($\pi$) and use it to calculate a cylinder's volume.
pi = 3.1416
r = float(input("Enter your radius : "))
h = float(input("Enter h :"))

v= pi *(r**2)*h
print("the volume is :" , v)

# 15. Take a multi-line string input using triple quotes and store it in a single variable.
my_text = """"my name is saiful islam , and this is me"""
print(my_text)

# 16. Find the memory address of a variable using the `id()` function.
x = int(input("enter any number : "))
memory_address = id(x)
print("the value of x is :" , x)
print("memory address : " , memory_address)
# 17. Create two variables with the same value and check if their memory addresses are identical
x = y = 50
memory_address = id(x)
memory_address1 = id(y)
if memory_address == memory_address1:
    print("identical")
else:
    print("not identical")
        
# 18. Initialize a variable as `None` and check its data type.
x = None
print(type(x))

# 19. Given `x = "5"` and `y = "10"`, print their sum as an integer and then as a concatenated string.
x = "5" 
y = "10"
print(int(x) + int(y))
print(x + y)

# 20. Take a number as a string input, add 5 to it, and output the result as a float.
x = "10"
y = int(x) + 5 
result = float(y)
print(result)

# 21. Store a user's weight in kilograms and convert it to pounds inside a new variable ($1\text{ kg} = 2.20462\text{ lbs}$).

# 22. Create a dynamic profile card printout using variable assignments for name, profession, and country.
name = input("Enter your name :")
profession = input("Enter your profession :")
country = input("Enter your country : ")
print(name)
print(profession)
print(country)

# 23. Create a boolean variable that checks if a user-inputted number is positive.
number = float(input("Enter a number: "))
is_positive = number > 0
print(is_positive)

# 26. Take a product price as input, add 15% VAT, and store the final price in a variable.
price = float(input("Enter product price: "))
final_price = price * 1.15
print(f"Final price with 15% VAT: {final_price:.2f}")
