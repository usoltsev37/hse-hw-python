import concurrent
import math
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time as current_time

THREADS = 10
N = 4000


def integrate(f, a, b, job_id=0, n_jobs=1, n_iter=1000):
    start_time = current_time()
    acc = 0.0
    left = job_id * (n_iter // n_jobs)
    right = min(n_iter, (job_id + 1) * (n_iter // n_jobs))
    for i in range(left, right):
        acc += f(a + i * (b - a) / n_iter) * (b - a) / n_iter
    return acc, job_id, start_time


def run(f, a, b, n_jobs, executor, log_file):
    start_time = current_time()
    threads = []
    with executor(max_workers=n_jobs) as executor:
        result = 0.0
        for i in range(n_jobs):
            threads.append(executor.submit(integrate, f, a, b, i, n_jobs))
        for thread in concurrent.futures.as_completed(threads):
            acc, job_id, start_time = thread.result()
            result += acc
            log_file.write(f'    job_id: {job_id}, start_time: {start_time}, result: {acc}\n')
        log_file.write(f'result: {result}\n')
    end_time = current_time()
    return end_time - start_time, result


def medium():
    with open('artifacts/logs.txt', 'w') as log_file, open('artifacts/medium.txt', 'w') as file:
        for n_jobs in range(1, 2 * multiprocessing.cpu_count() + 1):
            file.write(f'----------- {n_jobs} jobs -----------\n')
            log_file.write(f'----------- {n_jobs} jobs -----------\n')

            log_file.write('thread work: \n')
            time, result = run(math.cos, 0, math.pi / 2, n_jobs, ThreadPoolExecutor, log_file)
            file.write('thread work: \n')
            file.write(f'\ttime: {time}\n')
            file.write(f'\tresult: {result}\n----------------------\n')
            log_file.write('\n----------------------\n')

            log_file.write(f'process work:\n')
            time, result = run(math.cos, 0, math.pi / 2, n_jobs, ProcessPoolExecutor, log_file)
            file.write('process work: \n')
            file.write(f'\ttime: {time}\n')
            file.write(f'\tresult: {result}\n----------------------\n')
            log_file.write('\n----------------------\n')
