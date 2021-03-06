# 데이터 구조



## 문자열(string)

- 문자들의 나열
  - 모든 문자는 str 타입
- 문자열은 ' '나  " "를 활용해 표기
  - 문자열을 묶을 때 동일한 문장 부호를 활용
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지하도록 함

| 문법        | 설명                                       |
| ----------- | ------------------------------------------ |
| s.find(x)   | x의 첫 번쨰 위치를 반환, 없으면, -1을 반환 |
| s.index(x)  | x의 첫 번쨰 위치를 반환, 없으면, 오류발생  |
| s.isalpha() | 알파벳 문자 여부                           |
| s.isupper() | 대문자 여부                                |
| s.islower() | 소문자 여부                                |
| s.istitle() | 타이틀 형식 여부 (제일 앞이 대문자)        |

### 문자열 변경

- replace(old, new[,count])
  - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
  - count를 지정하면, 해당 개수만큼만 시행
- strip([chars])
  - 특정한 문자들을 지정하면,
  - 양쪽을 제거하거나, 왼쪽을 제거하거나, 오른쪽을 제거
  - 문자열을 지정하지 않으면 공백을 제거함
- .split(sep = None, maxsplit = -1)
  - 문자열을 특정한 단위로 나눠 리스트로 반환
    - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음.
    - maxsplit이 -1인 경우에는 제한이 없음.
- 'separator'.join([iterable])
  - 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환
    - iterable에 문자열이 아닌 값이 있으면 TupeError 발생

## 리스트(list)

### 리스트의 정의

- 변경 가능한 값들의 나열된 자료형
- 순서를 가지며, 서로 다른 타입의 요소를 가질수 있음
- 변경 가능하며, 반복 가능함
- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분

### list 값 추가 제거

- .append(x)
  - 리스트에 값을 추가함
- extent(iterable)
  - 리스트에 iterable의 항목을 추가함

- .insert(i,x)
  - 정해진 위치에 i에 값을 추가함
- .remove(x)
  - 리스트에서 값이 x인 것 삭제
- .pop(i)
  - 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
  - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함
- .clear()
  - 모든 항목을 삭제함

### 탐색 및 정렬

- .index(x)
  - x값을 찾아 해당 index 값을 반환
- .count(x)
  - 원하는 값의 개수를 반환함
- .sort()
  - 원본 리스트를 정렬함. None 반환
  - sorted 함수와 비교할 것
- .reverse()
  - 순서를 반대로 뒤집음(정렬하는건 아님)

## 딕셔너리(Dicrionary)

- 키-값 쌍으로 이뤄진 모음
  - 키
    - 불변 자료형만 가능
  - 값
    - 어떠한 형태든 관계없음
- 키와 값은 : 로 구분 됩니다. 개별 요소는 ,로 구분됩니다.
- 변경 가능하며, 반복가능함
  - 딕셔너리는 반복하면 키가 반환됩니다.



### 조회

- .get(key[,default])
  - key를 통해 value를 가져옴
  - KeyError가 발생하지 않으며, default 값으 설정할 수 있음(기본 : None)
- .pop(key[,default])
  - key가 딕셔너리에 있으면 제거히고 해당 값을 반환
  - 그렇지 않으면 default를 반환
  - default값이 없으면 KeyError
- .update([other])
  - 값을 제공하는 key, value로 덮어씁니다