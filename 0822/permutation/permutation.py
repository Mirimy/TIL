'''
[1, 2, 3] 의 순열 만들기
'''

def permutation(idx, N, r) :
    if idx == N :
        print(data[:r])
    else :
        for j in range(idx, N) :
            data[idx], data[j] = data[j], data[idx]
            permutation(idx + 1, N, r)
            data[idx], data[j] = data[j], data[idx]     # 원래 자리로 돌려놓기


data = [1, 2, 3]
permutation(0, len(data), 3)