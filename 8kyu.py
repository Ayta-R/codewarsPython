# Task: 'Wilson primes'
# Wilson primes satisfy the following condition. Let P represent a prime number.
# Then, ((P-1)! + 1) / (P * P) should give a whole number.
# Your task is to create a function that returns true if the given number is a Wilson prime.


def am_i_wilson(n):
    return n in (5, 13, 563)


# Task: altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_
# case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution
# for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.

def to_alternating_case(string):
    return "".join([c.swapcase() for c in string])


# Task:
# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:n, n is the number of
# customers to buy hotdogs, different numbers have different prices (refer to the following table), return a
# number that the customer need to pay how much money.
# solution

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return n * 90


# Task:  Training JS #7: if..else and ternary operator
# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'  'word'   =>  'drow'
# solution
def solution(str):
    return str[::-1]


print(solution("moon"))  # any word


# Task: MakeUpperCase
# Write a function which converts the input string to uppercase.

def make_upper_case(s):
    return s.upper()


# Task: Convert a String to a Number!
# We need a function that can transform a string into a number. What ways of achieving this do you know?
# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of
# an integral number.

def string_to_number(s):
    return int(s)


# Task Convert a Number to a String!
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

def number_to_string(num):
    return str(num)


# Task: Basic variable assignment
# This code should store "codewa.rs" as a variable called name but it's not working. Can you figure out why?

a = "code"
b = "wa.rs"
name = a + b


# Task: Multiply
# This code does not execute properly. Try to figure out why.

def multiply(a, b):
    return a * b


# Task: Check same case
# Write a function that will check if two given characters are the same case.
#
# If either of the characters is not a letter, return -1
# If both characters are the same case, return 1
# If both characters are letters, but not the same case, return 0

def same_case(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    if a.islower() and b.islower():
        return 1
    if a.isupper() and b.isupper():
        return 1
    else:
        return 0


# Task: Floating point comparison
# You have:
# a float value that comes from a computation and may have accumulated errors up to ±0.001
# a reference value
# a function approx_equals that compare the two values taking into account loss of precision; the function should
# return True if and only if the two values are close to each other, the maximum allowed difference is 0.001
# The function is bugged and sometimes returns wrong results.
# Your task is to correct the bug.

def approx_equals(a, b):
    diff = abs(a - b)
    return diff <= 0.001


# Task: Returning Strings
# Make a function that will return a greeting statement that uses an input; your program should return,
# "Hello, <name> how are you doing today?".
# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return "Hello, " + name + " how are you doing today?"


# Task: Grasshopper - Messi Goals
# Use variables to find the sum of the goals Messi scored in 3 competitions

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals
