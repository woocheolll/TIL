# PYthon



## 제어문 (Control Statement)

- 파이썬은 기본적으로 위에서 부터 아래로 순차적으로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 (분기/조건) 하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도로 표현이 가능



### 조건문

- 조건문은 참/ 거짓을 판단할 수 있는 조건식과 함께 사용



#### 기본형식

- expression 에는 참 거짓에 대한 조건식
  - 조건이 참인경우 이후 들여쓰기 되어있는 코드 블럭을 실행
  - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블럭을 실행
    - else는 선택적으로 활용

``` python
a = 10
if a >= 0:
    print('양수')  #참일경우 출력
else:
    print('음수')  ##거짓일경우 출력
print(a)
```



실습문제

- num에 숫자를 입력해 홀수인지 짝수인지 찾는 명령어

``` python
num = int(input('입력 : '))
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
    
print(num)
```





### 복수 조건문

``` python
if <expression>:
    # code block
elif <expression>:
    # code block
elif <expression>:
    # code block
else: 
    # code block
```

- 실습문제

``` python
dust= int(input('미세먼지 농도 : '))

if 150 < dust :
    print('매우나쁨')
elif 80 < dust :
    print('나쁨')
elif 30 < dust :
    print('보통')
else :
    print('좋음')
```



### 중첩 조건문

``` python
if <expression>:
    # code block
    if <expression>:
    	# code block
else: 
    # code block
      
```



- 실습

``` python
dust= int(input('미세먼지 농도 : '))

if 150 < dust :
    print('매우나쁨')
    if 300 < dust :
        print('야외활동은 자제하세요')
elif 80 < dust :
    print('나쁨')
elif 30 < dust :
    print('보통')
else :
    if 0 > dust :
        print('음수 입니다.')
    else:
        print('좋음')
```



## 반복문



### 종류

- while 문
  - 종료조건에 해당하는 코드를 통해 반복문을 종료시켜야함
- for 문 
  - 반복가능한 객체를 모두 순회하면 종료 (별도의 종료조건 없음)
- 반복 제어
  - break, continue, for-else





#### while 

- 참인 경우 반복적으로 코드를 실행
- 무한루프를 하지 않도록 종료조건 필요

```python
a = 0 
while a < 5:
    print(a)
    a += 1
print('끝')
```

