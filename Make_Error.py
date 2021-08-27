class BigNumberError(Exception) :
    def __init__(self, msg) :
        self.msg = msg
    
    def __str__(self) :
        return self.msg
try :
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("first num : "))
    num2 = int(input("second num : "))
    if num1 >= 10 or num2 >= 10 :
        raise BigNumberError("입력값 : {0}, {1}" \
            .format(num1, num2)) # except BigNumberError로 이동
    print("{0} / {1} = {2}" .format(num1, num2, int(num1 / num2)))

except ValueError :
    print("잘못된 값을 입력. 한 자리 숫자만 입력.")
except BigNumberError as err:
    print("Error! please insert just one number.")
    print(err)
# finally : 
finally :
    print("Thx for using our Cal.")