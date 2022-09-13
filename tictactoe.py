'''

CSE210 
W01 Prove: Developer
Author: Jacob Sanchez Bejarano

'''

from turtle import update


def main():

    row1 = [1,2,3]
    row2 = [4,5,6]
    row3 = [7,8,9]

    print_template(row1,row2,row3)

    player = ""
    winner = "none"
    

    while winner == "none":

        if player == "":
            player = "x"
            
        elif player == "x":
            player = "o"
            
        elif player == "o":
            player = "x"
        
        
        winner = turn(player, row1,row2, row3)
    
        


def print_template(row1,row2,row3):
    print(f'{row1[0]}|{row1[1]}|{row1[2]}')
    print('-+-+-')
    print(f'{row2[0]}|{row2[1]}|{row2[2]}')
    print('-+-+-')
    print(f'{row3[0]}|{row3[1]}|{row3[2]}')


def turn(player, row1,row2, row3):
    
    winnerx = winner_rules("x",row1,row2, row3)
    winnero = winner_rules("o",row1,row2, row3)
    winner = "none"

    if winnerx == "x":
        print(f"Player {winnerx} wins")
        winner = winnerx
        
    elif winnero == "o":
        print(f"Player {winnero} wins")
        winner = winnero
        
    elif((row1.count("x")+row2.count("x")+row3.count("x")) == 5 or (row1.count("o")+row2.count("o")+row3.count("o")) == 5) and winner == "none":
        print("Draw")
        return  
    
    else:

        status = "retry"
        
        while status != "ok":

            position = int(input(f"{player}'s turn to choose a square (1-9): "))    

            if position <= 3:
                if row1[position-1] != "x" and row1[position-1] != "o":
                    row1[position-1] = player
                    status = "ok"
                else:
                    print("Choose another position.")
                    
            elif position <= 6:
                if row2[position-4] != "x" and row2[position-4] != "o":
                    row2[position-4] = player
                    status = "ok"
                else:
                    print("Choose another position.")
                    
            elif position <= 9:
                if row3[position-7] != "x" and row3[position-7] != "o":
                    row3[position-7] = player
                    status = "ok"
                else:
                    print("Choose another position.")
            
            print_template(row1,row2,row3)

    
    return winner




def winner_rules(player,row1,row2, row3):
    winner = "none"

    if row1[0] == player and row1[1] == player and row1[2] == player:
        winner = player
    if row2[0] == player and row2[1] == player and row2[2] == player:
        winner = player
    if row3[0] == player and row3[1] == player and row3[2] == player:
        winner = player
    if row1[0] == player and row2[0] == player and row3[0] == player:
        winner = player
    if row1[1] == player and row2[1] == player and row3[1] == player:
        winner = player    
    if row1[2] == player and row2[2] == player and row3[2] == player:
        winner = player  
    if row1[0] == player and row2[1] == player and row3[2] == player:
        winner = player
    if row1[2] == player and row2[1] == player and row3[0] == player:
        winner = player

    return winner    



if __name__ == '__main__':
    main()