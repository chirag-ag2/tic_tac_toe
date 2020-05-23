#TicTacToeForLocalAndComputer
import os
from random import choice
d={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
p1=""
p2=""
d1={}

def result():
    for i in range(1,10,3):
        if d[str(i)]==d[str(i+1)]==d[str(i+2)]==d1[p1]:
            return 1
        elif d[str(i)]==d[str(i+1)]==d[str(i+2)]==d1[p2]:
            return 2
    for i in range(1,4):
        if d[str(i)]==d[str(i+3)]==d[str(i+6)]==d1[p1]:
            return 1
        elif d[str(i)]==d[str(i+3)]==d[str(i+6)]==d1[p2]:
            return 2
    if d["1"]==d["5"]==d["9"]==d1[p1]:
        return 1
    elif d["1"]==d["5"]==d["9"]==d1[p2]:
        return 2
    elif d["3"]==d["5"]==d["7"]==d1[p1]:
        return 1
    elif d["3"]==d["5"]==d["7"]==d1[p2]:
        return 2        
    else:
        return 0
            

def sample():
    print("\n-------------------")
    for i in range(1,10,3):
        print("|  ",end="")
        for j in range (0,3):
            print(i+j,end="  |  ",sep="")
        print("\n-------------------")




def board():
    print("\n-------------------")
    for i in range(1,10,3):
        print("|  ",end="")
        for j in range (0,3):
            print(d[str(i+j)],end="  |  ",sep="")
        print("\n-------------------")
    


    
def comp():
    global d,d1,p1,p2
    p1=input("Enter Name: ")
    while True:
        s1=input("Enter Your Symbol('X' or 'O'): ")
        s1=s1.upper()
        if s1=="X":
            s2="O"
            break
        elif s1=="O" or s1=="0" :
            s1="O"
            s2="X"
            break
        else:
            print("Choose valid symbol.")
    p2="Computer"
    gameStarter=choice((0,1))
    l=["1","2","3","4","5","6","7","8","9"]
    d1={p1:s1,p2:s2}
    print(f"Symbol of {p1} is: {s1}\nSymbol of {p2} is: {s2}.")
    input("Press Any Key To Continue")
    os.system("cls")
    i=0
    while len(l)!=0:   
        print("Available Places: ",*l)
        if(i%2!=gameStarter):
            x=input(f"{p1}'s Turn: ")
            if x in l:
                d[x]=d1[p1]
                board()
                k=result()
                if k==1:
                    print(f"{p1} Won.")
                    return
                elif k==2:
                    print(f"{p2} Won.")
                    return
                i+=1
                l.remove(x)
            else:
                print("Invalid Location")
        else:
            x=choice(l)
            print("Computer Chooses: ",x)
            if x in l:
                d[x]=d1[p2]
                board()
                k=result()
                if k==1:
                    print(f"{p1} Won.")
                    return
                elif k==2:
                    print(f"{p2} Won.")
                    return
                i+=1
                l.remove(x)
            else:
                print("Invalid Location")
    k=result()
    if k==1:
        print(f"{p1} Won.")
        return
    elif k==2:
        print(f"{p2} Won.")
        return
    else:
        print("Match Tied")
    
    
    
    
    
    

def local():
    global d,d1,p1,p2   
    p1=input("Enter Name of 1st Player: ")
    p2=input("Enter Name of 2nd Player: ")
    l=["1","2","3","4","5","6","7","8","9"]
    x=p1
    y=p2
    p1=choice((x,y))
    gameStarter=choice((0,1))
    if p1==x:
        p2=y
    elif p1==y:
        p2=x
    d1={p1:"X",p2:"O"}
    print(f"Symbol of {p1} is:X\nSymbol of {p2} is:O.")
    input("Press Any Key To Continue")
    os.system("cls")
    i=0
    while len(l)!=0:   
        print("Available Places: ",*l)
        if(i%2!=gameStarter):
            x=input(f"{p1}'s Turn: ")
            if x in l:
                d[x]=d1[p1]
                board()
                k=result()
                if k==1:
                    print(f"{p1} Won.")
                    return
                elif k==2:
                    print(f"{p2} Won.")
                    return
                i+=1
                l.remove(x)
            else:
                print("Invalid Location")
        else:
            x=input(f"{p2}'s Turn: ")
            if x in l:
                d[x]=d1[p2]
                board()
                k=result()
                if k==1:
                    print(f"{p1} Won.")
                    return
                elif k==2:
                    print(f"{p2} Won.")
                    return
                i+=1
                l.remove(x)
            else:
                print("Invalid Location")
    k=result()
    if k==1:
        print(f"{p1} Won.")
        return
    elif k==2:
        print(f"{p2} Won.")
        return
    else:
        print("Match Tied")        
        
        
        
print("Press Any Key To Start The Game.".center(70,"-"))
input()
ch="0"
 
os.system("cls")
while ch!="4": 
    
    ch=input("""Press 1. To Show Game Board
Press 2. To Start the new game with local players
Press 3. To Start the new game with computer
Press 4. To Exit
""")
    
    if ch=="1":
        sample()
    elif ch=="2":
        os.system("cls")
        d={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
        local()
    elif ch=="3":
        os.system("cls")
        d={"1":" ","2":" ","3":" ","4":" ","5":" ","6":" ","7":" ","8":" ","9":" "}
        comp()
    elif ch=="4":
        break
    else:
        print("Press Valid Button")
    input("Press Any Key To Continue")
    os.system("cls")   
        
        