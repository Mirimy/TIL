arr = [2, 6, 4, 5, 1, 7, 3, 8]

n = len(arr)

for i in range(4) :     # range 조정해서 원하는 위치까지만 '선택' 정렬 가능
    min_idx = i
    for j in range(i, n) :
        if arr[j] < arr[min_idx] :
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)