# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution(object):
           
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversed = 0
        sign = 1
        if x < 0:
            sign = -1    
            x = -x 
        while x != 0:
            digit = x % 10
            x = x / 10
            reversed = reversed * 10 + digit

        reversed = sign*reversed
        if reversed < -2**31 or reversed > 2**31 - 1:
            return 0  
        
        return reversed
