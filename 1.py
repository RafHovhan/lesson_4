i = int(input())
g = int(input())
a = [int(x) for x in input().split()]
b = [int(b) for b in input().split()]
k = set(a)
h = set(b)
j = sorted(k.intersection(h))
l = " ".join(str(x) for x in j)
print(l)