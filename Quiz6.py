from math import *

def std_weight(height, gender) :
    if gender == 'M' :
        height = pow(height,2) * 22
    elif gender == 'W' :
        height = pow(height,2) * 21
    return round(height, 2)


height = 175
gender = 'M'
person = std_weight(height / 100, gender)

print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다." .format(height, person))
