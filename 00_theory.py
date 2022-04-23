#############################
# Introduction to for loops #
#############################

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
for i in range(1,20):
    if i%3 == 0:
        total.append(i)

print(total)
