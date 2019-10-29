lst1 = [2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20]
insert = []
update = []
def multi_run_wrapper(arg):
   return add(arg)
def add(x):
    if x % 2:
        insert.append(x)
    else:
        update.append(x)

print("nik")
if __name__ == "__main__":
    from multiprocessing import Pool
    pool = Pool(4)
    results = pool.map(multi_run_wrapper,lst1)
    print("nikhil")
