class Solution(object):
    def reverseVowels(self, s):
        l=0
        r=len(s)-1
        arr=[]
        for i in s:
            arr.append(str(i))
        v=['a','e','i','o','u','A','E','I','O','U']
        while l<r:
            if arr[l] in v and arr[r] in v:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            if arr[l] not in v: 
                l+=1
            if arr[r] not in v: 
                r-=1
        s=''
        for i in arr:
            s+=str(i)
        return s