import time 
import os 
def clear():
    command = 'cls'
    os.system(command)
clear()
for am in range(1, 13, 1):
    print(str(am) + 'AM')
    time.sleep(1)
    clear()
    
for pm in range(1,13, 1):
    print(str(pm) + 'PM')
    time.sleep(1)
    clear()
    