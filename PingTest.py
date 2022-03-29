import threading
import requests
import time
import os
import keyboard

speed = int(input("| Time between ping : "))
_Threads = int(input("| How manny instances do you want to run? : "))
threads = []
url = '8.8.8.8'
data = {

}
def Task():
    while True:
        time.sleep(speed)
        print(os.system('ping ' + url))
        if keyboard.is_pressed('ESCAPE'):
            print("exited")
            break

for i in range(_Threads):
    t = threading.Thread(target=Task)
    t.daemon = True
    threads.append(t)

for i in range(_Threads):
    threads[i].start()

for i in range(_Threads):
    threads[i].join()

