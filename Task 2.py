import math
import numpy as np
from multiprocessing import Process, Pool
import matplotlib.pyplot as plt



def monte_carlo(edge_x1, edge_x2, edge_y1, edge_y2, function, num):
    edge_x = abs(edge_x1 - edge_x2)
    edge_y = abs(edge_y1 - edge_y2)
    ry = np.random.random(num)
    rx = np.random.uniform(edge_x1, edge_x2, num)
    hit = num_of_hit(rx, ry, function, num)
    return edge_x * edge_y * hit / num


def num_of_hit(rx, ry, function, n):
    k = 0
    for i in range(n):
        if function(rx[i]) >= ry[i]:
            k += 1
    return k


def mistake(edge_x1, edge_x2, edge_y1, edge_y2, function, n):
    a = np.array(
        [abs(monte_carlo(edge_x1, edge_x2, edge_y1, edge_y2, function, n) - 1) for i in range(100)])
    return (n, np.sum(a) / 100)


def function(x):
    return np.cos(x)

if __name__ == '__main__':
    edge_x1, edge_x2 = 0, np.pi / 2
    edge_y1, edge_y2 = 0, 1



    # for i in range(1000, 2000, 4):
    #     p1 = Process(target=mistake, args=(edge_x1, edge_x2, edge_y1, edge_y2, function, i, arr))
    #     p1.start()
    #     p2 = Process(target=mistake, args=(edge_x1, edge_x2, edge_y1, edge_y2, function, i + 1, arr))
    #     p2.start()
    #     p3 = Process(target=mistake, args=(edge_x1, edge_x2, edge_y1, edge_y2, function, i + 2, arr))
    #     p3.start()
    #     p4 = Process(target=mistake, args=(edge_x1, edge_x2, edge_y1, edge_y2, function, i + 3, arr))
    #     p4.start()

    pool = Pool(processes=4)
    arr1 = [pool.apply_async(mistake, args=(edge_x1, edge_x2, edge_y1, edge_y2, function, i)) for i in range(1000, 10000, 200)]
    arr = [p.get() for p in arr1]
    N_ = []
    V_ = []
    print(arr)
    for i in arr:
        N_.append(math.log(i[0], 10))
        V_.append(math.log(i[1], 10))


    plt.plot(N_, V_, 'ro')
    plt.show()
