###########################
# Control Flow Statements #
###########################
# """ 
# The flow control statements are divided into three categories
# 1. Conditional statements : [if, if-else, if-elif-else, nested if-else]
# 2. Iterative statements : [for, while]
# 3. Transfer statements : [break, continue, pass]
# """



#############
# For loops #
#############

# """ 
# For Loops
# A for loop is used for iterating over a sequence (this is either a list, tuple, a dictionary, a set or a string)

# This is less like for keyword in other programming languages, and works more like an iterator method as found in other
# object oriented programming languages

# """

# Example 1 : For loop basics , iterating over a list

grocery_list = ["banana", "apple", "micrsoft"]

# printing one by one
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])

# solution 1 [default end = "\n"]
for element in grocery_list:
    print(element)

# solution 2 [with end = " "]
for element in grocery_list:
    print(element, end = " ")

# solution 3     
for element in grocery_list:
    print(element, end = ", ")
    

# -------------------------------------------------------

# Example 2: iterating over list

numbers = [20,10,5]

for x in numbers:
    print(x)
    
# -------------------------------------------------------

# Example 3: print sum of the list

numbers = [1,2,3]
total = 0

for x in numbers:
    total = total + x

print(f"sum of the numbers is : {total}")


# -------------------------------------------------------

# Example 4: Using range to create a list to use in a for loop

# Range Syntax : range(start,stop,step)

# Parameter	Description
# start :	Optional. An integer number specifying at which position to start. Default is 0
# stop  :	Required. An integer number specifying at which position to stop (not included).
# step  :	Optional. An integer number specifying the incrementation. Default is 1


# Creating a range from 1 to 5, but not including 5
numbers = range(1,5)

# Converting the range object to list
numbers = list(numbers)

# print the list
print(numbers)

# Using the range in for loop
for i in range(1,5):
    print(i)
    
# finding sum of a range [Syntax 1]
total = 0

for i in range(1,4):
    total = total + i

print(total)

# finding sum of a range [Syntax 2]
total = 0

for i in range(1,4):
    total += i

print(total)

# -------------------------------------------------------

# Example 5. Add every second number in a range
total = 0

for i in range(0,11,2):
    total += i

print(total)


# -------------------------------------------------------

# Example 6. Checking if number is multiple of 3

total = []
for i in range(1,31):
    if i%3 == 0:
        total.append(i)

print(total)

# -------------------------------------------------------
# Example 7. program to display student's marks from record

student_name = 'James'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(f"{student_name} scored {marks[student]} in exam.")
        break
else:
    print('No entry with that name found.')

# --------------------------------------------------------------------------------------------------

################
# Nested loops #
################


# Example 1 print 1-5 four times

for i in range(0,4):
    for j in range(0,5):
        print(j+1, end = " ")
    print("")
    

# --------------------------------------------------------------------------------------------------

###############
# While loops #
###############

# With the while loop we can execute a set of statements as long as a condition is true.

# Example 1: 

x = 1 
while x < 6:
    print(x)
    x = x + 1 # Note: remember to increment x, or else the loop will continue forever.

# ------------

# Example 2 : Print a message once the condition is false
# """
# With the else statement we can run a block of code 
# once when the condition no longer is true:
# """

x = 1 
while x < 6:
    print(x)
    x = x + 1
else:
    print("x is no longer less than 6")

# ------------

# Example 3: Continue to the next iteration if x == 3:
# With the continue statement we can stop the current iteration, and continue with the next:

x = 0
while x < 6:
  x += 1
  if x == 3:
    continue
  print(x)


# ------------

# Example 4: Exit the loop when x == 3:
# With the break statement we can stop the loop even if the while condition is true:

x = 1
while x < 6:
  print(x)
  if x == 3:
    break
  x += 1
  
  
##