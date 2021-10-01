import time 
import os
def clear():
    command = 'cls'
    os.system(command)
clear()
for i in range(20, 50, 2):
    print(i)
    time.sleep(1)
    clear()