# 2231
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다.
# 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# input 216

    
num = int(input())
num2 = 0
for i in range(1, num):
    a = list(map(int, str(i)))  # 자리수 리스트
    num2 = i + sum(a) # i와 i 자릿수 합을 num2 입력
    if num == num2 :
        print(i)
        break
else:
    print(0)



