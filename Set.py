# 집합 (set)
# 중복 안 됨, 순서 없음
my_set = {1,2,3,4,4}
print(my_set)

java = {'A','B','C'}
python = set({'A','D'})

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람 늘어남
python.add('B')
print(python)

# java를 까먹음 
java.remove('B')
print(java)