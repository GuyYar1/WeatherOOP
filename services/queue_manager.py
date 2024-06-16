import asyncio
from asyncio import Queue


class Queue_manager:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """
        The __new__ method in Python is responsible for creating a new instance of a class.
        It is called before the __init__ method and is used to control the creation of a new instance.
        This is different from __init__, which initializes the instance after it is created.
        :param args:
        :param kwargs:
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.queue = Queue()
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.__class__._initialized = True

    async def add_to_queue(self, item):
        await self.queue.put(item)

    async def get_next_item(self):
        await asyncio.sleep(3)  # Delay for 3 seconds
        if not self.queue.empty():
            return await self.queue.get()
        else:
            return "No other Item, all is dequeued"
            # raise ValueError("The queue is empty")

    # read about Yield later


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