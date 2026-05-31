# - Print numbers from 1 to 10 using a while loop.
i = 1 
while True: 
    print(i)
    i+=1
    if i > 10:
        break
# - Print all numbers between 1 and 100 that are divisible by 7 using a while loop.
i = 1 
while True :
    if i % 7 == 0 and i <= 100:
        print(i)
    i+=1 
    break   
# - Print the multiplication table of a number in reverse order (from 10 down to 1) using a while loop.
n = int(input("Enter n: "))
i = 10
while True:
    print(n *i)
    if i <1:
        break
    i-=1 
# - Skip printing odd numbers from 1 to 20 using while and continue.
i = 1 
while True :
    if(i % 2 == 0) and i <= 20 :
        print(i)
        continue
    i+=1
    break
# - Create an infinite loop that breaks only when the user inputs the word "exit".
i = 1
while True :
    user_input = input("Enter text: ")
    if user_input == 'exit':
        break
    else:
        print(i)
    i+=1  
        
        
    
# - Implement a simple "Guess the Number" game where the loop runs until the user guesses correctly.
import random 
secret_num = random.randint(1 , 50)
while True :
    n = int(input("enter your number(1 - 50) : "))
    
    if n == secret_num :
        print("matched!")
    elif n > secret_num:
        print("too high!")
    elif n < secret_num:
        print("too low!")
    else:
        print("out of range!")
        break                       
# - Accumulate a user's expenses until they type "stop", then display the total expense.
total_expenses = 0 
while True:
    print("calc the total expenses untill type stop : ")
    user_input = input("enter your expenses:  ")
    if user_input == 'stop':
        break
    amount = float(user_input)
    total_expenses += amount
print(total_expenses)

