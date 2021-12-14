import time
import os
import sys
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
def clear():
    command = 'cls'
    os.system(command)


confirmation = input(slowprint('Do you want to launch \'Het raketje\'? yes/no: '))
clear()
if confirmation == 'yes':
    for i in range(30, -1, -1):
        clear()
        print(i)
        time.sleep(0.5)
    slowprint('\'Het raketje\' is on it\'s million mile journey to Saturn! ')
elif confirmation == 'no':
    slowprint('The rocket exploded and 721 people died...')
input('')