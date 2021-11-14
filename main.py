import time
value = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


def judge(r, n):
    ans = ''
    if(n >= 0 and n < 4):
        ans += value[2*(r - 1)] * n
    elif(n >= 4 and n < 9):
        m = n - 5
        if(m >= 0):
            ans += value[2*(r - 1)+1]
            ans += value[2*(r - 1)] * m
        else:
            ans += value[2*(r - 1)] * (m * -1)
            ans += value[2*(r - 1)+1]
    else:
        ans += value[2*(r - 1)] * (10 - n)
        ans += value[2*(r - 1)+2]
    return ans


def romam_num(n):
    if(n >= 0 and n < 4000):
        m = str(n)
        ans = ''
        for i in range(len(m)):
            ans += judge(len(m) - i, int(m[i]))
        return ans
    else:
        return 'Error, Please Input 0 <= n < 4000'


start = time.time()
for i in range(1, 4000):
    print(romam_num(i))
end = time.time()
print(end - start)
