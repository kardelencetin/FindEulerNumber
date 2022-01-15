from FindEulerNumber import TicToc, FindEulerNumber
import os
from threading import Thread

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    n = 10000000
    find_euler_numbers = []
    threads = []
    for i in range(os.cpu_count()):
        find_euler_numbers.append(FindEulerNumber())
        threads.append(Thread(target=find_euler_numbers[i].get_count_exceeds_one, args=(n,)))
        print("Started thread number #%d" % i)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    total = 0
    count = 0
    for find_euler_number in find_euler_numbers:
        total += find_euler_number.i
        count += find_euler_number.n
    print("Euler Number = %.8f | I / N = %d / %d | TIME = %.5f seconds"
          % (total / count, total, count, tt.toc()))



