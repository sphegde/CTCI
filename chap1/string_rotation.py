#s1 given string, s2 possible rotation
def stringRotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        s=s1+s1
        if isSubstring(s,s2):
            return True
        else:
            return False



def isSubstring(s1,s2):
    return s2 in s1
