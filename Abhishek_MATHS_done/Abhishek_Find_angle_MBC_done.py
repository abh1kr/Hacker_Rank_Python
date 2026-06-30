""" is a right triangle,  at .
Therefore, .

Point  is the midpoint of hypotenuse .

You are given the lengths  and .
Your task is to find  (angle , as shown in the figure) in degrees.

Input Format

The first line contains the length of side .
The second line contains the length of side .

Constraints


Lengths  and  are natural numbers.
Output Format

Output  in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.


Sample Input

10
10
Sample Output

45°"""

# CODE:
import math
AB_per=int(input())
BC_Base=int(input())
AC= pow((AB_per **2) + (BC_Base **2),0.5)
BC_new=BC_Base/2
MC=AC/2


thetha= BC_new/MC
radian=math.acos(thetha)
degree=math.degrees(radian)
# degree_new=round(degree)


print(f"{round(degree)}\u00B0")



