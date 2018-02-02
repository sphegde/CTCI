#using extra ds
def urlify(s):
    newString=[]
    for c in s:
        if c==" ":
            newString.append("%20")
        else:
            newString.append(c)
    return newString
