def process_solution(a, k) :
    print(a)
    print(k)

def backtrack(a, k, input) :
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES                     # c -> [0, 1]

    if k == input :
        process_solution(a, k)                  # 답이면 원하는 작업을 한다.
    else :
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates) :           # i = 0, 1
            a[k] = c[i]                         # c[0] = True, c[1] = False
            backtrack(a, k, input)

def construct_candidates(a, k, input, c) :
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)