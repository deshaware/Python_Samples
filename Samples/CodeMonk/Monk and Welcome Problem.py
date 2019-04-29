#inputting array
# Monk and Welcome Problem
items = input()
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
for z in range(int(items)):
    # ans.append(int(list1[z])+int(list2[z]))
    print(list1[z]+list2[z], end=" ")
# for i in ans:
#     print(i,end=" ")
# print(*ans)