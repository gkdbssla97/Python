try :
    print("Devide Calculator")
    nums = []
    nums.append(int(input("first num: ")))
    nums.append(int(input("second num: ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}" .format(nums[0],nums[1], nums[2]))
except ValueError :
    print("Error! fault num.")
except ZeroDivisionError as err :
    print(err)
except Exception as err :
    print("알 수 없는 에러가 발생")
    print(err)