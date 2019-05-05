def cal_pal(name):
    if(name[::-1] != name):
        print("NO")
    else:
        if(len(name) % 2 == 0):
            print("YES EVEN")
        else:
            print("YES ODD")

test = input("tests")
name = list()
for i in range(int(test)):
    n = input("name")
    cal_pal(n)
    # name.append(n)
# for n in name:
    # res = cal_pal(n)
    # print(res)

#consuming
# def cal_pal(name):
#     if(name[::-1] != name):
#         return "NO"
#     else:
#         if(len(name) % 2 == 0):
#             return "YES EVEN"
#         else:
#             return "YES ODD"

# def reverse(name):
#     temp = ""
#     for i in name:
#         temp = i + temp
#     return temp

# test = input()
# name = list()
# for i in range(int(test)):
#     n = input()
#     name.append(n)
# for n in name:
#     res = cal_pal(n)
#     print(res)
             
        
        

