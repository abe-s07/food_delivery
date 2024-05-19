"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).

exam_st_date = (11, 12, 2014)
Sample Output: The examination will start from : 11 / 12 / 2014
"""
# Define a tuple called 'exam_st_date' containing the exam start date in the format (day, month, year)
exam_st_date = (11, 12, 2014)

# Print the exam start date using string formatting
# The '%i' placeholders are filled with the values from the 'exam_st_date' tuple
print("The examination will start from : %i / %i / %i" % exam_st_date)

"""
Sample Output:

The examination will start from : 11 / 12 / 2014
Explanation:

The said code creates a tuple called "exam_st_date" containing three integers: 11, 12, and 2014. It then uses string formatting to print a string that states "The examination will start from :" followed by the integers in the tuple in the order they appear, formatted as day/month/year. The placeholders %i are used to format the integers.

The output would be: "The examination will start from : 11 / 12 / 2014".
"""
