lists = [" "," "," "," "," "," "," "," "," "," "]
#lists = [0,1,2,3,4,5,6,7,8,9] updated here now we can use empty box

def board():
    print(f"{lists[1]}   |  {lists[2]}   |   {lists[3]}")
    print("----------------")
    print(f"{lists[4]}   |  {lists[5]}   |   {lists[6]}")
    print("----------------")
    print(f"{lists[7]}   |  {lists[8]}   |   {lists[9]}")
    print("\n")

'''def board():
    print("    |      |    ")
    print("----------------")
    print("    |      |    ")
    print("----------------")
    print("    |      |    ")
    print("\n")'''

def appends(userInput):
    if(userInput not in lists):
        lists.pop(userInput)
        if(inputs == 1):
          lists.insert(userInput,"x")
        else:
            lists.insert(userInput,"O")
def checkWin():
    if(lists[1]==lists[2] and lists[2] == lists[3] and lists[1]!= " "):
        return True
    if(lists[4]==lists[5] and lists[5] == lists[6] and lists[4]!= " "):
        return True
    if(lists[7]==lists[8] and lists[8] == lists[9] and lists[7]!= " "):
        return True
    if(lists[1]==lists[4] and lists[4] == lists[7] and lists[7]!= " "):
        return True
    if(lists[2]==lists[5] and lists[5] == lists[8]and lists[8]!= " "):
        return True
    if(lists[3]==lists[6] and lists[6] == lists[9] and lists[9]!= " "):
        return True
    if(lists[1]==lists[5] and lists[5] == lists[9] and lists[5]!= " "):
        return True
    if(lists[3]==lists[5] and lists[5] == lists[7] and lists[3]!= " "):
        return True
    else:
        return False
        
print("Welcome to TIC-TAC-TOE Game")
player1 = input("input your name : ")
player2 = input("input your name :")
print(f"Players activated .{player1}  is player-1")
print(f"Defending player-2 {player2}")
print("-------------let's play--------------")
board()
print("like if you input 1 then, the position 1 in index will be check")
for i in range(1,10):
    if(i%2 == 0):
        inputs = 1
        userInput = int(input("player 1 input the no: "))
        appends(userInput)
        board()
        win = checkWin()
        if(win == True):
          print(f"hurray !!!!{player2} you win \n i need party")
          break

    
    else:
        inputs = 2
        userInput = int(input("player 2 input the no: "))
        appends(userInput)
        board()
        win = checkWin()
        if(win == True):
            print(f"Hurray !!!!{player1}  you win \n i need party")
            break

else:
    print("game drawed ! noone won try next time")   
    
