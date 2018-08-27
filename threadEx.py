import time
import json

try:
	import thread
except ImportError:
	import _thread as thread

import threading
class Man(): 
    def __init__(self, name):
        self.name = name

    def say(self, word):
        while(True):
            time.sleep(2)
            print(self.name + " say: " + word)

def run():   
    i = 0 
    while(True):
        time.sleep(2)
        i = i + 1
        print(json.dumps("Hello %d" % i))

man = Man('Stone')
threading.Thread(target=man.say,kwargs=dict(word="hello~")).start()

thread.start_new_thread(run, ())
#time.sleep(10)

        