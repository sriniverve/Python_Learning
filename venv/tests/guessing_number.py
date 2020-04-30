'''
This is an example program for gussing a number using while loop
'''

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess_number = int(input('Guess a number: '))
    guess_count += 1
    if guess_number == secret_number:
        print('You guessed it right. You Win!!!')
        break
else:
    print('You are have exhausted your options. Sorry!!!')
