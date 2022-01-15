import random
import time

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

    def get_count_exceeds_one(self, nn):
        i = 0
        for _ in range(nn):
            s = 0
            b = 0
            while s < 1:
                s += random.random()
                b += 1
            i += b
        self.n = nn
        self.i = i

    def value_of_euler_number(self):
        return self.i / self.n

