# 모음의 개수
# 영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.
import sys

sys.stdin = open("1264.txt")
a = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
while True:
    b = list(input())
    count_ = 0
    if b[0] == '#':
        break
    for i in b :
        if i in a :
            count_ += 1

        
    print(count_)