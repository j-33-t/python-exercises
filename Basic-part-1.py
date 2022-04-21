# Resource
# https://www.w3resource.com/python-exercises/python-basic-exercises.php



# 1. Write a Python program to get the Python version you are using

from platform import python_version



python_version()


# 2. Write a Python program to display the current date and time. (default date format in python - YYYY-MM-DD)

from datetime import date, datetime
Today = date.today()

print(f"today's date is: {Today}")


# 3. Write a Python program which accepts the radius of a circle from the user and compute the area
from math import pi

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