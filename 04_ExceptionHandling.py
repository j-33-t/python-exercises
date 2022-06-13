########################
#  Raising Exception   #
########################


# We can use raise to throw an exception if a condition occurs. 
# The statement can be complemented with a custom exception.

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

x = 4

print(x)


#################################
#  AssertionError Exception     #
#################################

# Instead of waiting for a program to crash midway, 
# you can also start by making an assertion in Python.

# We assert that a certain condition is met. 
# If this condition turns out to be True, then that is excellent! 
# The program can continue. If the condition turns out to be False, 
# you can have the program throw an AssertionError exception.

# AssertionError with error_message.
x = 1
y = 0
assert y != 0, "Invalid Operation" # denominator can't be 0

print(x / y)


 

#################################
#  try and except: Exception    #
#################################

x = 5
# z = 3
try:
  print(x+z)
except:
  print("An exception occurred, z not defined")
  
  
# Try, except, else

# Python code to illustrate
# working of try() 
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional
        # Part as Answer
        result = x // y
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
    else:
        print("Your answer is :", result)
   
# Look at parameters and note the working of Program
divide(3, 2)
divide(3, 0)