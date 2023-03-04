s=set(arr)
        x=len(arr)+k+1
        for i in range(1,x):
            if i not in s:
                if k==1:
                    return i
                k-=1