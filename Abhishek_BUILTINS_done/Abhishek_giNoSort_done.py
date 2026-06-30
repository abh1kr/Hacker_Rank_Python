"""You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324"""
# CODE:
s=input()
def sort(c):
    for i in c:
        if i.islower():
            return (0,i)
        elif i.isupper():
            return (1,i)
        elif i.isdigit():
            if(int(i)%2!=0):
                return (2,i)
            else:
                return (3,i)
result = ''.join(sorted(s, key=sort))
print(result)
