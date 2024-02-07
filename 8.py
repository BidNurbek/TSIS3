def spy_game(nums):
    s=0
    for i in range(len(nums)):
        if s==0 or s==1:
            if nums[i]==0:
                s+=1
        elif s==2:
            if nums[i]==7:
                return True
    return False

            


nums=list(map(int, input().split()))
print(spy_game(nums))