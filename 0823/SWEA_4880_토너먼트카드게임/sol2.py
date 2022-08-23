import sys
sys.stdin = open('input.txt')

def tournament(N, num) :
    num_left = []
    num_right = []
    if N > 2 :                                  # 함수에 입력된 card 길이가 2보다 크면
        for i in range(N) :                     # 두 그룹으로 나누어서 (카드 번호와 사람 번호의 왼쪽/오른쪽 그룹)
            if i <= ((N+1) // 2) - 1 :          # 각각을 다시 토너먼트 함수에 넣어준다
                num_left.append(num[i])
            else :
                num_right.append(num[i])

        final_num = [tournament(len(num_left), num_left) , tournament(len(num_right), num_right)]
        winner = tournament(2,  final_num)      # 왼쪽/ 오른쪽 그룹의 승자를 다시 함수에 넣어줌

    elif N == 2 :                               # 두 그룹으로 계속 쪼개다가 N이 2가 되면 승자를 가림
        if card[num[0] - 1] == 3 and card[num[1] - 1] == 1 :
            winner = num[1]
        elif card[num[0] - 1] == 1 and card[num[1] - 1] == 3 :
            winner = num[0]
        elif card[num[0] - 1] >= card[num[1] - 1] :
            winner = num[0]
        elif card[num[0] - 1] < card[num[1] - 1] :
            winner = num[1]

    elif N == 1 :                               # N 이 1명이면 부전승
        winner = num[0]

    return winner                               # 승자를 return 해준다



T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    card = list(map(int, input().split()))
    num = []
    for i in range(N) :
        num.append(i+1)

    result = tournament(N, num)
    print(f'#{tc} {result}')
