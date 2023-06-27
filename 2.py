N = [int(i) for i in input().split()]
k = set(N)
d = list(k)
for i in range(len(d)):
    if i == len(d) - 1:
        g = d[i - 2] +  d[i] + d[i - 1]
        print(g)