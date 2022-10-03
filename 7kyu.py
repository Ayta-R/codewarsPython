# Task: lucky number
# Write a function to find if a number is lucky or not. If the sum of all digits is 0 or multiple of 9
# then the number is lucky 1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisible by 9, hence number is lucky.
# Function will return true for lucky numbers and false for others.

def is_lucky(n):
    return n % 9 == 0


# Task: Fix string case
# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and
# your task is to convert that string to either lowercase only or uppercase only based on: make as few changes
# as possible if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.


def solve(s):
    countUpper = 0
    countLower = 0
    for i in s:
        if i == i.upper():
            countUpper += 1
        else:
            countLower += 1

    if countUpper <= countLower:
        s = s.lower()
    else:
        s = s.upper()

    return s


# Task Switcheroo
# Given a string made up of letters a, b, and/or c, switch the position of letters a and b
# (change a to b and vice versa). Leave any incidence of c untouched.
# Example:
# 'acb' --> 'bca'
# 'aabacbaa' --> 'bbabcabb'

def switcheroo(s):
    return s.replace('a', 'x').replace('b', 'a').replace('x', 'b')


#Task Debug Sum of Digits of a Number
# Debug   function getSumOfDigits that takes positive integer to calculate sum of it's digits.
# Assume that argument is an integer.

def get_sum_of_digits(num):
    a = str(num)
    sum = 0
    for x in a:
        sum += int(x)
    return sum

#Task


















