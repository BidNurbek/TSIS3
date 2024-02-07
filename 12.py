def histogram(s):
    for x in s:
        print('*'*x)
        
s=list(map(int, input().split()))
histogram(s)