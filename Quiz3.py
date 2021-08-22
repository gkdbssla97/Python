'''Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
rule1) : http:// 부분은 제외 => naver.com
rule2) : 처음 만나는 점(.) 이후 부분은 제외 => naver
rule3) : 남은 글자 중 처음 세자리 (nav) + 글자 갯수 (5) +
         글자 내 'e' 갯수 (1) + '!'(!)로 구성 '''
# 생성된 비밀번호 : nav51!
         
domain_url = "http://youtube.com"
my_str = domain_url.replace("http://","") # rule1
print(my_str)

my_str = my_str[:my_str.index('.')] # rule2
print(my_str)
r1 = my_str[:3]
r2 = len(my_str)
r3 = my_str.count('e')
r4 = '!'
print("{0}의 패스워드는 {1}입니다." .format(domain_url, r1+str(r2)+str(r3)+r4))

