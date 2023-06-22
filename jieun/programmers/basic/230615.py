
#_  암호해독
def solution(cipher, code):
    return ''.join(list(cipher)[code - 1::code])

#_  개미군단
def solution(hp):
    res = hp // 5
    res2 = (hp - (res * 5)) // 3
    res3 = (hp - (res * 5) - (res2 * 3))
    return res + res2 + res3

#_  접미사인지 확인하기
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))

#_  더 크게 합치기
def solution(a, b):
    return max(int(str(a) + str(b)), int(str(b) + str(a)))

