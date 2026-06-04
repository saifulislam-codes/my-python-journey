# 1. Write a function is_even(num) that returns True if a number is even, and False otherwise.
def is_even(num : int ) ->bool:
    if num is None :
        print("invalid!") 
        return False
    try:
        if num % 2 == 0 :
            return True
        else:
            return False
        
    except Exception as error:
        print(f"an error occurred:{error}")
        return None                    
        
# 2. Create a function calculate_area(radius) that returns the area of a circle.
def calc_area (rad : float) -> float:
    if rad is None:
            print("invalid")
    try:
        calculate_area = 3.1416 * rad **2
        return (calculate_area)
    except Exception as error:
        print(f"an error occured:{error}")
        return None 
     
rad = float(input("Enter radius : "))
print(calc_area(rad))
                
# 3. Write a function greet_user(name) that prints a personalized greeting message.
def greet_user (name: str ) -> str:
    if name is None or name == ' ':
        print("pls enter your name!!!")
    try:
        print(f"hello {name} , welcome back!")
    except Exception as error:
        print(error)
        
user_name = input("Enter your name :")
greet_user(user_name)

# 4. Create a function find_max(a, b, c) that returns the maximum of three numbers.
def find_max(a : float , b : float , c : float) -> float:
    if a is None or b is None or c is None:
        print("invalid!")
    try:
        if a >= b and a >= c :
            return a
        elif b >= c and b >= a :
            return b  
        elif c >= a and c >= b :
            return c
    except Exception as error:
        print("this is an error " , error)
        return 0.0
      
a = float(input("enter a :"))
b = float(input("enter b :"))
c = float(input("enter c :"))  
print(find_max(a , b , c))
 
# 5. Write a function factorial(n) that calculates and returns the factorial of $n$.
def factorial (n : int) -> int :
    if n is None or n < 0:
        print("invalid!")   
    try:
        fact = 1
        for i in range(1 , n + 1) :
            fact = fact * i
        return fact
    except Exception as error:
        print("this is an error: " , error)
    return 0

n = int(input("Enter n :"))
print(factorial(n))
     
        
# 6. Create a function reverse_string(text) that returns the reversed version of a string.

def rev_str(text : str) ->str:
    if text is None or text == " ":
        print("invalid!")
    try:
        rev_txt = text[::-1]
        return rev_txt
    except Exception as error:
        print(f"this text is an error occured {error}")
    return None

txt = input("Enter your text: ")
print(rev_str(txt))    
            
# 7. Write a function check_palindrome(text) that returns True if a string is a palindrome.
def check_palindrome (text : str) -> bool:
    if text is None or text == " ":
        print("invalid!")
    try:
        if text == text[::-1]:
            return True
        else:
            return False
    except Exception as error:
        print(f"this is an error occured {error}")

txt = input("enter your text : ") 
print(check_palindrome(txt))
               
# 8. Create a function count_words(sentence) that returns the total word count.
def count_words (sent : str) -> int:
    if sent is None or sent.strip() == "":
        print("invalid!")
    try:
        count = 0 
        for i in sent:
            count+=1
        return count
    except Exception as error:
        print(f"this is an error occured{error}")

text = input("Enter sentence: ")
print(count_words(text))
                    
# 9. Write a function celsius_to_fahrenheit(c) that returns the converted temperature.
def celsius_to_fahrenheit(cels : float) -> float :
    if cels is None :
        print("invalid!")
        return 0.0    
    try:
        far = (cels*9/5) + 32
        return far
    except Exception as error:
        print(f"this is an error occured.{error}")
    return 0.0

temp = float(input("Enter your temp :"))
print(celsius_to_fahrenheit(temp))
   
# 10. Create a function power(base, exponent) that returns the computed power without using .
def power(b : int , e : int ) -> int:
    if b is None or e is None :
        print("invalid! or get 0")
        return 0
    try:
        result = b**e
        return result
    except Exception as error:
        print(f"this is an error occured{error}")
        
b = int(input("Enter b : "))
e = int(input("Enter e : "))
print(power(b , e))
            
# 11. Write a function that takes a full name and returns it in "Lastname, Firstname" format.

def full_name(name : str) -> str:
    if name is None or name.strip() == "":
        print("invalid!")
        return None
    try : 
        part = name.split()
        if len(part) < 2 :
            return name
        
        first_name = part[0]
        last_name = part[-1]
        return last_name , first_name
    except Exception as error:
        print(f"an error{error}")
    return None

text = input("Enter name : ")
print(full_name(text))
      
# 12. Create a function is_prime(n) that returns True if a number is prime.
# 13. Write a function extract_domain(email) that returns the domain part of an email.
def extract_domain(email: str) -> str:
    if email is None or '@' not in email or email == "":
        print("Invalid")
        return None
    try :
        part = email.split('@')
        domain = part[-1]
        return domain
    except Exception as error:
        print("this is an error", error)
    return None 

text = input("Enter your email: ")
print(extract_domain(text))

# 26. Create a function is_multiple(a, b) that returns True if a is a multiple of b.
def is_multiple(a : int , b : int) -> bool:
    if a is None or a == 0 or b is None or b == 0:
        print("Invalid")
        return None
    try :
        if a % b == 0:
            return True
        else:
            return False
            
    except Exception as error:
        print(f"an error occured{error}")
    return False

a = int(input("a :"))
b = int(input("b :"))

print(is_multiple(a , b))

    
# 27. Write a function convert_currency(amount, rate) that returns the exchanged amount.
def convert_currency(amount : float , rate : float) -> float:
    if amount is None or rate is None or amount <= 0 or rate <= 0 :
        print("invalid")
        return None
    try:
        exchanged_amount = amount * rate
        return exchanged_amount
    except Exception as error:
        print(f"an error occured{error}")
    return 0.0

amount = float(input("Enter your amount:"))
rate = float(input("Enter your rate :"))
print(convert_currency(amount, rate))

# 28. Create a function hollow_square_string(size) that returns a string representing a hollow square.
# 29. Write a function remove_commas(text) that takes a string like "1,23,456" and returns an integer.
def remove_commas (text: str) -> int :
    if text is None or text == "":
        print("invalid!")
        return None
    try:
        new_text = text.replace(',', "")
        int_text = int(new_text)
        return int_text
    except Exception as error:
        print(f"this is an error{error}")
    return 0

text = (input("Enter your text :"))
print(remove_commas(text))        
        
        
# 30. Create a function net_salary(gross) that calculates and returns the salary after a 10% deduction.
def net_salaray(salary : int) -> float:
    if salary is None or salary <1:
        print("invalid!")
        return None
    try :
        calc_salray = salary - (salary * 0.1)
        return calc_salray
    except Exception as error:
        print(f"error occured{error}")
    return 0.0    
       
salary = int(input("Enter your salaray : "))
print(net_salaray(salary))        