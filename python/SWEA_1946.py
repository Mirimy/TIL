T = int(input())
num = 1

while T > 0 :
    T = T - 1
    N = int(input())
    doc = [""]

    for i in range(N) :
        Ci,Ki = input().split()
        Ki = int(Ki)
        while Ki > 0 :
            Ki = Ki - 1
            if len(doc[-1]) < 10 :
                doc[-1] = doc[-1] + Ci
            else :
                doc.append("")
                doc[-1] = doc[-1] + Ci

    print("#{0}".format(num))
    for raw in range(len(doc)) :
        print(doc[raw])
    num = num + 1