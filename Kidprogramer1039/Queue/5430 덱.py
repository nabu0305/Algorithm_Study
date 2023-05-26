from collections import deque

#코드 출처 : https://moonlight-spot.tistory.com/entry/%EB%B0%B1%EC%A4%80-5430-AC-in-%ED%8C%8C%EC%9D%B4%EC%8D%AC

T = int(input())
for tc in range(T):
    query = input()
    k = int(input())
    # q: 입력받은 배열 양방향 큐에 담기
    q = deque(input()[1:-1].split(','))
    # flag: R(뒤집기)를 한 번만 실행하기 위함
    flag = 0
    
    # TIP! deque는 [''] 의 길이를 0이 아닌 1로 취급하기 때문에 초기화 필요!
    if k == 0:  
        q = []
    
    for c in query:
        if c == 'R':
            flag += 1
        elif c == 'D':
            if len(q) == 0:
                print('error')
                break
            else:
                if flag % 2 == 1:
                    q.pop()
                else:
                    q.popleft()
                        
    else:
        if flag % 2 == 1:
            q.reverse()
        print('[' + ','.join(q) + ']')
