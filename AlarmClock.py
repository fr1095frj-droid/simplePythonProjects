import time
import datetime
import pygame

def alarm():
    alarm_time = input('Enter your alarm time(HH:MM:SS): ').strip()
    now = datetime.datetime.now().strftime("%H:%M:%S")

    while alarm_time != now:
        print(now)
        time.sleep(1)
        now = datetime.datetime.now().strftime("%H:%M:%S")

    print('WAKE UP!')
    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play()


while True:
    alarm()

    pygame.mixer.init()
    pygame.mixer.music.load('alarm.mp3')
    pygame.mixer.music.play()
    answer = input('Would you like to set the again? (y/n): ').lower()
    if answer == 'y':
        pygame.mixer.music.stop()
        continue
    else:
        break


print('HAVE A NICE DAY ')
