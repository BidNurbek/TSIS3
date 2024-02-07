def fun(lst):
    lst1=[]
    for x in lst:
        if x not in lst1:
            lst1.append(x)
    return lst1


lst=list(map(int,input().split()))
print(*fun(lst))