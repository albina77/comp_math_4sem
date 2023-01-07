def func(r, n):
    if n != 0:
        x = func(r, n-1)
        return 4 * r * x * (1-x)
    else:
        return x0


n = int(input())
r = 0.4
ind = 2
x0 = 0.2
while ind != 0:
    for k in range(900, 902):
        a, b = [], []
        for i in range(k, k+2**n):
            a.append(func(r, i))
        for j in range(k+2**n, k+2**(n+1)):
            b.append(func(r, j))
        a = [i * 10000 // 1 for i in a]
        b = [i * 10000 // 1 for i in b]
        if a == b and a[0] != a[2**(n-1)]:
            ind = 1
        else:
            ind = 2
    if ind != 2:
        print(r)
        ind = 0
    r += 0.01
