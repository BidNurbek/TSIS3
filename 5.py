from itertools import permutations

def fun(s):
    p = permutations(s)
    for x in p:
        print(x)
s = input()
fun(s)