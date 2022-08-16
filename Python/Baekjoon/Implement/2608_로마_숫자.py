# 2608 로마숫자
# https://www.acmicpc.net/problem/2608
roman = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

arab = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

arab2 = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}

def rtoa(r):
    res = 0
    for key, val in arab2.items():
        cnt = r.count(key)
        if cnt > 0:
            r = r.replace(key, '')
            res += cnt * val
    for key, val in arab.items():
        cnt = r.count(key)
        if cnt > 0:
            r = r.replace(key, '')
            res += cnt * val
    return res

def ator(a):
    res = ''
    for key, val in reversed(roman.items()):
        if a >= key:
            cnt = a // key
            res += val * cnt
            a -= key * cnt
    return res


A = input()
B = input()
ans = rtoa(A)+rtoa(B)
print(ans)
print(ator(ans))
