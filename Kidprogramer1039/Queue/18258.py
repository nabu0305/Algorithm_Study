#18258번 큐2 답안
import sys 
input = sys.stdin.readline

n = int(input())
queue = []
front = 0
back = -1
for i in range(n):
  command = input()[:-1] #위의 sys 라이브러리에서 readline은 개행 문자를 포함하기에, 그걸 지워주려고 -1까지 리스트 슬라이스 했음.
  if command[0:4] == 'push': #push일 경우 : 파이썬 리스트 메서드 중 append 메서드 사용
    queue.append(int(command[5:]))
    back += 1
  elif command == 'pop': #pop일 경우: 좌표를 변경함으로써 굳이 배열에서 정수를 빼지 않는 방식으로 진행. 
   if back - front == -1:
    print(-1)
   else :
    print(queue[front])
    front+=1
 elif command == 'size': #size일 경우: 맨 뒤에서 맨 앞을 빼고, 1을 더해줌(아무 것도 없을 때는 -1이 아니라 0이 나와야 하기 때문)
  print(back-front+1)
 elif command == 'empty': #empty일 경우: 비어 있는 큐일 경우 1, 아니면 0을 출력하게 함(큐가 비어있다고 판단하는 기준 : back 좌표에서 front 좌표를 뺐을 때 -1이 나오는 경우(빠진 수도 없고(front) 들어간 수(back)도 없으니 비어있다고 판단))
  if back - front == -1:
    print(1)
  else:
    print(0)
 elif command == 'front': #front일 경우 : 큐의 변화가 없는 상태(-1)일 경우 그대로 출력하고, 아닐 경우에는 queue의 front좌표를 출력
  if back - front == -1:
    print(-1)
  else:
    print(queue[front])
 elif command == 'back': #back일 경우 : front와 동일하지만, 출력하는 좌표만 다름
  if back-front == -1:
    print(-1)
  else:
    print(queue[back])
else:
  continue
    
