'''Quiz) 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받습니다.
    
   rule1) 20명이 지원하였고 id는 1 ~ 20이라고 가정
   rule2) 무작위로 추첨하되 중복 불가
   rule3) random module, shuffle, sample 활용'''

# 출력예제
# -- 당첨자 발표 -- 
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 -- 

from random import *
id = range(1,21) # 1 ~ 20까지의 범위 설정
#print(id, type(id))
id = list(id)
shuffle(id)

winner = sample(id, 4)
print("치킨 당첨자 : {0}" .format(winner[0]))
print("커피 당첨자 : {}" .format(winner[1:]))