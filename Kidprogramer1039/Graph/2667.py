from collections import deque

def bfs(x, y, complex_num):
    global complex_size, complex_matrix, N

    queue = deque([(x, y)])
    complex_matrix[x][y] = complex_num
    size = 1

    while queue:
        cx, cy = queue.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < N and 0 <= ny < N and complex_matrix[nx][ny] == 1:
                complex_matrix[nx][ny] = complex_num
                size += 1
                queue.append((nx, ny))

    return size

def find_complex():
    global complex_size, complex_matrix, N

    complex_num = 2

    for i in range(N):
        for j in range(N):
            if complex_matrix[i][j] == 1:
                size = bfs(i, j, complex_num)
                complex_size.append(size)
                complex_num += 1

def main():
    global complex_size, complex_matrix, N

    N = int(input())
    complex_matrix = [list(map(int, input().strip())) for _ in range(N)]
    complex_size = []

    find_complex()

    print(len(complex_size))
    for size in sorted(complex_size):
        print(size)

if __name__ == "__main__":
    main()
