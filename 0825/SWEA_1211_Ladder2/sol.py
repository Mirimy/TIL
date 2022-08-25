import sys
sys.stdin = open('input.txt')

for _ in range(1, 11) :
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    q = []
    for j in range(100) :
        if arr[0][j] == 1 :
            q.append([0, j])

    min_counts = [0, 100 * 100]
    for si, sj in q :
        visited = [[0] * 100 for _ in range(100)]
        counts = [sj, 0]

        while si < 100 :
            visited[si][sj] = 1

            if sj - 1 >= 0 and arr[si][sj - 1] == 1 and visited[si][sj - 1] == 0 :
                si, sj = si, sj - 1
            elif sj + 1 < 100 and arr[si][sj + 1] == 1 and visited[si][sj + 1] == 0 :
                si, sj = si, sj + 1
            else :
                si, sj = si + 1, sj
            counts[1] += 1

        if counts[1] < min_counts[1] :
            min_counts = counts

    print(f'#{tc} {min_counts[0]}')
