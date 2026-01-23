import threading

print("Current Executing Thread:", threading.current_thread().getName())

from threading import *


def display():
    for i in range(6):
        print("Child Thread")


t = Thread(target=display)
t.start()
for i in range(6):
    print("Main Thread")

from threading import *


class Demo:
    def display(self):
        for i in range(6):
            print("Child Thread")


obj = Demo()
t = Thread(target=obj.display)
t.start()
for i in range(6):
    print("Main Thread")

from threading import *


class MyThread(Thread):
    def run(self):
        for i in range(6):
            print("Child Thread")


t = MyThread()
t.start()
for i in range(6):
    print("Main Thread")

from threading import *
import time


def divison(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:", n / 5)


def multiplication(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:", n * 5)


numbers = [10, 20, 30, 40, 50]
begintime = time.time()
divison(numbers)
multiplication(numbers)
print("The total time taken:", time.time() - begintime)

from threading import *
import time


def divison(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:", n / 5)


def multiplication(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:", n * 5)


numbers = [10, 20, 30, 40, 50]
begintime = time.time()
t1 = Thread(target=divison, args=(numbers,))
t2 = Thread(target=multiplication, args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()

print("The total time taken:", time.time() - begintime)

from threading import *

print("Main thread name", current_thread().getName())
current_thread().setName("MyThread")

print("After customise the thread name: ", current_thread().getName())

from threading import *


def m():
    print("Child Thread")


t = Thread(target=m)
t.start()
print("Main Thread Identification Number:", current_thread().ident)
print("Child Thread Identification Number:", t.ident)

# Metodos
# active_count() method:

from threading import *
import time


def display():
    print(current_thread().getName(), "...started")
    time.sleep(3)
    print(current_thread().getName(), "...ended")


print("The Number of active Threads:", active_count())
t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t3 = Thread(target=display, name="ChildThread3")
t1.start()
t2.start()
t3.start()
print("The Number of active Threads:", active_count())
time.sleep(5)
print("The Number of active Threads:", active_count())

# enumerate() function:

from threading import *
import time


def display():
    print(current_thread().getName(), "...started")
    time.sleep(3)
    print(current_thread().getName(), "...ended")


t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t3 = Thread(target=display, name="ChildThread3")
t1.start()
t2.start()
t3.start()
l = enumerate()
for t in l:
    print("Thread Name:", t.name)
time.sleep(5)
l = enumerate()
for t in l:
    print("Thread Name:", t.name)

# isAlive() method:

from threading import *
import time


def display():
    print(current_thread().getName(), "...started")
    time.sleep(3)
    print(current_thread().getName(), "...ended")


print("The Number of active Threads:", active_count())
t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t1.start()
t2.start()
print(t1.name, "is Alive :", t1.isAlive())
print(t2.name, "is Alive :", t2.isAlive())
time.sleep(5)
print(t1.name, "is Alive :", t1.isAlive())
print(t2.name, "is Alive :", t2.isAlive())

# join() method:

from threading import *
import time


def display():
    for i in range(5):
        print("First Thread")


t = Thread(target=display, name="ChildThread")
t.start()
t.join()  # This is executed by Main Thread
for i in range(5):
    print("Second Thread")


# join(seconds) method:

from threading import *
import time


def display():
    for i in range(5):
        print("First Thread")
        time.sleep(2)


t = Thread(target=display, name="ChildThread")
t.start()
t.join(5)  # This is executed by Main Thread
for i in range(5):
    print("Second Thread")

# Daemon Threads in Python with Examples
from threading import *

print(current_thread().isDaemon())
print(current_thread().daemon)

from threading import *


def display():
    print("Child Thread")


t = Thread(target=display)
t.start()
t.setDaemon(True)

from threading import *
import time


def display():
    for i in range(5):
        print("Child Thread")
        time.sleep(2)


t = Thread(target=display)
# t.setDaemon(True)
t.start()
time.sleep(5)
print("End Of Main Thread")

from threading import *
import time


def display():
    for i in range(5):
        print("Child Thread")
        time.sleep(2)


t = Thread(target=display)
t.setDaemon(True)
t.start()
time.sleep(5)
print("End Of Main Thread")

# Synchronization in Python with Examples
from threading import *
import time


def wish(name, age):
    for i in range(3):
        print("Hi", name)
        time.sleep(2)
        print("Your age is", age)


t1 = Thread(target=wish, args=("Sireesh", 15))
t2 = Thread(target=wish, args=("Nitya", 20))
t1.start()
t2.start()


from threading import *

l = Lock()
l.acquire()
print("lock acquired")
l.release()
print("lock released")


from threading import *

l = Lock()
l.release()
print("lock released")


from threading import *
import time

l = Lock()


def wish(name, age):
    for i in range(3):
        l.acquire()
        print("Hi", name)
        time.sleep(2)
        print("Your age is", age)
        l.release()


t1 = Thread(target=wish, args=("Sireesh", 15))
t2 = Thread(target=wish, args=("Nitya", 20))
t1.start()
t2.start()


from threading import *
import time

l = RLock()


def factorial(n):
    l.acquire()
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    l.release()
    return result


def results(n):
    print("The Factorial of", n, "is:", factorial(n))


t1 = Thread(target=results, args=(5,))
t2 = Thread(target=results, args=(9,))
t1.start()
t2.start()


from threading import *
import time

s = Semaphore(2)


def wish(name, age):
    for i in range(3):
        s.acquire()
        print("Hi", name)
        time.sleep(2)
        s.release()


t1 = Thread(target=wish, args=("Sireesh", 15))
t2 = Thread(target=wish, args=("Nitya", 20))
t3 = Thread(target=wish, args=("Shiva", 16))
t4 = Thread(target=wish, args=("Ajay", 25))
t1.start()
t2.start()
t3.start()
t4.start()


from threading import *

s = Semaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print("End")


from threading import *

s = BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print("End")

# Inter Thread communication in Python
from threading import *
import time


def traffic_police():
    while True:
        time.sleep(5)
        print("Traffic Police Giving GREEN Signal")
        event.set()
        time.sleep(10)
        print("Traffic Police Giving RED Signal")
        event.clear()


def driver():
    num = 0
    while True:
        print("Drivers waiting for GREEN Signal")
        event.wait()
        print("Traffic Signal is GREEN...Vehicles can move")
        while event.isSet():
            num = num + 1
            print("Vehicle No:", num, " Crossing the Signal")
            time.sleep(2)
        print("Traffic Signal is RED...Drivers have to wait")


event = Event()
t1 = Thread(target=traffic_police)
t2 = Thread(target=driver)
t1.start()
t2.start()


from threading import *
import time
import random

items = []


def produce(c):
    while True:
        c.acquire()  # Step 1.1
        item = random.randint(1, 10)  # Step 1.2
        print("Producer Producing Item:", item)
        items.append(item)  # Step 1.3
        print("Producer giving Notification")
        c.notify()  # Step 1.4
        c.release()  # Step 1.5
        time.sleep(5)


def consume(c):
    while True:
        c.acquire()  # Step 2.1
        print("Consumer waiting for update")
        c.wait()  # Step 2.2
        print("Consumer consumed the item", items.pop())  # Step 2.3
        c.release()  # Step 2.4
        time.sleep(5)


c = Condition()
t1 = Thread(target=consume, args=(c,))
t2 = Thread(target=produce, args=(c,))
t1.start()
t2.start()


from threading import *
import time
import random
import queue

items = []


def produce(c):
    while True:
        item = random.randint(1, 10)  # Step 1.2
        print("Producer Producing Item:", item)
        q.put(item)
        print("Producer giving Notification")
        time.sleep(5)


def consume(c):
    while True:
        print("Consumer waiting for update")
        print("Consumer consumed the item", q.get())
        time.sleep(5)


q = queue.Queue()
t1 = Thread(target=consume, args=(q,))
t2 = Thread(target=produce, args=(q,))
t1.start()
t2.start()


import queue

q = queue.Queue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get())

import queue

q = queue.LifoQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get())

import queue

q = queue.PriorityQueue()
q.put(10)
q.put(5)
q.put(20)
q.put(15)
while not q.empty():
    print(q.get())


import queue

q = queue.PriorityQueue()
q.put((1, "Ruhan"))
q.put((3, "Sharuk"))
q.put((4, "Ajay"))
q.put((2, "Siva"))
while not q.empty():
    print(q.get()[1])
