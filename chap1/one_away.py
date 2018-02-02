
#helper function for one replace and delete
def oneReplace(s1,s2):
    flag=0
    for i,j in zip(s1,s2):
        if abs(len(s1)-len(s2))>1:
            return False
        else:
            if i!=j:
                flag+=1
    return flag<2 or flag<1

def oneInsert(s1,s2):
    if abs(len(s1)-abs(len(s2)))>1:
        return False
    elif abs(len(s1)-abs(len(s2)))==1:
        flag=0
        for i,j in zip(s1,s2):
            if i!=j:
                flag=+1
        return flag<1

def oneAway(s1,s2):
    if oneReplace(s1,s2) or oneInsert(s1,s2):
        return True
    else:
        return False
