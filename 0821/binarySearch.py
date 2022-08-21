def binarySearch(S, E, key) :


    while S <= E :
        middle = (S + E) // 2
        print(middle)
        if middle == key :
            return('찾았다!')
        elif middle > key :
            E = middle
        else :
            S = middle
    return '실패!'


print(binarySearch(0, 400, 275))