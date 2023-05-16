답안 
n = int(input())
nums = []  #큐 배열 지정
for i in range(n): #배열에 입력받은 수 만큼 배열 추가
  nums.append(i+1)
front = 0
back = n-1

while back - front != 0: #큐의 길이가 1이 될 때까지 
  front += 1 #맨 앞 숫자 삭제
  num.append(nums[front]) #파이썬 append 함수를 활용하여 맨 뒤에 숫자 추가
  front += 1  #front좌표 및 back좌표 오른쪽으로 1칸씩 이동
  back += 1
