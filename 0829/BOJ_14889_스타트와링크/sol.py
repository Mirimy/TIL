import sys
sys.stdin = open('input.txt')

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# N // 2 개 부분집합 만들어서 있으면 start팀에 없으면 link 팀에

sl_min = 100 * N * N
for i in range(1<<N) :
    start = []
    link = []
    s_score = 0
    l_score = 0
    if bin(i)[2:].count('1') == N // 2 :
        for j in range(N) :
            if i & (1<<j) :
                start.append(j)
            else :
                link.append(j)

        for i in start :
            for j in start :
                if i < j:
                    s_score += S[i][j] + S[j][i]

        for k in link :
            for l in link :
                if k < l:
                    l_score += S[k][l] + S[l][k]

        if abs(l_score - s_score) < sl_min :
            sl_min = abs(l_score - s_score)

print(sl_min)