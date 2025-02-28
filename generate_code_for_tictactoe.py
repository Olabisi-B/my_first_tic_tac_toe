# Someone told me that I would save a lot of time by writing
# a program to generate tictactoe.py, so I wrote this program:

fo = open('tictactoe.py', 'w')
fo.write(r"""# My first tic-tac-toe program, by Al Sweigart al@inventwithpython.com
# This sure was a lot of typing, but I finally finished it!

# (This is a joke program. Or maybe I just cant code!)

import sys
if sys.version_info[0] == 2:
    input = raw_input # python 2 compatibility
print('Welcome to Tic Tac Toe but evil and bad!')
print('You are X.\n')

print(' | | \n-+-+-\n | | \n-+-+-\n | | \n')
print('Enter the number of your move:')
print('  789\n  456\n  123')
move = input()
print('I actually give up I cannot code. here are lyrics instead: Gyatt!
I was in Ohio before I met you
I rizzed too much and that's an issue
But I'm Grimace Shake
Gyatt!
Tell your friends it was nice to rizz them
But I hope I never edge again
I know it breaks your Fanum
Taxin' in Ohio and I'm still not Sigma
Four years, no Livvy
Now you're lookin' pretty on Adin Ross' Twitchy
And I-I-I-I-I can't rizz
No, I-I-I-I-I can't mew
So baby, gronk me closer
In the back Skibidi Toilet
That I know you can't afford
Kai Cenat tatted on my shoulder
Pull the gyatt right of the corner
From that Fanum that you taxed
From your roommate back in Ohio
We ain't ever not the Rizzler
We ain't ever not the Rizzler
We ain't ever not the Rizzler
Yeah, that's sick')
""")
fo.close()
