# your code goes here!
import time
time.sleep(1)

def countdown(x):
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
    print('HAPPY NEW YEAR!')

countdown(11)



def countdown_with_sleep(x):
    import time
    time.sleep(1)
    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')

countdown_with_sleep(11)


