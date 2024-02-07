def  solve(numheads, numlegs):
     r=(numlegs-2*numheads)/2
     c=numheads-r
     return r, c
     
print(solve(35, 94))