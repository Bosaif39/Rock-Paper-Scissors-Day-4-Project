import random
player=input("Type 0 for rock, 1 for paper and 2 for scissors\n")
player=int(player)

#player pick
if(player==0):
    print("You choose rock\n")
elif(player==1):
    print("You choose paper\n")
    
elif(player==2):
    print("You choose scissors\n")

#PC pick
pc=random.randint(0,2)
if(pc==0):
    print("PC choose rock\n")
elif(pc==1):
    print("PC choose paper\n")
    
elif(pc==2):
    print("PC choose scissors\n")

#Draw
if(pc==player):
    print("Draw!!\n")
    
#rock vs scissors
elif(pc==0 and player==2):
    print("PC win\n")
elif(pc==2 and player==0):
    print("You win\n")
    
#paper vs rock
elif(pc==1 and player==0):
    print("PC win\n")
elif(pc==0 and player==1):
    print("You win\n")
    
#scissors vs paper
elif(pc==2 and player==1):
    print("PC win\n")
elif(pc==1 and player==2):
    print("You win\n")
