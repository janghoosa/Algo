# 7682 틱택토
# https://www.acmicpc.net/problem/7682
direction = [
    # 세로
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # 가로
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # 대각선
    [0, 4, 8],
    [2, 4, 6],
]


def check(case):
    x = 0
    o = 0
    for i in direction:
        if case[i[0]] == case[i[1]] == case[i[2]]:
            if case[i[0]] == 'O':
                o += 1
            elif case[i[0]] == 'X':
                x += 1
    return x, o


def find(case):
    cntX = case.count('X')
    cntO = case.count('O')
    cntD = case.count('.')
    resX, resO = check(case)
    print(cntX, cntO, cntD, resX, resO)
    if resX > 0 and resO > 0:
        print('invalid')
        return
    if cntX > cntO+1:
        print('invalid')
        return
    if cntO > cntX:
        print('invalid')
        return
    if cntX == cntO + 1 and resX > 0 and resO == 0:
        print('valid')
        return
    if cntX == cntO and resX == 0 and resO > 0:
        print('valid')
        return
    if resO == 0 and cntD == 0 and cntX == cntO + 1:
        print('valid')
        return
    print('invalid')
    return

while True:
    tmp = input()
    if tmp == 'end':
        break
    find(tmp)
