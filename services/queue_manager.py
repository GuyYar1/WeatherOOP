import asyncio

class Queue_manager:



    def threaded(self, sync_q):
        # Your existing threaded producer logic (if any)
        pass

    async def async_coro(self, async_q):
        # Your existing asynchronous consumer logic (if any)
        pass

    def create_queues(self):
        # Create an asyncio queue
        async_q = asyncio.Queue()
        # Start the threaded producer (if needed)
        # threading.Thread(target=threaded, args=(async_q,)).start()
        # Return both queues
        return async_q

    async def producer(self, queue, enqueue):
        # Your producer logic (e.g., generate data and put it into the queue)
        await queue.put(enqueue)
        print(f'Produced {enqueue}')
        #await asyncio.sleep(random.uniform(0.05, 0.1))  # Simulate some work

    async def consumer(self, queue):
        # Your consumer logic (e.g., process data from the queue)
        # # while True:
        dequeue = await queue.get()
        print(f'Consumed {dequeue}')
        queue.task_done()
        return dequeue

        #
# How Does asyncio.Queue Work?
# A Queue follows the First-In-First-Out (FIFO) order, meaning that the first item added to the queue is the first one to be retrieved.
# Key methods of asyncio.Queue:
# put(item): Adds an item to the queue. If the queue is full, it waits until a slot becomes available.
# get(): Removes and returns an item from the queue. If the queue is empty, it waits until an item is available.
# get_nowait(): Returns an item immediately if available, otherwise raises an exception (similar to a non-blocking get).
# join(): Blocks until all items in the queue have been processed (useful for synchronization).
# task_done(): Indicates that a task (item) has been fully processed (used by consumers).
# qsize(): Returns the number of items in the queue.
# The queue size can be infinite (if maxsize is less than or equal to zero) or limited (if maxsize is a positive integer).
# Unlike the standard library’s queue, the size of an asyncio.Queue is always known and can be queried using qsize().
# Concurrency and Threads:
# asyncio.Queue is designed for asynchronous code, not for multithreading.
# It operates within a single thread (typically the event loop thread).
# Producers and consumers (coroutines) can work concurrently within the same thread.
# If you need multithreading, consider using the standard queue module instead.