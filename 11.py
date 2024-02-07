def fun(s):
    s1=""
    s1="".join(reversed(s))
    if s1==s:
        return True
    return False

s=input()
print(fun(s))