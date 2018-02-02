#check if the parans are balanced
def paran_checker(s):
    stack=[]
    parans={"]":"[", "}" : "{" ,  ")" : "(" }
    for char in s :
        if char==parans.values():
            stack.append(char)
        elif char in parans.keys():
                if stack == [] or parans[char] != stack.pop():
                    return False
        else:
                return False
        return stack == []
