# https://programmers.co.kr/learn/courses/30/lessons/81303?language=python3
# 표 편집

delete = []

class Node:
    def __init__(self):
        self.prev = None
        self.removed = False
        self.next = None
    
def deleteNode(cur):
    delete.append(cur)
    cur.removed = True
    up = cur.prev
    down = cur.next
    if up:
        up.next = down
    if down:
        down.prev = up
        cur = down
    else:
        cur = up
    return cur
        
def restoreNode():
    recent = delete.pop()
    recent.removed = False
    up = recent.prev
    down = recent.next
    if up:
        up.next = recent
    if down:
        down.prev = recent

def prevNode(node, num):
    for _ in range(num):
        node = node.prev
    return node

def nextNode(node, num):
    for _ in range(num):
        node = node.next
    return node
    
def solution(n, k, cmd):
    answer = ''
    
    LL = [Node() for _ in range(n)]
    node = LL
    for i in range(1,n):
        LL[i-1].next = LL[i]
        LL[i].prev = LL[i-1]
    cur = LL[k]
    
    for ins in cmd:
        if ins[0] == 'U':
            x = int(ins[2:])
            cur = prevNode(cur, x)
        elif ins[0] == 'D':
            x = int(ins[2:])
            cur = nextNode(cur, x)
        elif ins[0] == 'C':
            cur = deleteNode(cur)
        elif ins[0] == 'Z':
            restoreNode()
            
            
    for i in LL:
        if i.removed:
            answer = answer+'X'
        else:
            answer = answer+'O'
    
    return answer