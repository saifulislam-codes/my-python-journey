# 1. Create a basic calculator that takes two numbers and an operator ($+, -, *, /$)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
op = input("Enter operator: ")

if op == '+':
    print(a + b) 
elif op == '-' :
    print (a - b )
elif op == '*':
    print(a * b) 
elif op == '/':
    print(a / b) 
           
# 2. Assign letter grades (A, B, C, D, F) based on a student's percentage mark.
marks = int(input("Enter students marks : "))
if marks < 100 and marks >= 80 :
    print("A+")
elif marks <= 79 and marks >= 50 :
    print("A")
else:
    print("F")
        
# 3. Write a program to calculate the electricity bill based on units consumed (slabs: 1-100, 101-200, >200).

# 4. Take a number representing a day (1-7) and print the corresponding day of the week.
day_num = int(input("Enter your num : "))
if day_num == 1 :
    print("monday")
elif day_num == 2 : 
    print("tuesday")
elif day_num == 3 :
    print("wednesday")
elif day_num == 4 : 
    print("Thrusday")
elif day_num == 5 :
    print("Friday")
                    
# 5. Create a simple login system with a hardcoded username and password.
ACTUAL_USERNAME = "hello_world"
ACTUAL_PASSWORD = "12345678"
user_name = input("Enter your user name :")
user_password = int(input("enter your user password : "))

if user_name == ACTUAL_USERNAME and user_password == ACTUAL_PASSWORD :
    print("LOG in")
else:
    print("Can not log in !")
        
# 6. A shop gives a 10% discount if the total cost of purchased quantity is more than 1000. Calculate total cost.
cost = int(input("Enter your cost : "))
total_cost = cost - (10 * 1 /100)
if cost >=1000 : 
    print("total cost = ", total_cost)
else:
    print("buy more things ! ")
    
# 7. Categorize a person's age into Life Stages: Infant, Child, Teenager, Adult, Senior.
# 8. Check whether an inputted character is a vowel, consonant, digit, or special character using elif.
# 9. Create an ATM machine simulation: check balance, deposit, or withdraw with insufficient balance checks.
# 10. Determine the quadrant of a coordinate point $(x, y)$ (First, Second, Third, or Fourth quadrant).
# 11. Take a month number (1-12) and print the number of days in that month.
# 12. Write a program to check if an input number is a multiple of 2, 3, or both.
# 13. Calculate income tax based on salary slabs specified by a dummy tax law.
# 14. Check if a user entered a valid password (must contain minimum length and specific checks via if-elif).
# 15. Predict traffic light actions: given "Red", "Yellow", or "Green", print "Stop", "Wait", or "Go".
# 16. Determine if an employee is eligible for a promotion based on years of experience and performance rating.
# 17. Create a rock-paper-scissors game outcome logic for a single round given two player choices.
# 18. Check if a custom-entered URL is secure (https) or insecure (http) or invalid.
# 19. A school has following rules for grading system: Below 25 - F, 25 to 45 - E, 45 to 50 - D, 50 to 60 - C, 60 to 80 - B, Above 80 - A.
# 20. Check if a number is divisible by both 5 and 11.
# 21. Determine the oldest and youngest among three people based on their inputted ages.
# 22. Calculate the delivery charge for an e-commerce order based on distance and order value.
# 23. Take an integer temperature value and describe the weather (Freezing, Cold, Warm, Hot).
# 24. Verify if a 4-digit PIN entered by a user matches the correct system PIN.
# 25. Given a student's attendance percentage, decide if they are allowed to sit in the exam ($\ge 75\%$).
# 26. Check if a basic quadratic equation $ax^2 + bx + c = 0$ has real, distinct, or imaginary roots using the discriminant ($b^2 - 4ac$).
# 27. Decide whether a vehicle is speeding based on its speed and the road type (Highway vs. City).
# 28. Evaluate a text input: if it's "hi", say "hello"; if "bye", say "goodbye"; else say "I don't understand".
# 29. Determine the ticket price for a movie theater based on age (child, adult, senior) and show timing.
# 30. Check if a given string contains a space, if so print "Contains Space", else check if it contains a tab, else "Clean".