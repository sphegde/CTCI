def stringComp(s):
    holder={}
    result=[]
    for c in s:
        try :
            holder[c]+=1
        except KeyError:
            holder[c]=1
    for i in holder:
        result.append(i)
        result.append(holder[i])
    return result
