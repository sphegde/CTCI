# question 1.2 ctci

#using dict
def checkPerm(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        hasht={}
        v=0
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
    S1=sorted(s1)
    S2=sorted(s2)
    return S1==S2

print(checkPerm("fdss","ssfd"))
print(bySort("fdss","ssfd"))











#sorting strings and comparing
