# Exercise 1: Print First 10 natural numbers using while loop

# Solution 1
from itertools import count
from cv2 import sumElems


x = 0
while x < 10:
    print(x)
    x = x+1

#------------

# Solution 2
x = 0
result = []

while x < 10:
    x = x+1
    result.append(x)

print(result)

#-------------------------------------------------------------------------------------

# Exercise 2: Write a program to print the following number pattern using a loop.
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# start : 1
# stop  : 6
# step : 1
# run loop 5 times
for i in range(1 , 6):
    for j in range(1, i+1):
        print(j, end =  " ")
    print("")

      
#----------------------------
# Interveted range loop
for i in range(5 , -1, -1):
    for j in range(1, i+1):
        print(j, end =  " ")
    print("")



#-------------------------------------------------------------------------------------    

# Exercise 3: Calculate the sum of all numbers from 1 to a given number    

# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

number_x = int(input("Enter a number: "))

total = 0

for i in range(1,number_x + 1):
    total += i

print(f"Sum is : {total}")
    
    
#-------------------------------------------------------------------------------------
    
# Exercise 4: Write a program to print multiplication table of a given number till 10

num = 2
num_table = []

for i in range(1,num*11):
    if i%num == 0:
        num_table.append(i)
        
print(num_table)

#-------------------------------------------------------------------------------------

# Exercise 5: Display numbers from a list using loop

# Write a program to display only those numbers from a list that satisfy the following conditions
# -- The number must be divisible by five
# -- If the number is greater than 150, then skip it and move to the next number
# -- If the number is greater than 500, then stop the loop        

# Given : 
numbers = [12, 75, 150, 180, 145, 525, 50]

# Solution
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i%5 == 0:
        print(i)
    
#-------------------------------------------------------------------------------------    
# Exercise 6: Count the total number of digits in a number

# Write a program to count the total number of digits in a number using a while loop.
#   For example: the number is 75869, so the output should be 5.

n = 75869
counter = 0

# solution 1
while counter != len(str(n)):
    counter += 1

print(f"Total digits are: {counter}")

# solution 2
n = 75869
counter = 0
while n != 0:
    n = n // 10
    counter = counter + 1 

print(f"Total digits are: {counter}")


#-------------------------------------------------------------------------------------    

# Exercise 7: Print the following pattern

# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
   
    
for i in range(5,0,-1):
    for j in range(i,0,-1):
     print(j, end = " ")
    print("")

#-------------------------------------------------------------------------------------    

# Exercise 8: Print list in reverse order using a loop

# Given:
list1 = [10, 20, 30, 40, 50]

# solution 1: 
new_list = reversed(list1)

for i in new_list:
    print(i)

#solution 2:
start = len(list1) -1

for i in range(start,-1,-1):
    print(list1[i])
    
#-------------------------------------------------------------------------------------    
# Exercise 9: Display numbers from -10 to -1 using for loop

for i in range(-10,0,1):
    print(i)
    
#-------------------------------------------------------------------------------------    

# Exercise 11: Write a program to display all prime numbers with a range 1 to "n"

n = 10
for num in range(0, n+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)


                

                
        