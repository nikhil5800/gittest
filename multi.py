import multiprocessing as mp
from ctypes import c_char_p

def init(aa, vv):
    global a, v
    a = aa
    v = vv

def worker(i):
    a[i] = v.value * i

if __name__ == "__main__":
    N = 10
    a = mp.Array('i', [0]*N)
    v = mp.Value('i', 3)
    p = mp.Pool(initializer=init, initargs=(a, v))
    p.map(worker, range(N))
    print(a[:])