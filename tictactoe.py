# My first tic-tac-toe program, by Al Sweigart al@inventwithpython.com
# This sure was a lot of typing, but I finally finished it!

# (This is a joke program.)

import sys
if sys.version_info[0] == 2:
    input = raw_input # python 2 compatibility
print('Welcome to Tic Tac Toe so hype! I know I have good judgment, I know I have good taste
It's funny and it's ironic that only I feel that way
I promise 'em that you're different and everyone makes mistakes
But just don't
I heard that you're an actor, so act like a stand-up guy
Whatever devil's inside you, don't let him out tonight
I tell them it's just your culture and everyone rolls their eyes
Yeah, I know
All I'm asking, baby

Please, please, please
Don't prove I'm right
And please, pleasе, please
Don't bring me to tеars when I just did my makeup so nice
Heartbreak is one thing, my ego's another
I beg you, don't embarrass me, motherfucker, oh
Please, please, please (Ah)')
print('You are X.\n')

print(' | | \n-+-+-\n | | \n-+-+-\n | | \n')
print('Enter the number of your move:')
print('  789\n  456\n  123')
move = input()

if move == '1':
    print('O moves on the top-left space.')
    print('O| | \n-+-+-\n | | \n-+-+-\nX| | \n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '2':
        print('O moves on the bottom-right space.')
        print('O| | \n-+-+-\n | | \n-+-+-\nX|X|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the center space.')
            print('O| | \n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O| \n-+-+-\n |X| \n-+-+-\nX|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O|O|X\n-+-+-\n |X| \n-+-+-\nX|X|O\n')
                print('You have won!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| | \n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X| \n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '3':
        print('O moves on the bottom-center space.')
        print('O| | \n-+-+-\n | | \n-+-+-\nX|O|X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX| | \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '5':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\n |X| \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\n | |X\n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '8':
            print('O moves on the top-right space.')
            print('O|X|O\n-+-+-\n | | \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '9':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O| |X\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the right space.')
                print('O|X|X\n-+-+-\n |O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '4':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\nX| | \n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-right space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
    if move == '5':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\n |X| \n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('O|X|O\n-+-+-\n |X| \n-+-+-\nX|O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '6':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\n | |X\n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n | |X\n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n | |X\n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-right space.')
            print('O|X|O\n-+-+-\n | |X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\n |X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nX|O|O\n')
                    print('You have won!')
                    sys.exit()
    if move == '8':
        print('O moves on the bottom-right space.')
        print('O|X| \n-+-+-\n | | \n-+-+-\nX| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the center space.')
            print('O|X| \n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('O|X| \n-+-+-\nX|O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print('O|X| \n-+-+-\n |X| \n-+-+-\nX|O|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the right space.')
                print('O|X| \n-+-+-\nX|X|O\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nX|O|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X| \n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|X|X\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '9':
                print('O|X|X\n-+-+-\n |X| \n-+-+-\nX|O|O\n')
                print('You have won!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O|X| \n-+-+-\n |O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '9':
        print('O moves on the center space.')
        print('O| |X\n-+-+-\n |O| \n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the bottom-center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O| |X\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the right space.')
                print('O|X|X\n-+-+-\n |O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '4':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-right space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
if move == '2':
    print('O moves on the top-left space.')
    print('O| | \n-+-+-\n | | \n-+-+-\n |X| \n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the bottom-right space.')
        print('O| | \n-+-+-\n | | \n-+-+-\nX|X|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the center space.')
            print('O| | \n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O| \n-+-+-\n |X| \n-+-+-\nX|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O|O|X\n-+-+-\n |X| \n-+-+-\nX|X|O\n')
                print('You have won!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| | \n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X| \n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '3':
        print('O moves on the bottom-left space.')
        print('O| | \n-+-+-\n | | \n-+-+-\nO|X|X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX| | \n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO|X| \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO| |X\n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO| | \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO| | \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
    if move == '4':
        print('O moves on the bottom-left space.')
        print('O| | \n-+-+-\nX| | \n-+-+-\nO|X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '3':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX| | \n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the right space.')
            print('O| | \n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the top-center space.')
                print('O|O| \n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O|X| \n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('You have won!')
                sys.exit()
            if move == '9':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\nO|X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the top-right space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-right space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-right space.')
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X| \n-+-+-\nX|O| \n-+-+-\nO|X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-right space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-right space.')
                print('O|X|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '9':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\nX| | \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the right space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '5':
        print('O moves on the top-center space.')
        print('O|O| \n-+-+-\n |X| \n-+-+-\n |X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\n |X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\n |X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\n |X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print('O|O|X\n-+-+-\n |X| \n-+-+-\nO|X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the left space.')
                print('O|O|X\n-+-+-\nO|X| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X| \n')
                print('The computer wins!')
                sys.exit()
    if move == '6':
        print('O moves on the bottom-left space.')
        print('O| | \n-+-+-\n | |X\n-+-+-\nO|X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '3':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO| |X\n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\nO|X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the top-right space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-right space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-right space.')
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO|X|X\n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO| |X\n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO| |X\n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
    if move == '8':
        print('O moves on the center space.')
        print('O|X| \n-+-+-\n |O| \n-+-+-\n |X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the bottom-right space.')
            print('O|X| \n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the bottom-left space.')
            print('O|X| \n-+-+-\n |O| \n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X| \n-+-+-\nO|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-right space.')
            print('O|X| \n-+-+-\nX|O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-right space.')
            print('O|X| \n-+-+-\n |O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-right space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '9':
        print('O moves on the bottom-right space.')
        print('O| |X\n-+-+-\n | | \n-+-+-\n |X|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n |X| \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the right space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O|X|X\n-+-+-\n |X| \n-+-+-\nO|X|O\n')
                print('You have won!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
if move == '3':
    print('O moves on the top-left space.')
    print('O| | \n-+-+-\n | | \n-+-+-\n | |X\n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the bottom-center space.')
        print('O| | \n-+-+-\n | | \n-+-+-\nX|O|X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX| | \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '5':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\n |X| \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\n |X|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\n | |X\n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '8':
            print('O moves on the top-right space.')
            print('O|X|O\n-+-+-\n | | \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\n |X|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '9':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O| |X\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the right space.')
                print('O|X|X\n-+-+-\n |O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '2':
        print('O moves on the bottom-left space.')
        print('O| | \n-+-+-\n | | \n-+-+-\nO|X|X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX| | \n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO|X| \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO| |X\n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO| | \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO| | \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
    if move == '4':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\nX| | \n-+-+-\n | |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\n |X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\n | |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| |X\n-+-+-\n | |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-left space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\nX|X| \n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nO|O|X\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
    if move == '5':
        print('O moves on the bottom-left space.')
        print('O| | \n-+-+-\n |X| \n-+-+-\nO| |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO|X| \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the right space.')
            print('O| | \n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O| \n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X| \n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the bottom-center space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O| | \n-+-+-\nO|X|X\n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO|X| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
    if move == '6':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\n | |X\n-+-+-\n | |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n | |X\n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n | |X\n-+-+-\n |X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| |X\n-+-+-\n | |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\n | |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-left space.')
            print('O|X|O\n-+-+-\n | |X\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO| |X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
    if move == '8':
        print('O moves on the bottom-left space.')
        print('O|X| \n-+-+-\n | | \n-+-+-\nO| |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO| | \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-right space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\nX|X| \n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nO|O|X\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO|X| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO| |X\n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO| | \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
    if move == '9':
        print('O moves on the right space.')
        print('O| |X\n-+-+-\n | |O\n-+-+-\n | |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the bottom-center space.')
            print('O| |X\n-+-+-\n | |O\n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O| |X\n-+-+-\n |X|O\n-+-+-\nX|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\n |O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '2':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n | |O\n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO| |O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nX| |O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n |X|O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO|X|O\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the bottom-left space.')
            print('O|X|X\n-+-+-\n | |O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO| |O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO|X|O\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
if move == '4':
    print('O moves on the top-left space.')
    print('O| | \n-+-+-\nX| | \n-+-+-\n | | \n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\nX| | \n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| |X\n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-right space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
    if move == '2':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\nX| | \n-+-+-\n |X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| | \n-+-+-\n |X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\n |X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX| |X\n-+-+-\n |X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X|O\n-+-+-\nX|O| \n-+-+-\n |X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the bottom-right space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO|X| \n')
                print('The computer wins!')
                sys.exit()
    if move == '3':
        print('O moves on the bottom-left space.')
        print('O| | \n-+-+-\nX| | \n-+-+-\nO| |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX| | \n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the right space.')
            print('O| | \n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O| \n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X| \n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-right space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('You have won!')
                sys.exit()
        if move == '8':
            print('O moves on the top-right space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\nX|X| \n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nO|O|X\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
        if move == '9':
            print('O moves on the right space.')
            print('O| |X\n-+-+-\nX| |O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '5':
        print('O moves on the right space.')
        print('O| | \n-+-+-\nX|X|O\n-+-+-\n | | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX|X|O\n-+-+-\nX| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the bottom-right space.')
                print('O| |O\n-+-+-\nX|X|O\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\nX| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
        if move == '2':
            print('O moves on the top-center space.')
            print('O|O| \n-+-+-\nX|X|O\n-+-+-\n |X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\nX|X| \n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\n |X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '3':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX|X|O\n-+-+-\n | |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\nX| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '2':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\n |X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('O|X| \n-+-+-\nX|X|O\n-+-+-\n |O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the bottom-left space.')
                print('O|X| \n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '6':
        print('O moves on the center space.')
        print('O| | \n-+-+-\nX|O|X\n-+-+-\n | | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the bottom-right space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the bottom-right space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX|O|X\n-+-+-\n | |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|O|X\n-+-+-\nX| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '2':
                print('O moves on the bottom-left space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the bottom-right space.')
            print('O|X| \n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '8':
        print('O moves on the top-right space.')
        print('O|X|O\n-+-+-\nX| | \n-+-+-\n | | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the bottom-right space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print('O|X|O\n-+-+-\nX|O| \n-+-+-\n |X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the bottom-right space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO|X| \n')
                print('The computer wins!')
                sys.exit()
        if move == '3':
            print('O moves on the bottom-left space.')
            print('O|X|O\n-+-+-\nX| | \n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\nX|X| \n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nO|O|X\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print('O|X|O\n-+-+-\nX|X| \n-+-+-\n |O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O|X|O\n-+-+-\nX|X|X\n-+-+-\n |O| \n')
                print('You have won!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O|X|O\n-+-+-\nX|O|X\n-+-+-\n | | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the bottom-right space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '2':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO|X| \n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the bottom-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
    if move == '9':
        print('O moves on the bottom-right space.')
        print('O| |X\n-+-+-\nX| | \n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nX|X| \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the right space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O| |X\n-+-+-\nX|X|X\n-+-+-\nO| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\nX|O| \n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
if move == '5':
    print('O moves on the top-left space.')
    print('O| | \n-+-+-\n |X| \n-+-+-\n | | \n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\n |X| \n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('O|X|O\n-+-+-\n |X| \n-+-+-\nX|O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '2':
        print('O moves on the top-center space.')
        print('O|O| \n-+-+-\n |X| \n-+-+-\n |X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\n |X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\n |X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-right space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\n |X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print('O|O|X\n-+-+-\n |X| \n-+-+-\nO|X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the left space.')
                print('O|O|X\n-+-+-\nO|X| \n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X| \n')
                print('The computer wins!')
                sys.exit()
    if move == '3':
        print('O moves on the top-right space.')
        print('O| |O\n-+-+-\n |X| \n-+-+-\n | |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\nX| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X| \n-+-+-\n |X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\nX|X| \n-+-+-\n | |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-center space.')
            print('O|O|O\n-+-+-\n |X|X\n-+-+-\n | |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('O|X|O\n-+-+-\n |X| \n-+-+-\n |O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\n |X|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '4':
        print('O moves on the right space.')
        print('O| | \n-+-+-\nX|X|O\n-+-+-\n | | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nX|X|O\n-+-+-\nX| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the bottom-right space.')
                print('O| |O\n-+-+-\nX|X|O\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\nX| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
        if move == '2':
            print('O moves on the top-center space.')
            print('O|O| \n-+-+-\nX|X|O\n-+-+-\n |X| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\nX|X| \n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the top-right space.')
                print('O|O|O\n-+-+-\nX|X|O\n-+-+-\n |X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '3':
            print('O moves on the bottom-left space.')
            print('O| | \n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O| \n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X| \n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('O|X| \n-+-+-\nX|X|O\n-+-+-\n |O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '6':
        print('O moves on the left space.')
        print('O| | \n-+-+-\nO|X|X\n-+-+-\n | | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print('O| |O\n-+-+-\nO|X|X\n-+-+-\nX| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X| \n')
                print('The computer wins!')
                sys.exit()
            if move == '3':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\nO|X|X\n-+-+-\nX| |X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '2':
            print('O moves on the bottom-left space.')
            print('O| | \n-+-+-\nO|X|X\n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the bottom-left space.')
            print('O| | \n-+-+-\nO|X|X\n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-left space.')
            print('O|X| \n-+-+-\nO|X|X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
    if move == '8':
        print('O moves on the bottom-center space.')
        print('O|X| \n-+-+-\n |X| \n-+-+-\n |O| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print('O|X|O\n-+-+-\n |X| \n-+-+-\nX|O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X| \n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '3':
            print('O moves on the top-right space.')
            print('O|X|O\n-+-+-\n |X| \n-+-+-\n |O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\n |X|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '4':
            print('O moves on the right space.')
            print('O|X| \n-+-+-\nX|X|O\n-+-+-\n |O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nX|X|O\n-+-+-\n |O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('O|X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O|X| \n-+-+-\nO|X|X\n-+-+-\n |O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the bottom-left space.')
                print('O|X| \n-+-+-\nO|X|X\n-+-+-\nO|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print('O|X|X\n-+-+-\nO|X|X\n-+-+-\nO|O| \n')
                print('The computer wins!')
                sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print('O|X|X\n-+-+-\n |X| \n-+-+-\nO|O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO|X| \n-+-+-\nO|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-right space.')
                print('O|X|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-right space.')
                print('O|X|X\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '9':
        print('O moves on the bottom-left space.')
        print('O| |X\n-+-+-\n |X| \n-+-+-\nO| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X| \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the right space.')
            print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the bottom-center space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO|X| \n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
if move == '6':
    print('O moves on the bottom-right space.')
    print(' | | \n-+-+-\n | |X\n-+-+-\n | |O\n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the top-right space.')
        print(' | |O\n-+-+-\n | |X\n-+-+-\nX| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-left space.')
            print('O| |O\n-+-+-\n | |X\n-+-+-\nX|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|O\n-+-+-\n |X|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print(' | |O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-left space.')
                print('O| |O\n-+-+-\nX|O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the top-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print(' | |O\n-+-+-\nO|X|X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print(' |O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '7':
                print('O moves on the top-center space.')
                print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX| |O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print(' |X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '7':
            print('O moves on the left space.')
            print('X| |O\n-+-+-\nO| |X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nO|O|X\n-+-+-\nX|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|O|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX| |O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\nO|O|X\n-+-+-\nX| |O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|X|O\n-+-+-\nO|O|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '8':
            print('O moves on the top-left space.')
            print('O|X|O\n-+-+-\n | |X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\n |X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nX|O|O\n')
                    print('You have won!')
                    sys.exit()
    if move == '2':
        print('O moves on the bottom-left space.')
        print(' | | \n-+-+-\n | |X\n-+-+-\nO|X|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the center space.')
            print(' | | \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '7':
                print('O moves on the top-right space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the top-left space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the top-left space.')
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print(' | | \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '7':
                print('O moves on the top-center space.')
                print('X|O| \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print(' |X| \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('You have won!')
                sys.exit()
            if move == '9':
                print('O moves on the top-left space.')
                print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '7':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\n | |X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('X| |O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print(' |X| \n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-left space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('O moves on the top-right space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the top-left space.')
                print('O|X|X\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '9':
            print('O moves on the top-left space.')
            print('O| |X\n-+-+-\n | |X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO| |X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '4':
        print('O moves on the center space.')
        print(' | | \n-+-+-\nX|O|X\n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-left space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the top-left space.')
            print('O| | \n-+-+-\nX|O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '7':
            print('O moves on the bottom-left space.')
            print('X| | \n-+-+-\nX|O|X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-right space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('X|X| \n-+-+-\nX|O|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-center space.')
                print('X| |X\n-+-+-\nX|O|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the top-left space.')
            print('O|X| \n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the top-left space.')
            print('O| |X\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '5':
        print('O moves on the left space.')
        print(' | | \n-+-+-\nO|X|X\n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print(' | |O\n-+-+-\nO|X|X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print(' |O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '7':
                print('O moves on the bottom-center space.')
                print('X| |O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print(' |X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '2':
            print('O moves on the top-center space.')
            print(' |O| \n-+-+-\nO|X|X\n-+-+-\n |X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print(' |O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '7':
                print('O moves on the bottom-left space.')
                print('X|O| \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print(' |O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '7':
            print('O moves on the bottom-left space.')
            print('X| | \n-+-+-\nO|X|X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('X|O| \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('X|X| \n-+-+-\nO|X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-center space.')
                print('X| |X\n-+-+-\nO|X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print(' |X| \n-+-+-\nO|X|X\n-+-+-\n |O|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-right space.')
                print(' |X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '7':
                print('O moves on the bottom-left space.')
                print('X|X| \n-+-+-\nO|X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the bottom-left space.')
                print(' |X|X\n-+-+-\nO|X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print(' | |X\n-+-+-\nO|X|X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-left space.')
                print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('O moves on the bottom-center space.')
                print('X| |X\n-+-+-\nO|X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print(' |X|X\n-+-+-\nO|X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '7':
        print('O moves on the top-right space.')
        print('X| |O\n-+-+-\n | |X\n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the left space.')
            print('X| |O\n-+-+-\nO| |X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nO|O|X\n-+-+-\nX|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|O|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX| |O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\nO|O|X\n-+-+-\nX| |O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|X|O\n-+-+-\nO|O|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '2':
            print('O moves on the bottom-left space.')
            print('X| |O\n-+-+-\n | |X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('X| |O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-left space.')
            print('X| |O\n-+-+-\nX| |X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('X| |O\n-+-+-\nX|X|X\n-+-+-\nO| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('X| |O\n-+-+-\nO|X|X\n-+-+-\n | |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-center space.')
                print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX| |O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '2':
                print('O moves on the top-center space.')
                print('X|O|O\n-+-+-\nO|X|X\n-+-+-\n |X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('X|O|O\n-+-+-\nO|X|X\n-+-+-\nX|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\nO|X|X\n-+-+-\n |O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '1':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '8':
            print('O moves on the bottom-left space.')
            print('X|X|O\n-+-+-\n | |X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '8':
        print('O moves on the top-right space.')
        print(' |X|O\n-+-+-\n | |X\n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-left space.')
            print('O|X|O\n-+-+-\n | |X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\n |X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nX|O|O\n')
                    print('You have won!')
                    sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print(' |X|O\n-+-+-\n |O|X\n-+-+-\n |X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-left space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-left space.')
                print(' |X|O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('O moves on the bottom-left space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print(' |X|O\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the top-left space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '2':
                print('O moves on the bottom-left space.')
                print(' |X|O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('O moves on the bottom-left space.')
                print('X|X|O\n-+-+-\nX|O|X\n-+-+-\nO| |O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print(' |X|O\n-+-+-\n |X|X\n-+-+-\n |O|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the left space.')
                print(' |X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print(' |X|O\n-+-+-\nX|X|X\n-+-+-\n |O|O\n')
                print('You have won!')
                sys.exit()
            if move == '7':
                print('O moves on the bottom-left space.')
                print('X|X|O\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '7':
            print('O moves on the bottom-left space.')
            print('X|X|O\n-+-+-\n | |X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '9':
        print('O moves on the top-left space.')
        print('O| |X\n-+-+-\n | |X\n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n |X|X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O| |X\n-+-+-\nX|X|X\n-+-+-\nO| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
if move == '7':
    print('O moves on the bottom-left space.')
    print('X| | \n-+-+-\n | | \n-+-+-\nO| | \n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '2':
        print('O moves on the bottom-right space.')
        print('X| | \n-+-+-\n | | \n-+-+-\nO|X|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '4':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\nX| | \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the right space.')
                print('X| |O\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the top-center space.')
            print('X|O| \n-+-+-\n |X| \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the right space.')
                print('X|O| \n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('X|O| \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the right space.')
                print('X|O|X\n-+-+-\n |X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\n | |X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('X| |O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('X|X| \n-+-+-\n |O| \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-right space.')
                print('X|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the top-right space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('X|X|X\n-+-+-\n |O| \n-+-+-\nO|X|O\n')
                print('You have won!')
                sys.exit()
        if move == '9':
            print('O moves on the top-center space.')
            print('X|O|X\n-+-+-\n | | \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('X|O|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('X|O|X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the right space.')
                print('X|O|X\n-+-+-\n |X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('X|O|X\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
    if move == '3':
        print('O moves on the center space.')
        print('X| | \n-+-+-\n |O| \n-+-+-\nO| |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\n |O| \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\nX|O| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\n |O|X\n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the top-right space.')
            print('X|X|O\n-+-+-\n |O| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the right space.')
            print('X| |X\n-+-+-\n |O|O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('X| |X\n-+-+-\nO|O|O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the top-center space.')
                print('X|O|X\n-+-+-\nX|O|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('X|O|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('X|X|X\n-+-+-\n |O|O\n-+-+-\nO| |X\n')
                print('You have won!')
                sys.exit()
    if move == '4':
        print('O moves on the top-right space.')
        print('X| |O\n-+-+-\nX| | \n-+-+-\nO| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the center space.')
            print('X| |O\n-+-+-\nX|O| \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the center space.')
            print('X| |O\n-+-+-\nX|O| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-right space.')
            print('X| |O\n-+-+-\nX|X| \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the right space.')
                print('X| |O\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('X| |O\n-+-+-\nX|X|X\n-+-+-\nO| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('X|X|O\n-+-+-\nX|O| \n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
    if move == '5':
        print('O moves on the bottom-right space.')
        print('X| | \n-+-+-\n |X| \n-+-+-\nO| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-center space.')
            print('X|O| \n-+-+-\n |X| \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the right space.')
                print('X|O| \n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print('X|O| \n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '9':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '9':
                print('O moves on the left space.')
                print('X|O|X\n-+-+-\nO|X| \n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '4':
            print('O moves on the bottom-center space.')
            print('X| | \n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-center space.')
            print('X| | \n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('X|X| \n-+-+-\n |X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-center space.')
            print('X| |X\n-+-+-\n |X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '6':
        print('O moves on the bottom-right space.')
        print('X| | \n-+-+-\n | |X\n-+-+-\nO| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the top-right space.')
            print('X| |O\n-+-+-\n | |X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('X| |O\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('X| |O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-center space.')
            print('X| | \n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print('X| | \n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-center space.')
            print('X|X| \n-+-+-\n | |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-center space.')
            print('X| |X\n-+-+-\n | |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '8':
        print('O moves on the top-right space.')
        print('X|X|O\n-+-+-\n | | \n-+-+-\nO| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the center space.')
            print('X|X|O\n-+-+-\n |O| \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the center space.')
            print('X|X|O\n-+-+-\n |O| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('X|X|O\n-+-+-\nX|O| \n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print('X|X|O\n-+-+-\n |X| \n-+-+-\nO|O| \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '3':
                print('X|X|O\n-+-+-\n |X| \n-+-+-\nO|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-right space.')
                print('X|X|O\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-right space.')
                print('X|X|O\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
    if move == '9':
        print('O moves on the top-center space.')
        print('X|O|X\n-+-+-\n | | \n-+-+-\nO| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the bottom-right space.')
            print('X|O|X\n-+-+-\n | | \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('X|O|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('X|O|X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('X|O|X\n-+-+-\nO|X| \n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('X|O|X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('X|O|X\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '3':
            print('O moves on the center space.')
            print('X|O|X\n-+-+-\n |O| \n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the right space.')
                print('X|O|X\n-+-+-\n |O|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\nX|O| \n-+-+-\nO|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('X|O|X\n-+-+-\n |O|X\n-+-+-\nO| |X\n')
                print('You have won!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-right space.')
            print('X|O|X\n-+-+-\nX| | \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X|O|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '6':
                    print('X|O|X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the bottom-right space.')
            print('X|O|X\n-+-+-\n |X| \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the right space.')
                print('X|O|X\n-+-+-\n |X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '6':
            print('O moves on the bottom-right space.')
            print('X|O|X\n-+-+-\n | |X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X|O|X\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('X|O|X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('X|O|X\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
if move == '8':
    print('O moves on the bottom-right space.')
    print(' |X| \n-+-+-\n | | \n-+-+-\n | |O\n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the top-right space.')
        print(' |X|O\n-+-+-\n | | \n-+-+-\nX| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the right space.')
            print(' |X|O\n-+-+-\n | |O\n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the right space.')
            print(' |X|O\n-+-+-\nX| |O\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the right space.')
            print(' |X|O\n-+-+-\n |X|O\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-left space.')
            print('O|X|O\n-+-+-\n | |X\n-+-+-\nX| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\n |O|X\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|O\n-+-+-\nX|O|X\n-+-+-\nX| |O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|O\n-+-+-\n |X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|O\n-+-+-\nX|X|X\n-+-+-\nX|O|O\n')
                    print('You have won!')
                    sys.exit()
        if move == '7':
            print('O moves on the right space.')
            print('X|X|O\n-+-+-\n | |O\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '2':
        print('O moves on the center space.')
        print(' |X| \n-+-+-\n |O| \n-+-+-\n |X|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-left space.')
            print('O|X| \n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the top-left space.')
            print('O|X| \n-+-+-\nX|O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the top-left space.')
            print('O|X| \n-+-+-\n |O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '7':
            print('O moves on the top-right space.')
            print('X|X|O\n-+-+-\n |O| \n-+-+-\n |X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '1':
                print('O moves on the right space.')
                print('X|X|O\n-+-+-\n |O|O\n-+-+-\nX|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-left space.')
                print('X|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-left space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '9':
            print('O moves on the top-left space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '4':
        print('O moves on the bottom-left space.')
        print(' |X| \n-+-+-\nX| | \n-+-+-\nO| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the center space.')
            print(' |X| \n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '6':
                print('O moves on the top-left space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('O moves on the top-right space.')
                print('X|X|O\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the top-left space.')
                print('O|X|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print(' |X| \n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-center space.')
            print(' |X| \n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '7':
            print('O moves on the bottom-center space.')
            print('X|X| \n-+-+-\nX| | \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-center space.')
            print(' |X|X\n-+-+-\nX| | \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '5':
        print('O moves on the bottom-center space.')
        print(' |X| \n-+-+-\n |X| \n-+-+-\n |O|O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the top-right space.')
            print(' |X|O\n-+-+-\n |X| \n-+-+-\nX|O|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the right space.')
                print(' |X|O\n-+-+-\nX|X|O\n-+-+-\nX|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the left space.')
                print(' |X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '7':
                    print('X|X|O\n-+-+-\nO|X|X\n-+-+-\nX|O|O\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '7':
                print('O moves on the right space.')
                print('X|X|O\n-+-+-\n |X|O\n-+-+-\nX|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-left space.')
            print(' |X| \n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-left space.')
            print(' |X| \n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '7':
            print('O moves on the bottom-left space.')
            print('X|X| \n-+-+-\n |X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-left space.')
            print(' |X|X\n-+-+-\n |X| \n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '6':
        print('O moves on the bottom-left space.')
        print(' |X| \n-+-+-\n | |X\n-+-+-\nO| |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the center space.')
            print(' |X| \n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-left space.')
                print('O|X| \n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '7':
                print('O moves on the top-right space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '9':
                print('O moves on the top-left space.')
                print('O|X|X\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-center space.')
            print(' |X| \n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-center space.')
            print(' |X| \n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '7':
            print('O moves on the bottom-center space.')
            print('X|X| \n-+-+-\n | |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '9':
            print('O moves on the bottom-center space.')
            print(' |X|X\n-+-+-\n | |X\n-+-+-\nO|O|O\n')
            print('The computer wins!')
            sys.exit()
    if move == '7':
        print('O moves on the top-right space.')
        print('X|X|O\n-+-+-\n | | \n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the right space.')
            print('X|X|O\n-+-+-\n | |O\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the right space.')
            print('X|X|O\n-+-+-\n | |O\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the right space.')
            print('X|X|O\n-+-+-\nX| |O\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the right space.')
            print('X|X|O\n-+-+-\n |X|O\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-left space.')
            print('X|X|O\n-+-+-\n | |X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('X|X|O\n-+-+-\n |O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('X|X|O\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
    if move == '9':
        print('O moves on the top-left space.')
        print('O|X|X\n-+-+-\n | | \n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\nX|O| \n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O|X|X\n-+-+-\n |X| \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O|X|X\n-+-+-\n |X| \n-+-+-\nO|X|O\n')
                print('You have won!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
if move == '9':
    print('O moves on the top-left space.')
    print('O| |X\n-+-+-\n | | \n-+-+-\n | | \n')
    print('Enter the number of your move:')
    print('  789\n  456\n  123')
    move = input()

    if move == '1':
        print('O moves on the center space.')
        print('O| |X\n-+-+-\n |O| \n-+-+-\nX| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the bottom-center space.')
            print('O| |X\n-+-+-\n |O| \n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|O| \n-+-+-\nX|O|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O| |X\n-+-+-\n |O|X\n-+-+-\nX|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the right space.')
                print('O|X|X\n-+-+-\n |O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '4':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the bottom-right space.')
            print('O|X|X\n-+-+-\n |O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '2':
        print('O moves on the bottom-left space.')
        print('O| |X\n-+-+-\n | | \n-+-+-\nO|X| \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '3':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO| | \n-+-+-\nO|X|X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the bottom-right space.')
            print('O| |X\n-+-+-\nX| | \n-+-+-\nO|X|O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '5':
                print('O moves on the right space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X| \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO| |X\n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO| | \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
    if move == '3':
        print('O moves on the right space.')
        print('O| |X\n-+-+-\n | |O\n-+-+-\n | |X\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the bottom-center space.')
            print('O| |X\n-+-+-\n | |O\n-+-+-\nX|O|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O| |X\n-+-+-\n |X|O\n-+-+-\nX|O|X\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\n |O|O\n-+-+-\nX|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '4':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nX|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '2':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n | |O\n-+-+-\nO|X|X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '4':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '8':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO| |O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
        if move == '4':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nX| |O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O| |X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n |X|O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the bottom-center space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO|X|O\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the bottom-left space.')
            print('O|X|X\n-+-+-\n | |O\n-+-+-\nO| |X\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO| |O\n-+-+-\nO|X|X\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|X|X\n-+-+-\nX|O|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '5':
                print('O moves on the left space.')
                print('O|X|X\n-+-+-\nO|X|O\n-+-+-\nO| |X\n')
                print('The computer wins!')
                sys.exit()
    if move == '4':
        print('O moves on the bottom-right space.')
        print('O| |X\n-+-+-\nX| | \n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O| \n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\nX|X| \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the right space.')
                print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '8':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|X|O\n')
                    print('You have won!')
                    sys.exit()
            if move == '6':
                print('O| |X\n-+-+-\nX|X|X\n-+-+-\nO| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '6':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\nX|O| \n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '5':
        print('O moves on the bottom-left space.')
        print('O| |X\n-+-+-\n |X| \n-+-+-\nO| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X| \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X| \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the right space.')
            print('O| |X\n-+-+-\nX|X|O\n-+-+-\nO| | \n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '3':
                print('O moves on the top-center space.')
                print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO| |X\n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '2':
                    print('O|O|X\n-+-+-\nX|X|O\n-+-+-\nO|X|X\n')
                    print('It\'s a tie!')
                    sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O| \n')
                print('Enter the number of your move:')
                print('  789\n  456\n  123')
                move = input()

                if move == '3':
                    print('O|X|X\n-+-+-\nX|X|O\n-+-+-\nO|O|X\n')
                    print('It\'s a tie!')
                    sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '8':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO|X| \n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
    if move == '6':
        print('O moves on the bottom-right space.')
        print('O| |X\n-+-+-\n | |X\n-+-+-\n | |O\n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '1':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\nX| |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '2':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\n |O|X\n-+-+-\n |X|O\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the center space.')
            print('O| |X\n-+-+-\nX|O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
        if move == '5':
            print('O moves on the bottom-left space.')
            print('O| |X\n-+-+-\n |X|X\n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the left space.')
                print('O| |X\n-+-+-\nO|X|X\n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '4':
                print('O| |X\n-+-+-\nX|X|X\n-+-+-\nO| |O\n')
                print('You have won!')
                sys.exit()
            if move == '8':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\n |X|X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '8':
            print('O moves on the center space.')
            print('O|X|X\n-+-+-\n |O|X\n-+-+-\n | |O\n')
            print('The computer wins!')
            sys.exit()
    if move == '8':
        print('O moves on the bottom-left space.')
        print('O|X|X\n-+-+-\n | | \n-+-+-\nO| | \n')
        print('Enter the number of your move:')
        print('  789\n  456\n  123')
        move = input()

        if move == '2':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO| | \n-+-+-\nO|X| \n')
            print('The computer wins!')
            sys.exit()
        if move == '3':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO| | \n-+-+-\nO| |X\n')
            print('The computer wins!')
            sys.exit()
        if move == '4':
            print('O moves on the bottom-right space.')
            print('O|X|X\n-+-+-\nX| | \n-+-+-\nO| |O\n')
            print('Enter the number of your move:')
            print('  789\n  456\n  123')
            move = input()

            if move == '2':
                print('O moves on the center space.')
                print('O|X|X\n-+-+-\nX|O| \n-+-+-\nO|X|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '5':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX|X| \n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
            if move == '6':
                print('O moves on the bottom-center space.')
                print('O|X|X\n-+-+-\nX| |X\n-+-+-\nO|O|O\n')
                print('The computer wins!')
                sys.exit()
        if move == '5':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO|X| \n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
        if move == '6':
            print('O moves on the left space.')
            print('O|X|X\n-+-+-\nO| |X\n-+-+-\nO| | \n')
            print('The computer wins!')
            sys.exit()
