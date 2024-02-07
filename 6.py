def func(s):
    spl = s.split()
    rvs= " ".join(reversed(spl))
    return rvs
s = input()
print(func(s))