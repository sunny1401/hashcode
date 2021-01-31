
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


def isHappy(self, n: int) -> bool:
    strn = str(n)
    solution = dict()
    while(True):
        if strn in solution:
            break
        sumv = sum(int(i)**2 for i in strn)
        if sumv == 1:
            return True
        solution[strn] = sumv
        strn = str(sumv)
    return False