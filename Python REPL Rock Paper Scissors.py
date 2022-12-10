import random
import time

def rps():
    rpsL = ['r', 'p', 'p', 's', 'p', 's', 's', 'r', 'p', 's']
    pS = 0
    cS = 0
    print('\n')
    print("On shoot, you must enter r, p, or s, do you understand?")
    ###
    inp = input('Yes or No? (y/n): ').lower()
    print('\n')
    if inp != 'y':
        print('Goodbye')
        return 1
    else:
        while pS < 3 and cS < 3:
            print('On shoot...\n')
            time.sleep(1)
            print('rock')
            print('.\n.')
            time.sleep(1)
            print('paper')
            print('.\n.')
            time.sleep(1)
            print('scissors')
            print('.\n.')
            time.sleep(1)
            print('shoot!\n')
            comp = random.choice(rpsL)
            #print(f'For testing purposes: computer chose {comp}')
            ###
            player = input('(r/p/s): ').lower()
            '----------------------------------------------------------'
            if player == 'r' and comp == 'r':  
                print('draw')
                print(f'you: {pS}, computer: {cS}')
            if player == 'p' and comp == 'p':
                print('draw')
                print(f'you: {pS}, computer: {cS}')
            if player == 's' and comp == 's':
                print('draw')
                print(f'you: {pS}, computer: {cS}')
            '----------------------------------------------------------'
            if player == 'r' and comp == 's':  
                pS = pS + 1
                if pS != 3 and cS != 3:
                    print(f'you won this round. you: {pS}, computer: {cS}')
            if player == 's' and comp == 'p':
                pS = pS + 1
                if pS != 3 and cS != 3:
                    print(f'you won this round. you: {pS}, computer: {cS}')
            if player == 'p' and comp == 'r':
                pS = pS + 1
                if pS != 3 and cS != 3:
                    print(f'you won this round. you: {pS}, computer: {cS}')
            '----------------------------------------------------------' 
            if player == 'r' and comp == 'p': 
                cS = cS + 1
                if pS != 3 and cS != 3:
                    print(f'you lost this round. you: {pS}, computer: {cS}')
            if player == 's' and comp == 'r':
                cS = cS + 1
                if pS != 3 and cS != 3:
                    print(f'you lost this round. you: {pS}, computer: {cS}')
            if player == 'p' and comp == 's':
                cS = cS + 1
                if pS != 3 and cS != 3:
                    print(f'you lost this round. you: {pS}, computer: {cS}')
            '----------------------------------------------------------'     
            print('\n')
            if pS == 3 or cS == 3:
                print('And we have a winner!')
                print('\n')
            elif pS == 2 or cS == 2:
                print('Sudden Death!')
                print('\n')
            '----------------------------------------------------------'    
        if pS > cS:
            winr = pS
            print(f'You won')
            print('\n')
        else:
            winr = cS
            print(f'Computer won')
            print('\n')

start = rps()
start
