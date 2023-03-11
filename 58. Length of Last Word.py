class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        i=len(s)-1
        count=0
        while(s[i]!=' '):
            count+=1
            if i==0:
                break
            i-=1
        return count