import random
print("Welcome to Stone Paper Scissor Game ")
un1=input("Enter Player name : ")
un=un1.capitalize()
print(f"{un} Vs. Computer")
print("-----------Let's Begin------------")
a=["stone","paper","scissor"]
i=1
user=0
comp=0
while(i<=10):
    c = input("Enter a choice out of Stone Paper or Sissor : ")
    c1 = random.choice(a)
    c2=c.lower()
    if c1==c2:
        print(f"Both got {c} so no points awarded.")
        user=user+0
        comp=comp+0
        print(f"{un} : {user}       Computer : {comp}")
    elif c1=="stone" and c2=="scissor" :
        print("Computer got one point as Stone breaks Scissor")
        comp = comp + 1
        print(f"{un} : {user}       Computer : {comp}")
    elif c1 == "stone" and c2 == "paper":
        print("User got one point as Paper Wraps Stone")
        user = user + 1
        print(f"{un} : {user}       Computer : {comp}")
    elif c1=="paper" and c2=="scissor":
        print("User got one point as Scissor cuts paper")
        user = user + 1
        print(f"{un} : {user}       Computer : {comp}")
    elif c1=="paper" and c2=="stone" :
        print("Computer got one point as Paper Wraps Stone")
        comp = comp + 1
        print(f"{un} : {user}       Computer : {comp}")
    elif c1=="scissor" and c2=="stone":
        print("User got one point as Stone breaks Scissor")
        user = user + 1
        print(f"{un} : {user}       Computer : {comp}")
    elif c1=="scissor" and c2=="paper":
        print("Coputer got one point as Scissor cuts paper")
        comp = comp + 1
        print(f"{un} : {user}       Computer : {comp}")
    else:
        print("Wrong Choice!!!!!!!")
        print("Enter Your Choice Again")
        i=i-1
    i=i+1
if user > comp:
    print(f"{un} Won!!!!")
elif user==comp :
    print("Draw!!!!")
else:
    print(f"{un} Lose!!!!")



