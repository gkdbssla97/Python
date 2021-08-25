import sys

print("Python","JAVA",'C', sep = " vs ", end = ' ?\n')
print("Python","Java", file=sys.stdout)
print("Python","Java", file=sys.stderr)

# 시험성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items() :
    print(subject, str(score).rjust(4), sep = ":") # 오른쪽 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1,21) : # 1 ~ 20
    print("대기번호 :" + str(num).zfill(2))


#answer = input("아무 값이나 입력하세요 : ")
#print("입력한 값은",answer+"입니다.")

# 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간확보
print("{0: >10}". format(500))

# 양수일 땐 + 로 표시, 음수일 땐 - 로 표시 
print("{0: >+10}" . format(+500))
print("{0: >+10}" . format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:ㅁ<+10}" .format(500))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}" .format(1000000000000))
print("{0:+,}" .format(-1000000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보
# 빈 자리는 ^로 채워주기 
print("{0:^<+30,}" .format(1000000000000000))

# 소수점 출력
print("{0:.3f}" . format(5/3))