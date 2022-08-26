import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())    # N 화덕 M 피자
    pizza = list(map(int, input().split()))

    q = [0] * N             # 화덕 크기 만큼 화덕 만들기
    num = [0] * N           # 화덕 크기 만큼 화덕 자리에 넣을 피자 번호
    for i in range(N) :     # 초기 설정 (피자 1~N 번까지, 번호 1~N 번까지 넣기)
        q[i] = pizza[i]
        num[i] = i + 1

    p_idx = N - 1           # 이번에 채운 피자 idx (화덕 빈자리 생기면 +1)
    target = -1
    while len(pizza) != 1 :
        target = (target + 1) % N      # target : 0, 1, 2 , 0, 1, 2 , ...
        q[target] = q[target] // 2

        if q[target] == 0 :            # 화덕의 target 자리 0이 되면
            if p_idx < M - 1 :              # 1 // 피자 마지막번호까지 안넣었으면
                p_idx += 1                  # 피자 인덱스 +1 해서
                q[target] = pizza[p_idx]    # 빈 자리에 남은 피자 넣어주기
                num[target] = p_idx + 1     # 현재 화덕에 있는 피자 번호도 저장
            else :                          # 2 // 피자 마지막번호까지 다 넣었으면
                if q == [0] * N :           # 마지막에 남은 피자 나올때까지 계속 실행 ([2, 3, 0] 이럴땐 킵고잉)
                    break                   # 마지막으로 0 된 피자 나왔으면 탈출, 그때 target이 마지막 피자

    print(f'#{tc} {num[target]}')