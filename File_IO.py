# File Write

score_file = open("score.txt", "w", encoding="utf8")
print("Math: 0", file=score_file)
print("Eng: 50", file=score_file)
score_file.close()


score_file = open("score.txt", "a", encoding="utf8")
score_file.write("Sci : 80")
score_file.write("\nCoding : 100")
score_file.close()

# File Read

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 한 줄 읽기 커서는 다음 줄로 이동
print(score_file.readline()) # 한 줄 읽기 커서는 다음 줄로 이동
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True :
    line = score_file.readline()
    if not line :
        break
    print(line, end="") # 별도의 줄 바꿈 필요없음
score_file.close()

print("\n")

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines :
    print(line, end="")
score_file.close()
