num = int(input())
for i in range(num):
    m , n = map(int, input().split())
    a = 0
    if m > n:
        for j in range(1,m+1):
            if (m%j==0) and (n%j==0):
                a = j
    else:
        for j in range(1,n+1):
            if (m%j==0) and (n%j==0):
                a = j
    print(int((m*n)/a))
