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

loop = asyncio.get_event_loop()
queue = janus.Queue(loop=loop)
asyncio.create_task(async_func(queue.async_q))
threading.Thread(target=threaded, args=(queue.sync_q,)).start()
loop.run_forever()