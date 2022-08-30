# 7682 틱택토
# https://www.acmicpc.net/problem/7682
def flag(arr,equ):
    if arr[0][0]==arr[0][1]==arr[0][2]==equ:
        return True
    if arr[1][0]==arr[1][1]==arr[1][2]==equ:
        return True
    if arr[2][0]==arr[2][1]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][0]==arr[2][0]==equ:
        return True
    if arr[0][1]==arr[1][1]==arr[2][1]==equ:
        return True
    if arr[0][2]==arr[1][2]==arr[2][2]==equ:
        return True
    if arr[0][0]==arr[1][1]==arr[2][2]==equ:
        return True
    if arr[2][0]==arr[1][1]==arr[0][2]==equ:
        return True
    return False
    

while True:
    string=input()
    if string=="end":
        break
    else:
        cntX=0
        cntO=0
        index=0
        arr=[[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                arr[i][j]=string[index]
                if string[index]=="X":
                    cntX+=1
                if string[index]=="O":
                    cntO+=1
                index+=1
        if cntX>cntO+1:
            print("invalid")
            continue
        if cntO>cntX:
            print("invalid")
            continue
        if cntO==cntX:
            if flag(arr,"O") and not flag(arr,"X"):
                print("valid")
                continue
        if cntO+1==cntX:
            if flag(arr,"X") and not flag(arr,"O"):
                print("valid")
                continue
        if cntX==5 and cntO==4:
            if not flag(arr,"O"):
                print("valid")
                continue
        print("invalid")