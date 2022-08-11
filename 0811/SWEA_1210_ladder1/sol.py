import sys
sys.stdin = open('input.txt')

for T in range(1, 11) :
    tc = int(input())

    # 사다리 배열 2차원 리스트로 받아 오기
    arr = []
    for _ in range(100) :
        lst = list(map(int, input().split()))
        arr.append(lst)

    # 도착지 (값 2인 위치)의 인덱스 값 [i][j] 찾기
    for i_idx in range(100) :
        for j_idx in range(100) :
            if arr[i_idx][j_idx] == 2 :
                i = i_idx
                j = j_idx

    while True :
        # y좌표 0 되면 탈출
        if i == 0 :
            break

        # 직진보다는 우 / 좌회전을 먼저
        # j = 오른쪽 끝 아니고
        if j < 99 :
            # 오른쪽 길 있으면
            if arr[i][j+1] == 1 :
                # 가기 전에 원래 위치에 1 지워주고 감
                # 끝에 도착했을 때 왔던 길에 1이 있으면 다시 돌아 갈 수도 있기 때문에!
                arr[i][j] = 0
                j = j+1
                continue

        # j = 왼쪽 끝 아니고
        if j > 0 :
            # 왼쪽 길 있으면
            if arr[i][j-1] == 1 :
                arr[i][j] = 0
                j = j-1
                continue

        # 양옆길 없으면 위로 감
        i -= 1

    print(f'#{tc} {j}')