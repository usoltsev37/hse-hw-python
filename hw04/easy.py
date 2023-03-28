from multiprocessing import Process
from threading import Thread
from time import time

THREADS = 10
N = 50000


def fibonacci(n: int):
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(result[i - 1] + result[i - 2])
    return result


def calc_time_sync():
    start_time = time()
    for _ in range(THREADS):
        fibonacci(N)
    end_time = time()
    return end_time - start_time


def calc_time_thread():
    start_time = time()
    threads = [Thread(target=fibonacci, args=(N,)) for _ in range(THREADS)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time()
    return end_time - start_time


def calc_time_process():
    start_time = time()
    processes = [Process(target=fibonacci, args=(N,)) for _ in range(THREADS)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    end_time = time()
    return end_time - start_time


def easy():
    with open('artifacts/easy.txt', 'w') as file:
        file.write(f'calc_time_sync: {str(calc_time_sync())}\n')
        file.write(f'calc_time_thread: {str(calc_time_thread())}\n')
        file.write(f'calc_time_process: {str(calc_time_process())}\n')
