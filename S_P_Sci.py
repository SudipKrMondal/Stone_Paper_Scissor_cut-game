import random



def gameWin(n,user):
    if n==user:
        return None
    elif n==1:
        if user==2:
            return True
        elif user==3:
            return False

    elif n==2:
        if user==3:
            return True
        elif user==1:
            return False

    elif n==3:
        if user==1:
            return True
        elif user==2:
            return False

n=random.randint(1,3)


user=int(input("Enter your choice: Stone(1), Paper(2) or Scissor(3):   "))

a=gameWin(n,user)

print(f"Computer Chose: {n}")
print(f"You Chose: {user}")
if a== None:
    print("Game has been Tie: ")
elif a== True:
    print("You Win!!")
else:
    print("You Lose!!!")
