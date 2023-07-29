# python-starmap-async

How to pass arguments to python map_async using starmap_async example with logging.

Logging in combination with multiple processes with python can be challenging. This provides an example of combining both
logging with multiple processes running (via a `queue`), and also use of [starmap_async](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap_async)
to convenienly pass multiple arguments to a worker process (which isn't immediately obvious how to achive if you first search how to pass arguments with map_async arguments). 


# Usage
```
python3 `starmap_async_example.py`
```

Output:

```
INFO:root:Task 1 process ForkPoolWorker-1 started.
INFO:root:Task 2 process ForkPoolWorker-2 started.
INFO:root:Task 3 process ForkPoolWorker-3 started.
INFO:root:Task 1 running: hello
INFO:root:Task 2 running: world
INFO:root:Task 3 running: python
INFO:root:Task 1 process ForkPoolWorker-1 started.
INFO:root:Task 1 running: hello
INFO:root:Task 2 process ForkPoolWorker-2 started.
INFO:root:Task 2 running: world
INFO:root:Task 3 process ForkPoolWorker-3 started.
INFO:root:Task 3 running: python
INFO:root:Task 1 done
INFO:root:Task 1 process ForkPoolWorker-1 done.
INFO:root:Task 1 done
INFO:root:Task 1 process ForkPoolWorker-1 done.
INFO:root:Task 2 done
INFO:root:Task 2 process ForkPoolWorker-2 done.
INFO:root:Task 3 done
INFO:root:Task 3 process ForkPoolWorker-3 done.
INFO:root:Task 2 done
INFO:root:Task 2 process ForkPoolWorker-2 done.
INFO:root:Results:
INFO:root:Task 1 result
INFO:root:Task 2 result
INFO:root:Task 3 done
INFO:root:Task 3 result
INFO:root:Task 3 process ForkPoolWorker-3 done.
```

Resources:

- [Logging to a single file from multiple processes](https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes)
- [Multiprocessing Logging in Python](https://superfastpython.com/multiprocessing-logging-in-python/)
- [queue objects should only be shared between processes through inheritance](https://stackoverflow.com/questions/73384531/queue-objects-should-only-be-shared-between-processes-through-inheritance-even-w)
