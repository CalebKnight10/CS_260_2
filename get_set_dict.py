import timeit

d = {}


def time_dict_set(n):
    global d
    for i in range(n):
        d[i] = i


def time_dict_get(n):
    global d
    for i in range(n):
        x = d[i]


def main():

    k = 10
    print ("Lets check the dict setter times: ")
    for n in range(123456, 1000001, 101010):
        set_time = timeit.Timer("time_dict_set("+str(n)+")",
                               "from __main__ import time_dict_set")
        sett = set_time.timeit(k)
        print ("Time for {} dict sets: {}".format(n, sett))
        print ("Time for {} dict sets: {}".format(1, sett/float(k*n)))

    print ("And the dict getter times: ")
    for n in range(123456, 1000001, 101010):
        get_time = timeit.Timer("time_dict_get("+str(n)+")",
                               "from __main__ import time_dict_get")
        gett = get_time.timeit(k)
        print ("Time for {} dict gets: {}".format(n, gett))
        print ("Time for {} dict gets: {}".format(1, gett/float(k*n)))


if __name__ == '__main__':
    main()