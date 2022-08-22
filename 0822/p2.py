def process_solution(arr, k, result) :
    if result != 10 :
        return              # 원하는 결과 (합 10) 아니면 함수 끝내기

    for i in range(1, k+1) :
        if arr[i]  :
            print(data[i], end=' ')
    print()

def construct_candidator(c) :
    c[0] = 0
    c[1] = 1
    return 2

# arr : 부분집합을 구하기 위해 사용하거나 않거나 하는 원소들
# k : 현재 조사 위치
# N : 최대 조사 위치
# result
def powerset(arr, k, n, result) :

    c = [0] * MAXCANDIDATES

    # 언제까지 조사할거냐
    if k == n :
        # 내가 원하는 수식이 만들어 졌는지 확인할 함수
        process_solution(arr, k, result)
    else :
        k += 1
        # 유망성 조사
        ncandidates = construct_candidator(c)    # 조사 어떻게 할건지?
        for i in range(ncandidates) :
            # 내가 집어넣어준 arr의 k번째 값을 쓰거나 안쓱너ㅏ
            arr[k] = c[i]
            # arr[k] 번째를 쓴 상황일 때
            if arr[k] :
                powerset(arr, k, n, result + data[k])       # k 번째 넣었으면 data[k] 값 sum에 더해주기
            else :
                powerset(arr, k, n, result)             # k 번째 안넣었을 때

MAXCANDIDATES = 100
NMAX = 100

data = list(range(11))
arr = [0] * NMAX
powerset(arr, 0, 10, 0)