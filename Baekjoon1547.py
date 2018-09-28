num = int(input())
a = [1, 2, 3]
for i in range(num):
    m , n = map(int, input().split())
    b = a.index(m)
    c = a.index(n)
    a.remove(m)
    a.insert(b, n)
    del a[c]
    a.insert(c, m)
print(a[0])
