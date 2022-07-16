case = int(input())

lst = list(map(int,input().split()))

lst.sort()

a = int(case / 2)

print(lst[a])