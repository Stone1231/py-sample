import asyncio
import time


# async_ex

async def cor1():
    print("cor1 start")
    for i in range(10):
        await asyncio.sleep(1.5)
        print("cor1", i)


async def cor2():
    print("cor2 start")
    for i in range(15):
        await asyncio.sleep(1)
        print("cor2", i)


def async_ex():
    loop = asyncio.get_event_loop()
    cors = asyncio.wait([cor1(), cor2()])
    loop.run_until_complete(cors)

# executors_ex
from concurrent.futures import ThreadPoolExecutor


def func(a, b):
    # Do time intensive stuff...
    return a + b


async def main(loop):
    executor = ThreadPoolExecutor()
    result = await loop.run_in_executor(executor, func, "Hello,", " world!")
    #result = await loop.run_in_executor(None, func, "Hello,", " world!")
    print(result)

def executors_ex():
    loop = asyncio.get_event_loop()
    #loop.set_default_executor(ThreadPoolExecutor())
    loop.run_until_complete(main(loop))

# event trigger ex
import functools

def trigger(event):
    print('EVENT SET')
    event.set() # wake up coroutines waiting
# event consumers
async def consumer_a(event):
    consumer_name = 'Consumer A'
    print('{} waiting'.format(consumer_name))
    await event.wait()
    print('{} triggered'.format(consumer_name))
async def consumer_b(event):
    consumer_name = 'Consumer B'
    print('{} waiting'.format(consumer_name))
    await event.wait()
    print('{} triggered'.format(consumer_name))

def event_ex():    
    # event
    event = asyncio.Event()

    main_future = asyncio.wait([consumer_a(event),consumer_b(event)])
    # event loop
    event_loop = asyncio.get_event_loop()
    event_loop.call_later(0.1, functools.partial(trigger, event)) # trigger event in 0.1 sec
    # complete main_future
    done, pending = event_loop.run_until_complete(main_future)

#websocket ex
# ref https://stackoverflow.com/questions/37369849/how-can-i-implement-asyncio-websockets-in-a-class
import aiohttp
from websockets import connect

class EchoWebsocket:
    #websockets.connect designed to be async context manager 
    #(it uses __aenter__, __aexit__)
    async def __aenter__(self):
        self._conn = connect("wss://echo.websocket.org")
        self.websocket = await self._conn.__aenter__()        
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()


async def main():
    async with EchoWebsocket() as echo:
        await echo.send("Hello!")
        print(await echo.receive())  # "Hello!"

def ws_ex():
    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


tStart = time.time()

#async_ex()
#executors_ex()
#ws_ex()

tEnd = time.time()
print("%f sec" % (tEnd - tStart))