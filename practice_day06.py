# ==========================================
# 🟢 STEP 1: LOOP BASICS & RANGE CONTROL
# ==========================================

# 1. Print the first 10 natural numbers using a for loop.
num = int(input("Enter your num :"))

for i in range (1 , num +1) :
    print(i)
# 2. Print all numbers from 10 down to 1 using range() step parameters.

for i in range(10 , 0 , -1):
    print(i)
    
# 3. Print all even numbers between 1 and 50.

for i in range (1 , 51):
    if i % 2 == 0:
        print(i)
        
# 4. Print the multiplication table of a given number up to 10.

n = int(input("Enter n : "))

for i in range (1 , 11):
    print(n * i) 

# ==========================================
# 🟡 STEP 2: MATHEMATICAL & SERIES LOGIC
# ==========================================

# 5. Calculate the sum of all numbers from 1 to N, where N is provided by the user.
n = int(input("enter your number : "))
for i in range (1 , n + 1):
    print(i)
    
# 6. Factorial of a number using a for loop.
n = int (input("Enter n : "))
factorial = 1 

for i in range (1 , n+ 1):
    factorial = factorial * i
    print(factorial)
    

# 7. Calculate the sum of squares of the first N natural numbers.

n = int(input("Enter n : "))
sum = 0 
for i in range (1 , n + 1):
    sum = sum + (i**2)
    print(sum)
    
    
    
# 8. Print the Fibonacci sequence up to N terms using a for loop.


# ==========================================
# 🔵 STEP 3: STRING & DATA MANIPULATION
# ==========================================

# 9. Count the total number of vowels present in a given string.
text = input("enter text :")
vowel = 'aeiouAEIOU'
for i in text :
    if i in vowel :
        print(i)
        
# 10. Iterate through a string and print each character with its index position.


# 11. Print the elements of a string in reverse order without using slicing [::-1].


# 12. Separate digits and alphabets from an alphanumeric string into two different strings using a loop.


# ==========================================
# 🔴 STEP 4: ADVANCED LOGIC & PROBLEM SOLVING
# ==========================================

# 13. Check if a given number is prime using a for loop.


# 14. Print a pattern of stars: 1 star on line one, 2 stars on line two, up to N lines.


# 15. Given a list of numbers, find the largest number using a loop.