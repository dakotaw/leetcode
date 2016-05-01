# Given a non-negative integer num, repeatedly add all its digits 
# until the result has only one digit.

class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return num % 9 or 9