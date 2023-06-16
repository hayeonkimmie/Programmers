
# TODO maketrans 함수 사용 
# TODO 문자열(str) 객체에서 문자를 다른 문자로 매핑하기 위한 변환 테이블을 생성하는 함수
# TODO 첫 번째 인자는 변환할 문자들을 나타내는 문자열
# TODO 두 번째 인자는 대응되는 변환 문자들을 나타내는 문자열
# TODO 세 번째 인자는 삭제할 문자들을 나타내는 문자열 (선택적)
#? EXAMPLE 
#? translation_table = str.maketrans('ABC', '123')
#? 위의 코드는 'A'를 '1', 'B'를 '2', 'C'를 '3'으로 변환하는 테이블을 생성

# _ 문자열 바꿔서 찾기 
def solution(myString, pat):
    trans_func = str.maketrans('AB', 'BA') # 변환 테이블 생성 
    answer = 1 if myString.translate(trans_func).count(pat) > 0 else 0
    return answer

# _ 더 크게 합치기
def solution(a, b):
    n1 = int(str(a)+str(b))
    n2 = int(str(b)+str(a))

    return max(n1, n2)

# # 다른 풀이 
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


# _ 홀수 vs 짝수
def solution(num_list):
    max_value = max( sum([n for idx, n in enumerate(num_list) if idx %2==0]), sum([n for idx, n in enumerate(num_list) if idx %2==1]))
    return max_value


# # if문 대신 slice 이용한 풀이 
def solution(num_list):
    answer = max(sum(num_list[::2]), sum(num_list[1::2]))
    return answer


#! 한줄로 푸는게 효율적인지 의문.. 
# _ 배열 비교하기 
def solution(arr1, arr2):
    return 1 if len(arr1) > len(arr2) else -1 if len(arr1) < len(arr2) else 0 if sum(arr1) == sum(arr2) else 1 if sum(arr1) > sum(arr2) else -1

# _뒤에서 5등까지
def solution(num_list):
    num_list.sort()
    return num_list[:5]

# _ 홀짝에 따라 다른 값 반환하기
def solution(n):
    return sum(range(1,n+1,2)) if n%2==1 else sum([v**2 for v in range(0,n+1,2)])