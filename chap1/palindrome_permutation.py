
def palindromeChecker(s):
    holder={}
    countc=0
    for c in s:
            try:
                holder[c]+=1
            except KeyError:
                holder[c]=1
            if holder[c]%2==1:
                countc+=1
            else:
                countc-=1
    return countc <2
