# Variables, Strings, and Basic Logic (Python)


# Swap two variables without using a third variable.

a= int(input("Enter a : "))
b = int (input("Enter b : "))

a = a + b 
b = a - b 
a = a - b

print("a is : " , a)
# print("b is : ", b)

# Take a user's full name and print it in "Lastname, Firstname" format.

first_name = input("Enter user's first name : ")
last_name = input("Enter user's last name : ")

last_name , first_name = first_name , last_name
print(first_name , last_name)

# Calculate the area of a circle where the radius is taken as user input.

radius = float(input("Enter the radius: "))
area = 3.1416*radius*radius
print("the area is : " , area)

# Create a program that converts Celsius to Fahrenheit.

celsius = float(input("Enter the cels' temp : "))
fahernheit = (celsius *9 / 5) + 32
print("the fahernheit temp is :", fahernheit)

# Input a sentence and count how many words it has using split().

sent = input("Enter any sentence : ")
count = len(sent.split())
print(count)

# Take a string and print it in reverse without using loops (use slicing).

str = input("Enter string : ")
reverse_str = str[:: -1]
print(reverse_str)

# Check if a string is a palindrome (reads the same forward and backward).'

str = input("enter string :")
reverse_str = str[::-1]
if(reverse_str == str):
    print("palindrome")
else:
    print("Not palindrome")
            
# Extract the domain name from an email address (e.g., user@gmail.com → gmail.com).
email = input("enter the string : ")
if('@' in email):
    pos = email.find('@')
    domain = email[pos + 1 :]
    print(domain)
else:
    print("no domain exist")    

# Remove all leading and trailing spaces from a string and replace middle spaces with hyphens.

str = input("Enter sting : ")
new_str = str.strip()
if(' ' in new_str):
    new_new_str = new_str.replace(' ' , '-')
    print(new_new_str)
    
# Input a long string and find the index of a specific word.

str = input("Enter string : ")

target_str = input("your target string : ")

index_pos=str.find(target_str)
print(index_pos)
