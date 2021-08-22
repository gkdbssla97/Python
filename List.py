# List []

# 지하철 칸 별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ['A', 'B', 'C']
print(subway)

# B는 몇 번째 칸에 타고 있는가 ?
print(subway.index('B'))

# D가 다음 정류장에서 다음 칸에 탐
subway.append('D')
print(subway)

# X가 A와 B 사이에 탐
subway.insert(1, 'X')
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 ?
subway.append('A')
print(subway)
print(subway.count('A'))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort() # 오름차순
print(num_list)

# 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
num_list = [5,2,4,3,1]
mix_list = [20, 'A', True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)