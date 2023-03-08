class Solution(object):
    def isPalindrome(self, x):
        copy = x;
        sum = 0;
        while (x > 0):
            b = x % 10;
            sum = sum * 10 + b;
            x = x//10;
        if (sum == copy):
            return True;
        return False;