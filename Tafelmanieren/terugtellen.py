import time
import os
def clear():
    command = 'cls'
    os.system(command)


confirmation = input('Do you want to launch \'Het raketje\'? yes/no: ')
clear()
if confirmation == 'yes':
    for i in range(30, -1, -1):
        clear()
        print(i)
        time.sleep(1)
    print('\'Het raketje\' is on it\'s million mile journey to Saturn! ')
elif confirmation == 'no':
    print('The rocket exploded and 721 people died...')