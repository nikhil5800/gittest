import multiprocessing
from ctypes import c_char_p
import traceback
import numpy as np

def tonumpyarray(shared_array):
    '''Create numpy array from shared memory.'''
    try:
        nparray= np.frombuffer(shared_array,dtype=c_char_p)
        assert nparray.base is shared_array
        return nparray
    except:
        print(traceback.format_exc())



def square_list(mylist, result, lst):
    """
    function to square a given list
    """
    # append squares of mylist to result array
    try:
        for idx, num in enumerate(mylist):
            if num in lst:
                result[idx] = c_char_p(num.encode('utf-8'))

        # square_sum value


    # print result Array
        print("Result(in process p1): {}".format(result[:]))
    except:
        print(traceback.format_exc())



    # print square_sum Value



if __name__ == "__main__":
    # input list
    mylist = ['sku1','sku2','sku3','sku4']
    lst = ['sku2','sku4']
    # creating Array of int data type with space for 4 integers
    result = multiprocessing.Array(c_char_p, len(mylist))

    #lst = [2,4]
    # creating Value of int data type
    #square_sum = multiprocessing.Value(c_char_p)

    # creating new process
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, lst))

    # starting process
    p1.start()

    # wait until process is finished
    p1.join()
    p1.close()
    # print result array

    print(tonumpyarray(result))

    # print square_sum Value
    #print("Sum of squares(in main program): {}".format(square_sum.value))

