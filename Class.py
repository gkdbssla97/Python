# name = "Marine"
# hp = 40
# damage = 5

# print("Create Unit \'{}\'" .format(name))
# print("hp {0} damage {1}\n" .format(hp, damage))

# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("Create Unit \'{}\'" .format(name))
# print("hp {0} damage {1}\n" .format(hp, damage))

# def attack(name, location, damage) :
#     print("{0} : {1} 방향으로 적군 공격. [공격력] {2}" .format(
#     name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

class Unit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성됨." .format(self.name))
        print("체력 {0}, 공격력 {1}" . format(self.hp, self.damage))

class AttackUnit :
    def __init__(self, name, hp, damage) :
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}"\
            .format(self.name, location, self.damage))

    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다." .format\
            (self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name,\
            self.hp))
        if self.hp <= 0 :
            print("{0} : 이 유닛은 파괴됐습니다" .format(self.name))

firebat1 = AttackUnit("firebat", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

marine1 = Unit("Marine", 40, 5) # 객체1
marine2 = Unit("Marine", 40, 5) # 객체2
tank = Unit("Tank", 150, 35) # 객체3

Wraith = Unit("Wraith", 80, 5)
print("Unit name : {0}, damage : {1}" .format(Wraith.name, Wraith.damage))

# 클래스 외부에서 내가 원하는 변수를 확장할 수 도 있고
# 그 확장한 변수는 그 확장된 객체에만 적용되고 
# 기존 객체에는 적용되지 않음
wraith2 =Unit("MC Wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True :
    print("{0}는 현재 클로킹 상태." .format(wraith2.name))

