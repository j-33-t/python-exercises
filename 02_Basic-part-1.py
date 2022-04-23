# Resource
# https://www.w3resource.com/python-exercises/python-basic-exercises.php



# 1. Write a Python program to get the Python version you are using

from logging import raiseExceptions
from platform import python_version
from re import I
from types import new_class
from matplotlib.pyplot import eventplot

from numpy import append
from validators import Min




python_version()


# 2. Write a Python program to display the current date and time. (default date format in python - YYYY-MM-DD)

from datetime import date, datetime
Today = date.today()

print(f"today's date is: {Today}")


# 3. Write a Python program which accepts the radius of a circle from the user and compute the area
from math import floor, pi

r = float(input("Enter radius of the circle: "))
area = pi*r**2
print(f"Area of the circle is : {area}")

# 4. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

print(f"{last_name} {first_name}")

# 5. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers

numbers = map(int,input("Enter numbers values separated by space: ").split())
list_n = list(numbers)
tuple_n = tuple(numbers)

print(f"list : {list_n}")
print(f"tuple: {tuple_n}")

# 6. Write a Python program to accept a filename from the user and print the extension of that.
filename = input("Enter filename: ")
extension = filename.rsplit(sep = ".", maxsplit=1)
print(f"filetype: {extension[1]}")

# 7. Write a Python program to display the first and last colors from the following list

color_list = ["Red","Green","White" ,"Black"]

print(color_list[0],color_list[-1])

# 8. Write a Python program to display the examination schedule (extract the date from exam_st_date)
from datetime import datetime
exam_st_date = (11, 12, 2014)

exam_st_date = str(exam_st_date) \
    .replace("(","") \
        .replace(")","")
                
exam_st_date = datetime.strptime(exam_st_date, "%d, %m, %Y").strftime('%d/%m/%Y')
print(exam_st_date)

# Solution 2
exam_st_date = (11, 12, 2014)
print("Exam date will start from : %i / %i / %i " %exam_st_date)

# 9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n = int(input("Enter a number: "))

n1 = int("%i" %n)
n2 = int("%i%i" %(n,n))
n3 = int("%i%i%i" %(n,n,n))
print(f"{n1+n2+n3}")

# 10 . Write a Python program to print the docstring  of Python built-in function(s).

print(f"{int().__doc__}")

# 11. Write a Python program to print the calendar of a given month and year.
import calendar
y = 2022
m = 4
print(calendar.month(y,m))

# 12.  Write a Python program to print the following
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example

print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")


# 13. Write a Python program to calculate number of days between two dates.
# Sample : (2014, 7, 2), (2014, 7, 11)

date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

date1 = str(date1) \
    .replace("(","") \
        .replace(")","")
        

date2 = str(date2) \
    .replace("(","") \
        .replace(")","")
        
date1 = datetime.strptime(date1, "%Y, %m, %d")
date2 = datetime.strptime(date2, "%Y, %m, %d")

diff = (date2 - date1).days
print(f"difference in days: {diff}")

# 14.  Write a Python program to get the volume of a sphere with radius 6.
# formua = 4/3 pi*r**2
r = 6
area_of_sphere = (4/3)*pi*(r**3)
print(f"are of sphere is : {round(area_of_sphere, 2)}")

# 15. Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference

def difference(n):
    if n > 17:
        print((n-17)*2)
    else: 
        print(17 - n )
        
n = int(input("Enter number: "))
difference(n)

# 16. Write a Python program to test whether a number is within range 100 to 1000 or 2000.

def test(n):
    if n < 100:
        print("Less than 100")
    elif n < 1000:
        print("between 100 and 1000")
    elif n < 2000:
        print("between 1000 and 2000")
    else:
        print("n greater than 2000")
        
n = int(input("Enter a number: "))
test(n)

# 17. Write a Python program to calculate the sum of three given numbers, 
# if the values are equal then return three times of their sum.

def three_times(n,n1,n2):
    if n == n1 == n2:
        print(f"{(n+n1+n2)*3}")
    else:
        print(f"{n+n1+n2}")
        
three_times(1,2,3)
three_times(3,3,3)

# 18.  Write a Python program to get a new string from a given string where "Is" has been added to the front. 
# If the given string already begins with "Is" then return the string unchanged

def is_start(string):
    if string.startswith("Is"):
        print(string)
    else:
        print(f"Is {string}")
    
sentance = str(input("Enter a sentance: "))
is_start(sentance)

# 19. Write a Python program to find whether a given number (accept from the user) is even or odd, 
# print out an appropriate message to the user

def odd_even(n):
    if (n%2) == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")

odd_even(20)
odd_even(11)

# 20. Write a Python program to count the number 4 in a given list


def count_4(array):
    count = 0
    for n in array:
        if n == 4:
            count = count +1
    return count

n = [1,2,3,4,5,6,5,4,3,2,1,4]
count_4(n)

# 21. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def n_string(string,n):
    text = ""
    for i in range(n):
        text = text + string
    return text

print(n_string("Messi ", 3))


# 22. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
# Return the n copies of the whole string if the length is less than 2.

def n_2_string(string,n):
    text = ""
    for i in range(n):
        if len(string) < 2:
            text = text + string
        else:
            text = text + string[0] + string[1]
    return text
            
n_2_string("messi", 3)

# 23. Write a Python program to test whether a passed letter is a vowel or not. 

def vowel_check(string):
    # Converting input to string and to lowercase
    string = str(string).lower()
    
    # Checking if string is of length == 1
    if len(string) > 1:
        return TypeError("Only input single character")
    else:
        pass
    
    # Checking if string contains only alphabets
    if string.isalpha():
        pass
    else:
        return TypeError("Only alphabets allowed as input")
    
    # Storing all vowels for further conditional statements    
    vowels = ["a","e","i","o","u"]

    # Checking if entered character is a vowel or not
    if string in vowels:
        print("Entered letter is a vowel")
    else:
        print("Entered letter is not a vowel")



vowel_check("a")
vowel_check(1)


# 24. Write a Python program to check whether a specified value is contained in a group of values
# Sample 1:  3 -> [1, 5, 8, 3] | Sample 2: -1 -> [1, 5, 8, 3]

def check_n(n,list):
    if n in list:
        return True
    else:
        return False

n1 = 3
list_1 = [1, 5, 8, 3]

check_n(n,list_1)

n2 = -1
list_2 = [1, 5, 8, 3]

check_n(n2,list_2)


# 25. Write a Python program to create a histogram from a given list of integers


def histogram(list):
    for i in list:
        character = "+"
        if i < 10:
            print(f"{i*character}")
        else:
            print(f"{i*character}")

list = [ 5,10,15,20,25]
histogram(list)


# 26. Write a Python program to concatenate all elements in a list into a string and return it


def concat_elements(list):
    new_list = ""
    for i in list:
        new_list = new_list + str(i)
    return new_list

concat_elements([20,4,2022])


# 27. Write a Python program to print all even numbers from a given numbers list in the same order 
# and stop the printing if any numbers that come after 237 in the sequence

# Sample list


def even_print(list):
    new_list = []
    for i in list:
        if i%2 == 0:
            new_list.append(i)
    return new_list
              
        
        
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]  

even_print(numbers)


# 28. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.



def gcd(x,x2):
   # Storing factors from variable x
   factors = []
   
   # Storing factors from variable x2
   factors2 = [] 
   
   # For loop for finding factors of x
   for i in range(1,x+1):
       if x % i == 0:
           factors.append(i)
   
   # For loop for finding factors of x2
   for i in range(1,x2+1):   
       if x2 % i == 0:
           factors2.append(i)       
   
   # Finding common numbers among lists i.e factors and factors2 
   factors_set = set(factors)
   common = factors_set.intersection(factors2)
   GCD = list(common)
   
   return (f"The GCD of {x} and {x2} is: {max(GCD)}")
    

# Testing    
gcd(20,28)
gcd(186,168)


# 29. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

def sum_fun(x,x1,x2):
    if x == x1:
        return 0
    elif x1 == x2:
        return 0
    elif x == x2:
        return 0
    else:
        return (x+x1+x2)
    
sum_fun(2,2,1)
sum_fun(1,2,3)

# 30. Write a Python program to get the least common multiple (LCM) of two positive integers.


def lcm(x,x2):
    x_multiples = []
    x2_multiples = []
    
    if x < x2:
        for i in range(1,x*(x2+1)):
            if i%x == 0:
                x_multiples.append(i)
                
        for i in range(1,x2*(x2+1)):
            if i%x2 == 0:
                x2_multiples.append(i)
    else:
        for i in range(1,x*(x+1)):
            if i%x == 0:
                x_multiples.append(i)
                
        for i in range(1,x2*(x+1)):
            if i%x2 == 0:
                x2_multiples.append(i)
            
    lcm = []
    for i in x2_multiples:
        if i in x_multiples:
            lcm.append(i)
    
    
    return min(lcm)
             
    
lcm(3,13)

        
