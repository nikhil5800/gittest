from multiprocessing import Process, Manager

def dothing(L, i):  # the managed list `L` passed explicitly.
    for elems in i:
        if elems % 2 == 0:
            L.append(i)


    # for j in range(5):
    #     text = "Process " + str(i) + ", Element " + str(j)
    #     L.append(text)

L = []

if __name__ == "__main__":
    with Manager() as manager:
        L = manager.list()  # <-- can be shared between processes.
        processes = []

        for i in range(5):
            p = Process(target=dothing, args=(L,[2,3,4,6,7,8,9,10],))  # Passing the list
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        L = list(L)
        print("Within WITH")
        print(L)

    print("Within IF")
    print(L)

#print("Outside of IF")
#print(L)