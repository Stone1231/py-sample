import time
import json

try:
	import thread
except ImportError:
	import _thread as thread

def run():   
    i = 0 
    while(True):
        time.sleep(2)
        i = i + 1
        print(json.dumps("Hello %d" % i))
thread.start_new_thread(run, ())
time.sleep(10)