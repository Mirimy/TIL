def my_strcmp(word1, word2) :
    # 두 단어중 더 짧은 단어의 길이 파악
    if len(word1) < len(word2) :
        short = len(word1)
    else :
        short = len(word2)
    # 두 단어를 짧은 단어의 길이를 기준으로 비교해 나갈건데
    for i in range(short) :
        # 만약 두 알파벳이 다르다.
        if word1[i] != word2[i] :
            # 두 단어의 ASCII 코드 값의 차를 반환
            return ord(word1[i]) - ord(word2[i])
    # 만약 짧은 단어 기준으로 비교했는데 서로 다른 알파벳이 없다면
        # 두 단어의 길이가 같으면 0 반환
    if len(word1) == len(word2) :
        return 0
        # word1이 더 길면 : 사전 순서상 뒤가 될테니 1 반환
    elif len(word1) > len(word2) :
        return 1
        # 아니면 -1 반환
    else :
        return -1

# 파이썬에서는 그냥 이렇게 쓰면 됨
def my_strcmp2(word1, word2) :
    if word1 == word2 :
        return 0
    else :
        if word1 > word2 :
            return -1
        else :
            return 1


print(my_strcmp('abc', 'abcd'))
print(my_strcmp('Zab', 'zab'))