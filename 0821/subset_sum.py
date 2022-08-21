arr = [0, 1, 2, 3, 1, -2, -3]

n = len(arr)

for i in range(1<<n) :
    sub_sum = 0
    zero_sum = []
    for j in range(n) :
        if i & (1<<j) :
            sub_sum += arr[j]
            zero_sum.append(arr[j])
    if sub_sum == 0 :
        print(zero_sum, sub_sum)
