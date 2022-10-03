# 행복한지 슬픈지
import sys
sys.stdin = open('10769.txt')
a = input()
happy = a.count(':-)')
sad = a.count(':-(')
if happy > sad :
    print('happy')
elif happy < sad :
    print('sad')
elif happy == 0 and sad == 0:
    print('none')
else:
    print('unsure')