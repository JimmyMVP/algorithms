"""
Calculate number of permutations of a string.
Also calculate factorial to check if the solution is correct
"""


def factorial(x):
    fac = 1
    for i in range(1,x+1):
        fac*=i
    return fac

def num_permutations(s):

    if(len(s) == 0):
        return 1
    n = 0
    for i in range(len(s)):
        n+= num_permutations(s[:i] + s[i+1:])
    return n


s = 'marin'
print(num_permutations(s))
print(factorial(len(s)))