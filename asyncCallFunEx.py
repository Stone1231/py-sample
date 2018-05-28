import asyncio
import time
import json


@asyncio.coroutine
def yield_ex():
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, waitsec, 1)
    future2 = loop.run_in_executor(None, waitsec, 2)
    response1 = yield from future1
    response2 = yield from future2
    print(response1)
    print(response2)

@asyncio.coroutine
def yield_ex2(s1, s2):
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, waitsec, s1)
    future2 = loop.run_in_executor(None, waitsec, s2)
    response1 = yield from future1
    response2 = yield from future2
    d = dict(res1 = response1,res2=response2)
    return d   

async def await_ex():#after python 3.5
    loop = asyncio.get_event_loop()
    future1 = loop.run_in_executor(None, waitsec, 1)
    future2 = loop.run_in_executor(None, waitsec, 2)
    response1 = await future1
    response2 = await future2
    print(response1)
    print(response2)

def waitsec(s):
    time.sleep(s)
    return "%f sec" % s


#yield_ex 單筆
def test_yield_ex():
    tStart = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(yield_ex())
    tEnd = time.time()
    print("yield ex: %f sec" % (tEnd - tStart))
test_yield_ex()

#yield_ex 多筆
def test_yield_ex2():    
    tStart = time.time()
    loop = asyncio.get_event_loop()
    tasks = [yield_ex2(1,2), yield_ex2(1,2)]
    res =loop.run_until_complete(asyncio.wait(tasks))

    results = []
    while res[0]:
        results.append(res[0].pop()._result) 
        
    tEnd = time.time()
    print("yield_ex2: %f sec, data:{:s}" % (tEnd - tStart) , json.dumps(results))
test_yield_ex2()

#await_ex
def test_await_ex():   
    tStart = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(await_ex())
    tEnd = time.time()
    print("async: %f sec" % (tEnd - tStart))
test_await_ex()

#模擬排程
def create_thread():   
    #1
    #loop = asyncio.new_event_loop()
    
    #2
    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    #1 or 2都可

    while(True):
        tStart = time.time()
        tasks = [yield_ex2(1,2), yield_ex2(3,4)]
        res =loop.run_until_complete(asyncio.wait(tasks))
        results = []
        while res[0]:
            results.append(res[0].pop()._result) 
            
        tEnd = time.time()
        print("job: {} sec, data:{}".format((tEnd - tStart) , json.dumps(results)))

        time.sleep(1)
try:
    import thread
except ImportError:
    import _thread as thread
thread.start_new_thread(create_thread, ())
time.sleep(10) #要睡一下才不會馬上結束