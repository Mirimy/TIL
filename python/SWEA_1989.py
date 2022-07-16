case = int(input())

word = []

for i in range(0, case) :
    word.append(str(input()))

num = 0


while num < case :
    if word[num] == word[num][::-1] :
        print("#{0} 1".format(num+1))
    else :
        print("#{0} 0".format(num+1))
    num = num + 1