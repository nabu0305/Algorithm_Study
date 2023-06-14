#15:08 ~ 18:43
import sys
from copy import deepcopy

class Node:
    def __init__(self, data):
        self.data = data  #data는 값을 가리키는 변수(속성, attribute)
        self.next = None  #next는 다음 노드를 가리키는 변수

class Linked_list:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    
    def appendleft(self, data): # 맨 앞에 숫자를 추가하는 함수
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1    
        
    def append(self, data): # 맨 뒤에 숫자를 추가하는 함수
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        self.length += 1

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        if self.head.next is None:
            self.head = None
        else:
            while node.next is not None:
                prev = node
                node = node.next
            prev.next = None
        self.length -= 1
        return node.data
    
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            node = self.head
            while node.next: #node.next is not None
                print(node.data, end = " → ")
                node = node.next
            print(node.data)    

result = 0
N,M = map(int, sys.stdin.readline().split())
quest = list(map(int, sys.stdin.readline().split()))

list = Linked_list() #list를 연결리스트 인스턴스로 지정
temList = Linked_list() #list를 연결리스트 인스턴스로 지정
list2 = Linked_list() #list를 연결리스트 인스턴스로 지정
temList2 = Linked_list() #list를 연결리스트 인스턴스로 지정

for i in range(1, N+1): #1부터 N까지 숫자 입력
    list.append(i)
for i in range(1, N+1): #1부터 N까지 숫자 입력
    list2.append(i)

for j in quest:
    LeftRes = 0
    RightRes = 0
    while True: #한 칸씩 전부 왼쪽으로 이동
        if list.head.data == j:
            list.popleft()
            break
        else:
            k = list.popleft()
            list.append(k)

            LeftRes += 1
    while True: #한 칸씩 전부 오른쪽으로 이동
        if list2.head.data == j:
            list2.popleft()
            break
        else:
            q = list2.pop()         
            list2.appendleft(q)
            RightRes += 1
    # print(f"j : {j}, left : {LeftRes}, Right : {RightRes}")
    if LeftRes < RightRes:
        list2 = deepcopy(list)
        result += LeftRes
    elif LeftRes >= RightRes:
        list = deepcopy(list2)
        result += RightRes
print(result)
