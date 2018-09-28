n, m = map(int,input().split())

list = [i for i in range(1,(n+1))]
answer=[0]*n
index=0
delete = m-1
while (len(list)!=0):
    while delete >= len(list):
        print("delete", delete)
        delete = delete - len(list)
        print("after delete: ", delete)
    print("index: ", index)
    answer[index] = list[delete]
    print(answer)
    del list[delete]
    delete =delete + (m-1)
    index+=1

print("<" + ", ".join(map(str, answer)) + ">")
