# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 31일 1,3,5,7,8,10,12 30일 4,6,9,11

T = int(input())

for i in range(1, T + 1):
    ymd = (input())
    year = int(ymd[:4])
    month = int(ymd[4:6])
    day = int((ymd[6:]))
    if month <1 or month>12:
        print(f'#{i} -1')
        continue
    
    if month in [1,3,5,7,8,10,12]:
        if 1 > day or day > 32:
            print(f'#{i} -1')
            continue
    if month == 2:
        if 1 > day or day > 29:
            print(f'#{i} -1')
            continue
    if month in [4,6,9,11]:
        if 1 > day or day > 31:
            print(f'#{i} -1')
            continue

    
    print("#%d %04d/%02d/%02d" %(i,year,month,day))