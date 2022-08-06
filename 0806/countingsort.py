# 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여,
# 선형 시간에 정렬하는 효율적인 알고리즘
# 수행시간 O(n+k)  // n이 비교적 작을 때만 가능

# 1. 주어진 정수 크기의 [0]*n 리스트를 만들고,
# 2. 정렬할 숫자를 인덱스로 활용하여 순회하면서 카운트 +1 한다.
#    각 숫자별 개수가 담긴 counts list를 인덱스로
# 3. counts[i] = counts[i-1] + counts[i] 하여 i 까지 누적 개수를 나타내는 리스트로.
# 4. 원래 data 리스트에서 가장 뒤의 1은 counts[1] 번째 자리에 위치한다. (1까지 counts[1]개 있으므로)
#    뒤에서부터 하나 정렬시키면 counts[i] 는 -1 한다.

def Counting_Sort(A, B, k) :
    # A [] -- 입력배열 (1 to k)
    # B [] -- 정렬된 배열
    # C [] -- 카운트 배열

    # 1.
    C = [0] * (k+1)
    # 2.
    for i in range(0, len(A)) :
        C[A[i]] += 1
    # 3.
    for i in range(1, len(C)) :
        C[i] += C[i-1]
    # 4.
    for i in range(len(B)-1, -1, -1) :
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]

    return B


lst = [4, 2, 6, 3, 3, 1, 1, 0, 3]
sorted_lst = [0]*len(lst)
print(Counting_Sort(lst, sorted_lst, 6))