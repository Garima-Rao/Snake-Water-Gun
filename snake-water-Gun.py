import random
print("welcome to Snake, Water and Gun game")
print("This is three round game\nenter\n 0 for snake\n 1 for Water\n 2 for Gun")
name=input("enter your name:")
round=0
user_score=0
comp_score=0
while(round!=3):
 
 user_choice=input("enter your choice:")
 comp_choice=random.randint(0,2)
 if comp_choice==0:
    print("Bot choice=Snake")
 if comp_choice==1:
    print("Bot choice=Water")
 if comp_choice==2:
    print("Bot choice=Gun")
 if int(user_choice)==0:
    print(name+" choice=Snake")
 if int(user_choice)==1:
    print(name+" choice=Water")
 if int(user_choice)==2:
    print(name+" choice=Gun")
 if int(user_choice)==comp_choice:
    print("draw")
 elif int(user_choice)==0 and comp_choice==1 or int(user_choice)==2 and comp_choice==0 or int(user_choice)==2 and comp_choice==1:
    print(name+" won")
    user_score+=1
 elif int(user_choice)==0 and comp_choice==2 or int(user_choice)==1 and comp_choice==2:
    print("Bot won")
    comp_score+=1
# elif user_choice==choice[1] and comp_choice==1:
#     print("Bot won")
 else:
    print("invalid input")
 round+=1
if user_score>comp_score:
   print("🥳🥳 winner is "+name+"🏆🏆")
elif user_score<comp_score:
   print("🥳🥳 winner is Bot🏆🏆")
else:
   print("Game is draw")
