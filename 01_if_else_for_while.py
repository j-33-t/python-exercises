# Exercise 1: Print First 10 natural numbers using while loop

# Solution 1
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
for i in range(1 , 6, 1):
    for j in range(1, i+1):
        print(j, end =  " ")
    print("")

      
#----------------------------
# Interveted range loop
for i in range(5 , -1, -1):
    for j in range(1, i+1):
        print(j, end =  " ")
    print("")



    

    


