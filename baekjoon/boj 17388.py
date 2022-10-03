# 와글와글 숭고한
import sys
sys.stdin = open('17388.txt')
S, K, H = map(int,input().split())
uv = S+K+H
if uv >= 100 :
    print('OK')
else:
    if S < K and S < H:
        print('Soongsil')
    elif K < S and K < H:
        print('Korea')
    else:
        print('Hanyang')