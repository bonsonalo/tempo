import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data. ")
    # note that the process of concurrency starts the momnets it reads to be awaited. but here, since we used Taskgroup, it will handle it by itself

    """ 
    Mental model to keep:

    await = “pause here until this coroutine finishes.”

    create_task = “start this coroutine running now in the background.”

    TaskGroup = “start them all, wait until they’re all done (and handle errors properly).”
    """
    
    await asyncio.sleep(sleep_time) # simulate a network request or I/O operation 
    return {"id": id, "data": f"Sample data ffrom coroutine {id}"}


async def main():
    tasks= []
    async with asyncio.TaskGroup() as tg:     # we can use gather() but it doesnt have a error handling feature. but TaskGroup() has it
        for i, sleep_time in enumerate([2,1,3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # after the Task group block, all tasks have completed
    results= [task.result() for task in tasks]

    for result in results:
        print(f"Recieved result: {result}")


asyncio.run(main())




""" Using synchronization in async 

what si happening here is, if the process involves action like using shared resource, while 1 pauses and other use it, it might create error and not get the needed result. so We are using lock to say that the first task should finish going to the next one. At the pause time, if there is another code outside this lock function where it doesnt share the resource, it can run, if not it will wait the sleep time until it finishes the first task he has


so the optput will be for the 1st (all), then the 2nd(all) and so on
"""



lock = asyncio.Lock()
shared_resource= 0

async def modify_shared_resource():
    global shared_resource
    async with lock:
        #critical section starts

        print(f"Resource before modification: {shared_resource}")
        shared_resource+=1 # modify the shared resource

        await asyncio.sleep(1) # simulate IO operation
        print(f"Resource after modification: {shared_resource}")
        # cirtical section ends

async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


asyncio.run(main())




""" 
   Semaphore
Semaphore is like using .lock() but allows multiple coroutines to have access to the same object at the same time to not overload it
"""

async def access_resource(semaphore, resource_id):
    async with semaphore:
        # Simulate accessing a limited resource 
        print(f"Accessing resource {resource_id}")
        await asyncio.sleep(1) # simulate work witht the resource

        print(f"releasing resource {resource_id}")

async def main():
    semaphore= asyncio.Semaphore(2) # allow 2 concurrent access
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5))) # the * is generator that gives you a special kind of Python object that produces values lazily — one at a time, only when you ask for them.
    #it becomes modify_shared_resource(), modify_shared_resource(), modify_shared_resource(), modify_shared_resource(), modify_shared_resource()



asyncio.run(main())




""" Using event """


async def waiter(event):
    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution")
async def setter(event):
    await asyncio.sleep(2)
    event.set()
    print("event has been set!")
async def main():
    event = asyncio. Event ()
    await asyncio.gather(waiter(event), setter(event) )
asyncio. run (main ())