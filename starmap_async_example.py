from multiprocessing import Pool, Queue, current_process
import time
import logging
import threading
from logging.handlers import QueueHandler

"""
Take three arguments using startmap_async
"""


def logger_thread(q):
    while True:
        record = q.get()
        if record is None:
            break
        logger = logging.getLogger(record.name)
        logger.handle(record)


# Function to be executed by workers
def task(index, message):
    qh = QueueHandler(q)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    log.addHandler(qh)
    process = current_process()
    log.info(f"Task {index} process {process.name} started.")
    log.info(f"Task {index} running: {message}")
    time.sleep(2)
    log.info(f"Task {index} done")
    log.info(f"Task {index} process {process.name} done.")
    return f"Task {index} result"


if __name__ == "__main__":
    q = Queue()
    logging.basicConfig()
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    lp = threading.Thread(target=logger_thread, args=(q,))
    lp.start()

    # Data to process, a list of tuples with arguments for the task function # noqa: E501
    data = [(1, "hello"), (2, "world"), (3, "python")]
    # Create and configure the process pool
    with Pool() as pool:
        # Execute the tasks using pool.startmap_async()
        result_async = pool.starmap_async(task, data)

        # Wait for the async results (optional)
        result_async.wait()

        # Get the results from the async result object
        results = result_async.get()

        # Print the results
        log.info("Results:")
        for result in results:
            log.info(result)
    # And now tell the logging thread to finish up too
    q.put(None)
