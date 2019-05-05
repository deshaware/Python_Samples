# import array
# arr = list()
# n = input("N ")
# for i in range(int(n)):
#     #take inputs
#     list1 = list(map(int, input().split()))
#     arr = array.array(list1)
#     list1.clear()
# for i in range(n):
#     print(arr[i])
T = input()
for t in range(int(T)):
    N = input()
    lst = list()
    for i in range(int(N)):
        l = list(map(int, input().split()))
        lst.append(l)
    # input done, now gotta cal
    count = 0
    for i in range(int(N)):
        for j in range(int(N)):
            a = i
            p = i
            b = j
            q = j
            while p < int(N):
                while q < int(N):
                    if(lst[a][b] > lst[p][q] and p >= a and q >= b):
                        count = count + 1
                    q = q + 1
                p = p + 1
                q = 0
    # for i in range(int(N)):
    #     print(lst[i])
    print(count)
