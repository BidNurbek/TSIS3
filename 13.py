print("Hello! What is your name?")
def fun():
    import random
    cnt=0
    s=input()
    print("Well, KBTU, I am thinking of a number between 1 and 20.")
    r = random.randint(1, 20)
    x=0
    while x!=r:
        print("Take a guess.")
        x = int(input())
        cnt+=1
        if x==r:
            print(f"Good job, KBTU! You guessed my number in {cnt} guesses!")
fun()
