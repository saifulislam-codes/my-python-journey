# **📦 Part 1: List (Mutability, Slicing & Logic)
# 1. Count Without `len()`**
# Write a function to count and return the total number of elements in a list using a `for` loop. Do not use the built-in `len()` function.
list1 = [10 ,20 , 30 , 40 , 50]
count = 0 
for num in list1 :
    count= count + 1
print(count)    

# **2. Manual List Reversal**
#Write a function to reverse a list in-place using a loop. Do not use `[::-1]` or the built-in `.reverse()` method.
def manu_rev_implace(data_list : list) ->list:
    try:
        if data_list is None or not isinstance(data_list , list):
            print("invalid output!")
            return None
        
        if len(data_list) == 0:
            print("Empty!")
            return[]
        left = 0 ;
        right = len(data_list) - 1
        
        while left < right:
            p = data_list[left]
            data_list[left] = data_list[right]
            data_list[right] = p
            
            left = left + 1
            right = right - 1
        return data_list
    
    except Exception as error:
        print(error)
        return None
       
            
list1 = [10 , 20 , 30 , 40 , 50] 
print(list1)

result = manu_rev_implace(list1)
print(result)
    

# **3. The Index Shifting Trap**
# Given a list (e.g., `[1, 2, 3, 2, 4]`), write a function to remove all occurrences of a specific element (e.g., `2`). Handle the logic safely so that modifying the list inside the loop does not skip adjacent target elements due to index shifting.
# **4. Single-Pass Max and Min**
# Find both the maximum and minimum numbers in a list by iterating through it exactly once (Single-Pass). Do not use the built-in `max()` or `min()` functions.
def maxi_mini(data: list) -> list:
    current_max = data[0]
    current_min = data[0]
    
    for num in data[1:]:
        if current_max < num:
            current_max = num
            #print(f"maximum is : {current_max}")
        if current_min > num :
            current_min = num
           # print(f"minimum is : {current_min}")
    return(current_max , current_min)        
                
data = [10 , 40 , 30 , 50 , 20]
print(maxi_mini(data))
                
    
# **5. Array Sorted Checker**
# Write a function that takes a list of numbers and checks whether it is sorted in ascending order. Return `True` if sorted, otherwise `False`.
def order_checker(data2 : list) -> bool:
    if len(data2) <= 1:
        return True
    
    
    for i in range(len(data2) - 1):
        if data2[i +1 ] < data2[i]:
            return False
    return True

data2 = [10 , 20 , 30 , 40 , 50 ]
print(order_checker(data2))  