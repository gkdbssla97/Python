from random import *

idx = 1
cnt = 0
for i in range(1, 51) :
    customer = randint(5,50)
    if customer >= 5 and customer <= 15 :
        print("[O] {0}번째 손님 (소요시간 : {1}분" .format(i, customer))
        cnt += 1
    else :
        print("[ ] {0}번째 손님 (소요시간 : {1}분" .format(i, customer))
    idx += 1

print("총 탑승 승객 : {0} 분" .format(cnt))
