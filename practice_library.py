# 절댓값
print(abs(-5) + 1)
# 제곱
print(pow(4,3))
# 최댓값
print(max(5,16)), print(min(5,16))
# 반올림
print(round(4.41)), print(round(4.62))

from math import * # math Library

print(floor(4.42)) # 내림
print(ceil(4.42)) # 올림
print(sqrt(4)) # 제곱근

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random()*10)) # 정수 출력
print(int(random()*10) + 1) # 정수 출력 1 ~ 11 난수 값

print(randrange(1, 45)) # 1~ 45 미만의 난수 값 생성
print(randint(1, 45)) # 1~ 45 이하의 난수 값 생성