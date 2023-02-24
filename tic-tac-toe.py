def structure():
    print("|   |   |   |\n")
    print(f"| {a[6]} | {a[7]} | {a[8]} |\n")
    print("|   |   |   |\n")
    print("-------------\n")
    print("|   |   |   |\n")
    print(f"| {a[3]} | {a[4]} | {a[5]} |\n")
    print("|   |   |   |\n")
    print("-------------\n")
    print("|   |   |   |\n")
    print(f"| {a[0]} | {a[1]} | {a[2]} |\n")
    print("|   |   |   |\n")
a=[" "," "," "," "," "," "," "," "," "]
i=0
r=['X','O']
while i==0:
    player1=input("would you like to play as X or O: ").upper()
    if player1 not in r:
        print("you can only enter x or o")
    else:
        break

if player1=='X':
    player2='O'
else:
    player2='X'
def win():
    if a[6]==a[7]==a[8]!=" ":
        return True
    if a[4]==a[5]==a[3]!=" ":
        return True
    if a[2]==a[1]==a[0]!=" ":
        return True
    if a[0]==a[3]==a[6]!=" ":
        return True
    if a[1]==a[7]==a[4]!=" ":
        return True
    if a[2]==a[5]==a[8]!=" ":
        return True
    if a[0]==a[4]==a[8]!=" ":
        return True
    if a[2]==a[4]==a[6]!=" ":
        return True
    else:
        return False 
while win()==False:
    while i==0:
        b=int(input("player1 enter a value from 1-9: "))
        if a[b-1] in r:
            print("oops, it was already taken by the other player")
            continue
        else:
            break
    a[b-1]=player1
    structure()
    if win()==False:
        while i==0:
            c=int(input("player2 enter a value from 1-9: "))
            if a[c-1] in r:
                print("oops, it was already taken by the other player")
                continue
            else:
                break
        a[c-1]=player2   
        structure()
        if win()==True:
            print("congrats player2 you won")
        else:
            continue
    else:
        print("congrats player1 you won")



