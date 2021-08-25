import pickle

# 따로 close()를 사용할 필요 없음
with open("profile.pickle", "rb") as profile_file :
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf8") as study_file :
    study_file.write("Studying Python")

with open("study.txt", "r", encoding="utf8") as study_file :
    print(study_file.read())