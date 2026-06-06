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

# Input a string and capitalize only the first and last characters.
text = input("Enter text: ")
first = text[0].upper()
last = text[-1].upper()
middle = text[1 : -1]
print(first+middle+last)

# Create a basic calculator that takes two numbers and an operator (+,−,∗,/).
a = int(input("enter a : "))
b = int(input("Enter b : "))
op = input("enter op : ")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b)
else:
    print("invalid!")
                
# Find the remainder of a division without using the % operator.
n = int(input("Enter n : "))
d = int(input("Enter d : "))
q = n //d 
r = n - (d * q)
print(r)

# Check if a string contains only numbers.
text = input("Enter your text : ")
try: 
    new_text = int(text)
    print("number exists")
except Exception as error:
    print("number does not exists")
# Convert a string like "1,000" into an integer (remove the comma).
text = input("Enter any str num : ")
new_text = text.replace(',', "") 
print(int(new_text))
# Take a user's birth year and calculate their age.
current_year = int(input("Enter current year : "))
birth_year = int(input("Enter birth year"))
age = current_year - birth_year
print(age)

# Swap the first and last characters of a string.
string = input("Enter text : ")
p = string[-1]
string[-1] = string[0]
string[0] = p 
print(string)

# Repeat a string N times, where N is provided by the user.
text = input("Enter string: ")
n = int(input("Enter n :"))
empty_str = ""
for new_str in range(n):
    empty_str = empty_str + text 
print(empty_str)
    

# Use input() to get a sentence and replace all vowels with *.
text = input("Enter text : ")
vowel = ('a', 'e', 'i', 'o', 'u' , 'A', 'I', 'O', 'U','E')

for rep in vowel:
    text = text.replace(rep, '*')
print(text)

# Write a program that converts total seconds into hours, minutes, and seconds.
total_second = int(input("Enter seconds: "))
hours = total_second // 3600
remaining_second = total_second % 3600
minitues = remaining_second // 60
second = remaining_second % 60

print(f"{total_second} seconds : {hours} H {minitues} min {second} sec")

