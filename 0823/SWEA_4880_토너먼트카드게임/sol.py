import sys
sys.stdin = open('input.txt')

def tournament(card, N, num) :
    global card_origin
    card_left = []
    card_right = []
    num_left = []
    num_right = []
    if N > 2 :                                  # 함수에 입력된 card 길이가 2보다 크면
        for i in range(N) :                     # 두 그룹으로 나누어서 (카드 번호와 사람 번호의 왼쪽/오른쪽 그룹)
            if i <= ((N+1) // 2) - 1 :          # 각각을 다시 토너먼트 함수에 넣어준다
                card_left.append(card[i])
                num_left.append(num[i])
            else :
                card_right.append(card[i])
                num_right.append(num[i])

        final_num = [tournament(card_left, len(card_left), num_left) , tournament(card_right, len(card_right), num_right)]
        final_card = [card_origin[final_num[0] - 1], card_origin[final_num[1] - 1]]
        winner = tournament(final_card, 2,  final_num)      # 왼쪽/ 오른쪽 그룹의 승자를 다시 함수에 넣어줌

    elif N == 2 :                               # 두 그룹으로 계속 쪼개다가 N이 2가 되면 승자를 가림
        if card[0] == 3 and card[1] == 1 :
            winner = num[1]
        elif card[0] == 1 and card[1] == 3 :
            winner = num[0]
        elif card[0] >= card[1] :
            winner = num[0]
        elif card[0] < card[1] :
            winner = num[1]

    elif N == 1 :                               # N 이 1명이면 부전승
        winner = num[0]

    return winner                               # 승자를 return 해준다



T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    card_origin = list(map(int, input().split()))
    num = []
    for i in range(N) :
        num.append(i+1)

    result = tournament(card_origin, N, num)
    print(f'#{tc} {result}')
