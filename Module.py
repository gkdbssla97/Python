# 부품처럼 만들어진 파일 
# 타이어만 교체, 범퍼만 교체처럼 S/W도 부품만 교체하면 됨

import theater_module
theater_module.price(3) 
theater_module.price_morning(5)
theater_module.price_soldier(4)

print("--------")

import theater_module as mv # 모듈의 별명을 mv로 설정
mv.price_soldier(4)

from theater_module import * 
price(4)
