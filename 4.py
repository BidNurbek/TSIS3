def filter_prime(x):
    s = 0
    list = []
    num = x.split()
   
    for x in num:
        for i in range(1, 100):
            if int(x) % i == 0:
                s = s + 1
        if s == 2:
            list.append(x)
        s = 0
    return list

x = input()
print(filter_prime(x))