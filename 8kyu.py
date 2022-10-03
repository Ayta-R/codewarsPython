# 'Wilson primes'
# Wilson primes satisfy the following condition. Let P represent a prime number.
# Then, ((P-1)! + 1) / (P * P) should give a whole number.
# Your task is to create a function that returns true if the given number is a Wilson prime.


def am_i_wilson(n):
    return n in (5, 13, 563)


# altERnaTIng cAsE <=> ALTerNAtiNG CaSe
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


# Task:
# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'  'word'   =>  'drow'
# solution
def solution(str):
    return str[::-1]


print(solution("moon"))  # any word
