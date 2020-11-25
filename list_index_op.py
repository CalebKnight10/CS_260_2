import random
import timeit

test_list = list(range(123456))
c = 10000
def verify_list_index_one(test_list, n):
    for i in range(c):
        index = random.randint(0, c-1)
        test_list[index]


def main():
    for n in range(123456, 10000001, 101010):
        indexTime = timeit.Timer("verify_list_index_one(test_list,"+str(n)+")",
                                 "from __main__ import test_list,\
                                 verify_list_index_one")
        it = indexTime.timeit(number = 10)
        print ("TOTAL TIME for %d index access in %d list of"\
               "numbers :%15.9f seconds" % (c, n, it))


if __name__ == '__main__':
    main()