import asyncio
import threading
import janus


def threaded(squeue):
    import time
    while True:
        time.sleep(2)
        squeue.put_nowait(time.time())
        print(squeue.qsize())


@asyncio.coroutine
def async_func(aqueue):
    while True:
        time = yield from aqueue.get()
        print(time)

def useQueue():
    loop = asyncio.get_event_loop()
    queue = janus.Queue(loop)
    asyncio.create_task(async_func(queue.async_q))
    threading.Thread(threaded, queue.sync_q).start()
    loop.run_forever()


async def async_func(q):
    # Your asynchronous logic here

def useQueue():
    loop = asyncio.get_event_loop()
    queue = janus.Queue(loop)
    asyncio.create_task(async_func(queue.async_q))
    loop.run_forever()
