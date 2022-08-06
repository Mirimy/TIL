# 첫 번째 원소부터 인접한 원소끼리 계속 자리를
# 교환하면서 맨 마지막 자리까지 이동
# 시간복잡도 : O(n^2) (이중for문)


# 구간의 끝 정하기
# for i : n-1 -> 1
#   for j : 0 -> i-1
#       if arr[j] arr[j+1] (왼쪽이 크면)
#           arr[j] <-> arr[j+1] (자리 바꿈)

def BubbleSort(a,N) :
    for i in range(N-1, 0, -1) :
        for j in range(0, i) :
            if a[j] > a[j+1] :
                a[j], a[j+1] = a[j+1], a[j]
    return a

lst = [98,55, 7, 78, 12, 42]
print(BubbleSort(lst, len(lst)))
