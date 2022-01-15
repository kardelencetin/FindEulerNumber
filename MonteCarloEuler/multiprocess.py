import random
import time
import os
from multiprocessing import Process, Array


class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2 - self.t1


class FindEulerNumber:
    def __init__(self):
        self.i = 0
        self.n = 0

    def get_count_exceeds_one(self, nn, p, all_i, all_n):
        for _ in range(nn):
            s = 0
            b = 0
            while s < 1:
                s += random.random()
                b += 1
            self.i += b
            self.n = nn
        all_i[p] = self.i
        all_n[p] = self.n

    def value_of_euler_number(self):
        return self.i / self.n


if __name__ == "__main__":
    for number_of_p in range(1, os.cpu_count() + 1):
        tt = TicToc()
        tt.tic()
        n = int(403200 / number_of_p)
        find_euler_number = []
        processes = []
        shared_i = Array('i', [0] * number_of_p)
        shared_n = Array('i', [0] * number_of_p)
        for i in range(number_of_p):
            find_euler_number.append(FindEulerNumber())
            processes.append(
                Process(target=find_euler_number[i].get_count_exceeds_one, args=(n, i, shared_i, shared_n)))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

        count = 0
        total = 0
        for i, n in zip(shared_i, shared_n):
            count += i
            total += n
            euler_number = (count / total)
        print(
            f"P={number_of_p} | Euler Number = {euler_number:.8f} | i/n={count}/{total} | Time = {tt.toc():.8f} seconds")
