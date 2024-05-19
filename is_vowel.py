"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
# Define a function called is_vowel that takes one parameter: char (a character).
def is_vowel(char):
    # Define a string called all_vowels containing all lowercase vowel characters.
    all_vowels = 'aeiou'

    # Check if the input character (char) is present in the all_vowels string.
    return char in all_vowels

# Call the is_vowel function with two different characters and print the results.
print(is_vowel('c'))  # Output: False (character 'c' is not a vowel)
print(is_vowel('e'))  # Output: True (character 'e' is a vowel)

"""
The said code defines a function called "is_vowel" which takes in one parameter "char". First, the function declares a variable "all_vowels" containing all lowercase vowels. The function then uses the "in" operator to check whether the value of "char" parameter is present within the "all_vowels" string, and returns the result.

In the last two lines the code call the function "is_vowel" twice, with the input values 'c' and 'e' and print the results.

In the first case, False will be returned, while in the second case, True will be returned.
"""
