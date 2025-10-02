import time

print('You fine yourself in forest near an abandon house')
time.sleep(2)
house = input('Will you go in? (y / n): ')
if house == 'y':
    print('the house is dark')
    time.sleep(1)
    print('You see an old man in corner of the house')
    time.sleep(1)
    talk = input('Will you talk to him? (y / n): ')
    if talk == 'y':
        print('He tells you don not go throgh the red door...')

    else:
        print('you keep touring the house')
    time.sleep(2)

    print('you go down stairs and see two doors black and red')
    time.sleep(2)
    door = input('which door you choose? (red / black): ')
    if door == 'red':
        print('door closes behind you and you cant open it')
        time.sleep(1)
        print('you hear scarry noises coming closer')
        time.sleep(1)
        print('and colser...')
        time.sleep(1)
        print('and colser..')
        time.sleep(1)
        print('and colser.')
        time.sleep(1)
        print('and now youre dead')
        print('GAME OVER')
    elif door == 'black':
        print('you go to black room and at the end of the room ...')
        time.sleep(2)
        print('you find all of your answers')

else:
    print('an wolf find you youre dead')