weather = input("How's the weather? ")
if weather == "Rain" or weather == "Snow":
    print("Take an umbrella")
elif weather == "Dust" : # not else if
    print("Take a mask")
else :
    print("No way") 


temp = int(input("How's the temprature? "))
if temp >= 30: 
    print("So hot\n")
elif temp >= 10 & temp < 30:
    print("So good")
    print("??")
else :
    print("COLD")