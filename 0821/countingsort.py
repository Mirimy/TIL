arr= [0, 4, 1, 3, 1, 2, 4, 1]
print(arr)
counts = [0] * 5

for i in arr :
    counts[i] += 1

print(counts)

for i in range(5) :
    if i != 0 :
        counts[i] += counts[i-1]

print(counts)
temp = [0] * len(arr)

for i in arr[::-1] :
    temp[counts[i]-1] = i
    counts[i] -= 1

print(temp)
