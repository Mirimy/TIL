import sys
sys.stdin = open('input.txt')

N = int(input())
sw = list(map(int, input().split()))
stu_num = int(input())      # 1 남 2 여
stu = [list(map(int, input().split())) for _ in range(stu_num)]     # [성별,번호]

for i in stu :
    if i[0] == 1 :                    # 남자
        for j in range(1, N + 1) :    # 스위치 1 ~ N 의 j번에 대해
            if j % i[1] == 0 :        # j가 내 번호의 배수이면
                if sw[j - 1] == 1 :       # j번째 스위치 상태 바꾸기
                    sw[j - 1] = 0
                else :
                    sw[j - 1] = 1
    elif i[0] == 2 :                                # 여자
        for lr in range(N // 2 + 1) :            # 좌우가 0~N//2씩 차이나는 lr에 대해
            l = i[1] - 1 - lr
            r = i[1] - 1 + lr
            if 0 <= l < N and 0 <= r < N and sw[l] == sw[r] :
                if sw[l] == 1 :
                    sw[l] = sw[r] = 0
                else :
                    sw[l] = sw[r] = 1
            else :
                break

while len(sw) > 0 :             # 20개씩 끊어서 출력
    for i in range(20) :
        if i > len(sw) - 1 :
            break
        print(sw[i], end=' ')
    sw = sw[20:]
    print()
