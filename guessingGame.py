import random
flag = True
while flag:
    num = input("Type a number for an upper limit :")
    

    if num.isdigit():
        print("Lets play ")
        num = int(num)
        flag = False
    else:
        print("Invalid Input Try Again ")

secert = random.randint(1,num)


guess = None
count = 1 

while guess!= secert :
    guess=input("Please type a number Between 1 And  "    + str(num)   +      "  : ")
    if guess.isdigit():
        guess = int(guess)


    if guess == secert :
        print("You Got it ")
    else:
        print("Try Again ")
        count += 1

print("it took you ", count," guess")
