'''Quiz)   
   1. 랜덤으로 날짜를 뽑는다.
   2. 월별 날짜는 다름을 감안하여 최수 일수는 28일 이내
   3. 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외'''

from random import *
#print(randint(4,28))
date = randint(4,28)

print("Study semiar is adapted on date",date)