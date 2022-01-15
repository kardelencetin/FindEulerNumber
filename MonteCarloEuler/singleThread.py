from FindEulerNumber import TicToc, FindEulerNumber

if __name__ == "__main__":
    tt = TicToc()
    tt.tic()
    finding_euler_number = FindEulerNumber()
    finding_euler_number.get_count_exceeds_one(10000000)
    euler_number = finding_euler_number.value_of_euler_number()
    print("Euler Number = %10.8f | I = %d | N = %d"
          % (euler_number, finding_euler_number.i, finding_euler_number.n))
    print("TIME = %.6f seconds" % (tt.toc()))
