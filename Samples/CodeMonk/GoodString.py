# no tests
def main():
    longest = 0
    temp = 0
    count = 0
    s = input()
    for i in s:
        if(isVowel(i)):
            temp = temp + 1
            # if(count == 0):
            # if(count != 0 and isVowel(s[count])):
            #     temp = temp + 1
            #     longest = temp
            if(temp > longest):
                longest = temp
        else:
            temp = 0
            count = count + 1
    print(longest)


def isVowel(i):
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
       i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        return True
    else:
        return False


def test():
    count = 0
    i = input()
    for j in i:
        print(i[count])
        count = count + 1


main()
