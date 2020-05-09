from numpy import *
arr=array([[0 for x in range(3)]for y in range(3)])
print("Player1 will always go first, decide among yourself who will be Player1 and who will be Player2..Happy play..")
print(arr)
print("You CAN'T CHOOSE THE PLACES WHICH ARE ALREADY FILLED WITH 1'S AND 2'S !!!")
for z in range(10):
    a = input("Player1 or Player2: ")
    if a=='Player1'.lower():
        i=int(input(""))
        j=int(input(""))
        arr[i][j]=1
        print("player2 turn")
    else:
        i = int(input(""))
        j = int(input(""))
        arr[i][j]=2
        print("player1 turn")
    print("You CAN'T CHOOSE THE PLACES WHICH ARE ALREADY FILLED WITH 1'S AND 2'S !!!")

    print(arr)
    if  arr[0][0]==1 and arr[0][1]==1 and arr[0][2]==1:
        print("Player1 WON")
        break
    elif  arr[0][0]==2 and arr[0][1]==2 and arr[0][2]==2:
        print("Player2 WON")
        break
    elif arr[1][0]==1 and arr[1][1]==1 and arr[1][2]==1:
        print("Player1 WON")
        break
    elif arr[1][0]==2 and arr[1][1]==2 and arr[1][2]==2:
        print("Player2 WON")
        break
    elif arr[2][0]==1 and arr[2][1]==1 and arr[2][2]==1:
        print("Player1 WON")
        break
    elif arr[2][0]==2 and arr[2][1]==2 and arr[2][2]==2:
        print("Player2 WON")
        break
    elif arr[1][0]==2 and arr[1][1]==2 and arr[1][2]==2:
        print("Player2 WON")
        break
    elif arr[0][0]==1 and arr[1][1]==1 and arr[2][2]==1:
        print("Player1 WON")
        break
    elif arr[0][2]==1 and arr[1][1]==1 and arr[2][0]==1:
        print("Player1 WON")
        break
    elif arr[0][0]==2 and arr[1][1]==2 and arr[2][2]==2:
        print("Player2 WON")
        break
    elif arr[0][2]==2 and arr[1][1]==2 and arr[2][0]==2:
        print("Player2 WON")
        break
    elif arr[0][0]==2 and arr[1][0]==1 and arr[2][0]==1:
        print("Player1 WON")
        break
    elif arr[0][0]==2 and arr[1][0]==2 and arr[2][0]==2:
        print("Player2 WON")
        break
    elif arr[0][1]==2 and arr[1][1]==2 and arr[2][1]==1:
        print("Player1 WON")
        break
    elif arr[0][1]==2 and arr[1][1]==2 and arr[2][1]==2:
        print("Player2 WON")
        break
    elif arr[0][2]==1 and arr[1][2]==1 and arr[2][2]==1:
        print("Player1 WON")
        break
    elif arr[0][2]==2 and arr[1][2]==2 and arr[2][2]==2:
        print("Player2 WON")
        break
if True:
    print("THANKS FOR PLAYING!!!")
    print("GOOD BYE!!! TAKE CARE")
else:
    print("DRAW")
