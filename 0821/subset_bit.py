arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n) :      # 모든 부분집합 2진수 생성
    for j in range(n) :     # 각 원소를 표현하는 이진수 생성
        if i & (1<<j) :     # 각 원소가 부분집합 i 에 포함되면
            print(arr[j], end=", ")     # 그 원소 출력
    print()
print()