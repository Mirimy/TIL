# 합이 10이 되는 부분집합의 경우의 수

def f(i, N) :
    global answer
    if i == N :
        s = 0
        for i in range(N) :
            if bit[i] :
                s += A[i]

        if s == 10 :
            answer += 1     # 부분집합의 합이 10인 경우의 수
            for i in range(N) :
                if bit[i] :
                    print(A[i], end=' ')
            print()
    else :
        bit[i] = 1      # A[i]가 부분집합에 포함
        f(i+1, N)       # i 다음 부분을 결정하러 갈래
        bit[i] = 0      # A[i]가 부분집합에 불포함
        f(i+1, N)       # i 다음 부분을 결정하러 갈래   .... 10까지 쭉쭉

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
f(0, 10)
print(f'경우의 수는 {answer}')