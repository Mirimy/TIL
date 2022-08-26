import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())    # N 화덕 M 피자
    cheeze = list(map(int, input().split()))
    pizza = []
    for i in range(len(cheeze)) :
        pizza.append([i+1, cheeze[i]])
    print(pizza)

    q = []                          # 화덕 크기 만큼 화덕 만들기
    for _ in range(N) :             # 제일 처음 피자 채우기
        q.append(pizza.pop(0))

    while len(q) > 1 :              # q 에 남은 피자 1개 될 때까지
        a, b = q.pop(0)             # q 맨 앞에서 피자  빼서
        if b // 2 != 0 :            # 치즈 0 아니면
            q.append([a, b//2])     # [번호, 치즈//2] 해서 맨 뒤에 넣어주기
        else :                      # 치즈 0 이다?
            if pizza :              # 더 넣을 피자 있다면?
                q.append(pizza.pop(0))  # 순서대로 피자 넣어주기. 피자 없으면 pass

    print(f'#{tc} {q[0][0]}')
