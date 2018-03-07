from random import randint
def comp():
        ch = randint(1,3)
        if ch == 1:
                com='r'
        elif ch == 2:
                com='p'
        else:
                com='s'
        return com

def win(p1,com):
        if p1 == com:
                print('Draw!')
        elif p1 == 'r' and com == 's':
                print('\nYou Win!')
        elif p1 == 'r' and com == 'p':
                print('\nComputer Wins!')
        elif p1 == 'p' and com == 'r':
                print('\nYou Win!')
        elif p1 == 'p' and com == 's':
                print('\nComputer Wins!')
        elif p1 == 's' and com == 'p':
                print('\nYou Win!')
        elif p1 == 's' and com == 'r':
                print('\nComputer Wins!')

def game():
        print("\nYOU VS COMPUTER ")
        print("\nSelect from one of this option : \n rock (r), \n paper (p)  \n scissor (s) ")
        p1 = input()
        if p1=='r':
                p11="Rock"
        elif p1 == 'p':
                p11="Paper"
        else:
                p11="Scissor"
                
        print(p11, 'VS ' , end='')
        computer = comp()
        if computer=='r':
                computer11="Rock"
        elif computer == 'p':
                computer11="Paper"
        else:
                computer11="Scissor"
        print(computer11)
        win(p1,computer)

print("Want to Play Rock, Paper, Scissors :: ", "Yes (y) or No (n)")
ch1=input()
while ch1 == 'y':
        game()
        print("\n\nWhat to play again :: ", "Yes (y) or No (n)")
        ch1 = input()

print("Bbye")
        

        

