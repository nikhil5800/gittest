from multiprocessing import Pool
#import workers
lst1 = [2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20]
insert = []
update = []
def fun(i):
        if i % 2 == 0:
            insert.append(i)
        else:
            update.append(i)

if __name__ ==  '__main__':
    pool = Pool(4)
    result = pool.map(fun, lst1)
    print(len(insert))



