case = int(input())
num = 1

while case > 0 :
    case -= 1

    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max = -1000

    if n < m :
        for i in range(m - n + 1) :
            result = [a[i] * b[i] for i in range(len(a))]
            result = sum(result)
            if result > max :
                max = result
            a.insert(0,0)
    elif n > m :
        for j in range(n - m + 1) :
            result = [a[i] * b[i] for i in range(len(b))]
            result = sum(result)
            if result > max :
                max = result
            b.insert(0,0)
    else :
        result = [a[i] * b[i] for i in range(len(a))]
        result = sum(result)

    print(f'#{num} {max}')
    num += 1