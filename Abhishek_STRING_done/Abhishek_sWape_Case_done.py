"""# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:

# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# Function Description

# Complete the swap_case function in the editor below.

# swap_case has the following parameters:

# string s: the string to modify
# Returns

# string: the modified string
# Input Format

# A single line containing a string .

# Constraints


# Sample Input 0

# HackerRank.com presents "Pythonist 2".
# Sample Output 0

# hACKERrANK.COM PRESENTS "pYTHONIST 2".
# Language
# Python 3
# More
# 1234567891011121314
# def swap_case(s):
#     r=""
#     for i in s :
#         if i.islower()  :
#             r+=i.upper()
            
#         elif i.isupper():
#             r+=i.lower()
             
#         else:

# Line: 1 Col: 1

# Test against custom input
# BlogScoringEnvironmentFAQAbout"""

# CODE:

def swap_case(s):
    r=""
    for i in s :
        if i.islower()  :
            r+=i.upper()
            
        elif i.isupper():
            r+=i.lower()
             
        else:
            r+=i
    return r       
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)