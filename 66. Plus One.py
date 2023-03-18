class Solution(object):
    def plusOne(self, digits):
        digits=[str(i) for i in digits]
        s=''.join(digits)
        a=int(s)+1
        l=list(str(a))
        l=[int(i) for i in l]
        return l