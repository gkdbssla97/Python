sentence = "Hi guys"
sentence1 = "Hi guys"

print(sentence)
print(sentence1)

admin_num = "900291-4958121"
print(admin_num)
print("sex:",admin_num[7])
print("year:",admin_num[0:2]) # idx: 0 ~ 1
print("month:",admin_num[2:4]) # idx: 2 ~ 3

print("birth:",admin_num[0:6])
print(admin_num[7:]) # idx: 7 ~
print(admin_num[-7:]) # 맨 뒤에서 7번째부터 끝까지

# 문자열 처리
python = "Python is Amazing"
print(python.lower()) # small letter
print(python.upper()) # capital letter
print(len(python)) # length
print(python.replace("Python", "JAVA"))

idx = python.index('n')
print(idx)
idx = python.index('n',idx + 1) # find second 'n'
print(idx)

print(python.find("JAVA")) # -1 is none 
print(python.index("Python"))
print(python.count('n')) # How many 'n's are there in a sentence


print("나는 %d살 입니다" % 20)
print("나는 %s을 좋아해요" % "Python")
print("Apple은 %c로 시작합니다" % 'A')