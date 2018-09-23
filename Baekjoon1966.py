num = int(input())
for i in range(num):
    a=[]
    count=0
    m , n = map(int, input().split())
    a = list(input().split())
    result = [0]*m
    result[n] = 1
    while True:
        if a.index(max(a)) == 0:
            del a[0]
            count+=1
            if result[0] == 1:
                print(count)
                break
            else:
                del result[0]
        else:
            a.append(a[0])
            del a[0]
            result.append(result[0])
            del result[0]
