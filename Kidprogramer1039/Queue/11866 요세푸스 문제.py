n,k = map(int, input().split())
nums = []
for i in range(n):
    nums.append(i+1)
result = [] #큐를 만들기 위한 배열, 그리고 좌표 생성
front = 0 
back = n-1 

while back - front != -1:
    for i in range(k-1):
        nums.append(nums[front]) #앞의 숫자 2개를 뒤로 옮기고, 큐의 head와 tail 부분을 2칸씩 이동 
        front += 1
        back += 1
    result.append(nums[front]) # 3칸마다 head 부분을 개별 기록
    front += 1

list_str = str(result)[1:-1] #배열을 문자화 한 후, 양끝을 슬라이스 처리
print("<"+list_str+">")
