# - X 주차 주간 보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건: 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만듭니다.

import pickle

for i in range(1,6) :
    num = i
    with open("{0}주차.txt" .format(num), "w", encoding="utf8") as Work_file :
        Work_file.write(" - {0} 주차 주간 보고 -\n부서 :\n이름 : \n업무요약 :\n" .format(num))

                      
    
                    