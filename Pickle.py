import pickle

profile_file = open("profile.pickle", "wb")
profile = {"Name": "A", "Age": 30, "Hobby": ["C","CC","CCC"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 File에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # File에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 