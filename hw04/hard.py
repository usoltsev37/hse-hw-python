import codecs
import time
from datetime import datetime
from multiprocessing import Queue, Pipe, Process
from multiprocessing.connection import Connection


def A(queue: Queue, out_connection: Connection):
    while True:
        time.sleep(5)
        out_connection.send(queue.get().lower())


def B(in_connection: Connection, out_connection: Connection):
    while True:
        out_connection.send(codecs.encode(in_connection.recv(), "rot13"))


def hard():
    with open('artifacts/hard.txt', 'w') as file:
        queue = Queue()
        A_B_connection, B_A_connection = Pipe()
        B_M_connection, M_B_connection = Pipe()
        Process(target=A, args=(queue, A_B_connection), daemon=True).start()
        Process(target=B, args=(B_A_connection, B_M_connection), daemon=True).start()

        print('------- START -------\n   !!! note: to quit type "quit" as input\n')
        while True:
            message = input('input: \n')
            if message == 'quit':
                file.write(f'end: {datetime.now()}\n')
                break

            file.write(f'input: "{message}"\n\ttime: {datetime.now()}\n')
            queue.put(message)
            message = M_B_connection.recv()
            file.write(f'output: "{message}"\n\ttime: {datetime.now()}\n')
