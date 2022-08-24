# 3107 IPv6
# https://www.acmicpc.net/problem/3107
compressed = input()
tmp = compressed.split(':')
if '::' in compressed:
    newtmp = []
    index = 0
    while index < len(tmp):
        if tmp[index] == '':
            for i in range(9-len(tmp)):
                newtmp.append('0')
            if tmp[index+1] == '':
                index += 1
                newtmp.append('0')
        else:
            newtmp.append(tmp[index])
        index += 1
    tmp = newtmp
for i in range(8):
    tmplist = list(tmp[i])
    add0 = 4 - len(tmplist)
    for j in range(add0):
        tmplist.insert(0,'0')
    tmp[i] = ''.join(tmplist)
for i in range(7):
    print(tmp[i],end=':')
print(tmp[7])