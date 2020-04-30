'''
This is a program to play car game using indefinite while loop
'''
is_started = False
is_stopped = False

while True:
    user_input = input('>').lower()
    if user_input == 'start':
        if is_started == True:
            print('Nothing to do. Car already started')
        else:
            print('Car has started')
            is_started = True
            is_stopped = False
    elif user_input == 'stop':
        if is_stopped == True:
            print('Nothing to do. Car already stopped')
        else:
            print('Car has stopped')
            is_stopped = True
            is_started = False
    elif user_input == 'help':
        print('''
start - to start the car
stop  - to stop the car
quit  - to quit the game
        ''')
    elif user_input == 'quit':
        break
    else:
        print('Sorry, I do not understand your input. Please use start or stop to continue')