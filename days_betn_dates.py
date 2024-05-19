"""
Write a Python program to calculate the number of days between two dates.

Python datetime.date(year, month, day) :

The function returns date object with same year, month and day. All arguments are required. Arguments may be integers, in the following ranges:

MINYEAR <= year <= MAXYEAR
1 <= month <= 12
1 <= day <= number of days in the given month and year
If an argument outside those ranges is given, ValueError is raised.

Note: The smallest year number allowed in a date or datetime object. MINYEAR is 1.
The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
Pictorial Presentation:

Calculate number of days between two dates
Sample Solution:

Python Code:
"""
# Import the 'date' class from the 'datetime' module
from datetime import date

# Define a start date as July 2, 2014
f_date = date(2014, 7, 2)

# Define an end date as July 11, 2014
l_date = date(2014, 7, 11)

# Calculate the difference between the end date and start date
delta = l_date - f_date

# Print the number of days in the time difference
print(delta.days)
"""
Sample Output:

9  
Explanation:

This script imports the "date" class from the "datetime" module.

It then creates two date objects (<class 'datetime.date'>), 'f_date 'and 'l_date'.

The script then calculates the difference between these two dates and stores it in a variable called 'delta'.

The 'delta' variable is then printed, specifically the attribute "days" which returns the number of days between the said two dates.

In this case, the output would be 9, as there are 9 days between July 2nd and July 11th in 2014.

"""
