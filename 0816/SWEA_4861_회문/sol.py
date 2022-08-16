import sys
sys.stdin = open('input.txt')

def reverse_char(N, M, arr) :
    # 가로
    for i in range(N):
        for st in range(0, N - M + 1):  #  M 길이의 시작위치(st) 될 수 있는 범위
            if arr[i][st] != arr[i][st + M - 1]:   # M 길이 양끝단 다르면 조사 x
                continue
            elif arr[i][st + 1:st + M - 1] == arr[i][st + M - 2:st:-1]:    # M길이 양끝의 안쪽 조사
                return arr[i][st:st + M]    # 회문은 총 1개 존재하기 때문에 찾으면 바로 return

    # 세로
    for j in range(N):
        char = ''
        for i in range(N):  # j 같은 값 (세로줄) 한줄씩 뽑아서
            char += arr[i][j]  # char 에 저장 / j=0, 1, 2,.. 일 때 세로줄

        for st in range(0, N - M + 1):  # char에서 검사 시작할 위치 설정
            if char[st] != char[st + M - 1]:
                continue
            elif char[st + 1:st + M - 1] == char[st + M - 2:st:-1]:
                return char[st:st + M]

    # 회문 없으면?
    return False


T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())

    arr = []
    for _ in range(N) :
        arr.append(input())

    result = reverse_char(N, M, arr)
    print(f'#{tc} {result}')