#check if the parans are balanced
def paran_checker(s):
    stack=[]
    for t in s :
        if t=="{":
            stack.append(t)

        elif t=="}" and stack[len(stack)-1]:
            print(stack.pop())
        else:
            if len(stack)==0:
                return False

    if len(stack)==0:
        return True
    else:
        return False


print(paran_checker("{{}}"))




