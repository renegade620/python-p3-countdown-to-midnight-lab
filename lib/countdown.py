# your code goes here!
import time # import time library to use sleep

def countdown(num):
    while(num >= 1):
        print(f'{num} SECOND(S)!')
        num -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(num):
    while(num >= 1):
        print(f'{num} SECOND(S)!')
        time.sleep(1) # delays each step of the loop by 1 second
        num -= 1
    print("HAPPY NEW YEAR!")

countdown_with_sleep(10)