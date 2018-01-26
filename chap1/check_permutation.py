# question 1.2 ctci

#using dict
def checkPerm(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        hasht={}
        for n in s1:
            if n in hasht:
                hasht[n]+=1
            else:
                hasht[n]=1
        for m in s2:
            if m not in hasht:
                return False
            else:
                hasht[n]-=1
        return True


#sorting the string
def bySort(s1,s2):
    a1=sorted(s1)
    b2=sorted(s2)
    return a1==b2

print(checkPerm("fdss","ssfd"))
print(bySort("fdss","ssfd"))
