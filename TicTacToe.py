import os

def createBoard(xState, zState):
    zero = 'X' if xState[0] else('O' if zState[0] else 0)
    one = 'X' if xState[1] else('O' if zState[1] else 1)
    two = 'X' if xState[2] else('O' if zState[2] else 2)
    three = 'X' if xState[3] else('O' if zState[3] else 3)
    four = 'X' if xState[4] else('O' if zState[4] else 4)
    five = 'X' if xState[5] else('O' if zState[5] else 5)
    six = 'X' if xState[6] else('O' if zState[6] else 6)
    seven = 'X' if xState[7] else('O' if zState[7] else 7)
    eight = 'X' if xState[8] else('O' if zState[8] else 8)

    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def sum(a, b, c):
    return a+b+c


def chechWinner(xState, zState):
    Wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in Wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            return 0
    return -1

if __name__ == "__main__":
    while(True):
        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1  # 1 for X and 0 for O
        isDraw = 0
        regame = 'n'
        print("Tic Tac Toe")
        while(True):
            os.system('cls')
            createBoard(xState, zState)
            if(turn == 1):
                print("\nX's Chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
            else:
                print("\nO's Chance")
                value = int(input("Please enter a value: "))
                zState[value] = 1

            cwin = chechWinner(xState, zState)

            if(cwin == 1):
                os.system('cls')
                createBoard(xState, zState)
                print("\nX won the match")
                print("\nDo you want to play again")
                regame = input("Press 'Y' for Yes 'N' for No : ")
                break
            elif(cwin == 0):
                os.system('cls')
                createBoard(xState, zState)
                print("\nO won the match")
                print("\nDo you want to play again")
                regame = input("Press 'Y' for Yes 'N' for No : ")
                break

            if(isDraw == 8):
                os.system('cls')
                createBoard(xState, zState)
                print("\nMatch Draw!!")
                print("\nDo you want to play again")
                regame = input("Press 'Y' for Yes 'N' for No : ")
                break

            isDraw += 1
            turn *= -1
        if(regame != 'Y' and regame !='y'):
            break
