# for 문
print("번호: 1")
print("번호: 2")
print("번호: 3")
print("번호: 4")

for waiting_no in range(1, 6 ) :
    print("대기번호 : {0}" .format(waiting_no))

starbucks = ['A', 'B', 'C', 'D']
for customer in starbucks :
    print("{0}, 커피 나왔습니다." .format(customer))

# while 문
customer = 'A'
idx = 5
while idx >= 1:
    print("{0}, 커피 나왔습니다. {1} 번 남았어요."
    .format(customer, idx))
    idx -= 1
    if idx == 0:
        print("커피는 폐기처분됩니다")

customer = 'B'
person = "Unknown"
idx = 1
'''while person != customer :
    print("{0}, 커피 나왔습니다. 호출 {1}회" .format(customer, idx))
    person = input("what's your name?")'''

absent = [2, 5] # 결석
no_book = [7] 
for student in range(1, 11) :
    if student in absent:
        continue
    elif student in no_book :
        print("{0}, Come in office" . format(student))
        break
    print("{0}, Read a book please" .format(student))

# for 문 한 줄
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)