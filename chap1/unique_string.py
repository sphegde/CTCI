#ctci strings q1


#with an extra Data Structure
def uniqueString(s):
    checker={}
    for i in s:
        if i in checker:
            return False
        checker[i]=True
    return True


#without an extra Data Structure
def uniqueString2(s):
    return len(set(s))==len(s)


#compare each terms with other O(n^2)
def uniqueString3(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            print(s[i],"->",s[j])

            if s[i]==s[j]:
                return False
    return True

ss="sphegde"
print(uniqueString2(ss))
print(uniqueString(ss))
print(uniqueString3(ss))
