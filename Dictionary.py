cabinet = {3: "HA", 100: "CHOI"}

print(cabinet[3],cabinet[100])
print(cabinet.get(3))
print(cabinet.get(5)) # None

cabinet = {"A-3":'X', "B-100":'Y'}
print(cabinet.get("A-3"))
cabinet["A-3"] = 'Z'
print(cabinet.get("A-3"))

# 삭제
del cabinet["A-3"]
print(cabinet)
print(cabinet.items())
print(cabinet.keys())
print(cabinet.values())

# 모두 삭제
cabinet.clear()
print(cabinet)