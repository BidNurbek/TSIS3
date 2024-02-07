def has_33(a):
    num=a
    for i in range(len(num)-1):
        if num[i]==3 and num[i+1]==3:
            return True
    return False

a = list(map(int, input().split()))
print(has_33(a))