import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :

    arr = []
    for _ in range(5) :
        arr.append(input())   # 입력받아서 한 줄 씩 리스트에 ['ABCDE','abcde',...]

    max_len = 0
    for i in arr :
        if len(i) > max_len :
            max_len = len(i)   # arr 중 원소의 길이 최대값 찾기 (이걸 기준으로 순회할거임_

    h = ''
    for j in range(max_len) :    # j = const , i = 0, 1, 2 ... 인 arr[i][j] 차례로 저장
        for i in arr :
            if j <= len(i) - 1 :    # max_len 보다 짧은 문자열은 idx error 주의
                h += i[j]          # ( j 가 본인의 마지막 idx 보다 작아야 함 )

    print(f'#{tc} {h}')