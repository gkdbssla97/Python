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

# normal Unit

from random import *

class Unit :
    def __init__(self, name, hp, speed) :
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성" .format(self.name))
    def move(self, location) :
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동. [속도{2}]"\
            .format(self.name, location, self.speed))
    def damaged(self, damage) :
        print("{0} : {1} 데미지를 입었습니다." .format\
            (self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다." .format(self.name,\
            self.hp))
        if self.hp <= 0 :
            print("{0} : 이 유닛은 파괴됐습니다" .format(self.name))
# Attack Unit
class AttackUnit(Unit) :
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed) # 부모클래스 속성
        self.damage = damage
    
    def attack(self, location) :
        print("{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}"\
            .format(self.name, location, self.damage))
# Marine
class Marine(AttackUnit) :
    def __init__(self) :
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    def stimpack(self) :
        if self.hp > 10 :
            self.hp -= 10
            print("{0} : 스팀팩을 사용. (Hp 10 감소)" .format(self.name))
        else :
            print("{0} : 스팀팩을 사용 X" .format(self.name))

# Tank
class Tank(AttackUnit) :
    seize_development = False

    def __init__(self) :
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self) :
        if Tank.seize_development == False:
            return
        if self.seize_mode == False :
            print("{0} : 시즈모드로 전환" .format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else :
            print("{0} : 시즈모드 해제" .format(self.name))
            self.damage /= 2
            self.seize_mode = False
    
# Aero Unit
class Flyable :
    def __init__(self, flying_speed) :
        self.flying_speed = flying_speed

    def fly(self, name, location) : 
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]" \
            .format(name, location, self.flying_speed))
 # Aero Attack Unit
class FlyableAttackUnit(AttackUnit, Flyable) : 
    def __init__(self, name, hp, damage, flying_speed) :
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location) :
        print("[공중유닛 이동]")
        self.fly(self.name, location)

# Wraith
class Wraith(FlyableAttackUnit) :
    def __init__(self) :
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self) :
        if self.clocked == True :
            print("{0} : 클로킹 모드 해제" .format(self.name))
            self.clocked = False
        else :
            self.clocked == False
            print("{0} : 클로킹 모드 작동" .format(self.name))
            self.clocked = True

def game_start() :
    print("[알림] 새로운 게임을 시작합니다.")

def game_over() :
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units= []

attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units :
    unit.move("11시")

Tank.seize_development = True
print("[알림] 시즈모드 개발 완료")

for unit in attack_units :
    if isinstance(unit, Marine) :
        unit.stimpack()
    elif isinstance(unit, Tank) :
        unit.set_seize_mode()
    elif isinstance(unit, Wraith) :
        unit.clocking()

for unit in attack_units :
    unit.move("11시")

for unit in attack_units :
    unit.damaged(randint(5, 21))

game_over()


# building
# class BuildingUnit(Unit) :
#     def __init__(self, name, hp, location) :
#         # Unit.__init__(self,name, hp, 0)
#         super().__init__(name, hp, 0)
#         self.location = location

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("벌처", 80, 10, 20)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

# firebat1 = AttackUnit("firebat", 50, 16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)

# marine1 = Unit("Marine", 40) # 객체1
# marine2 = Unit("Marine", 40) # 객체2
# tank = Unit("Tank", 150) # 객체3

# Wraith = Unit("Wraith", 80)
# print("Unit name : {0}" .format(Wraith.name))

# # 클래스 외부에서 내가 원하는 변수를 확장할 수 도 있고
# # 그 확장한 변수는 그 확장된 객체에만 적용되고 
# # 기존 객체에는 적용되지 않음
# Wraith2 = FlyableAttackUnit("MC Wraith", 80, 10, 9)
# Wraith2.clocking = True

# if Wraith2.clocking == True :
#     print("{0}는 현재 클로킹 상태." .format(Wraith2.name))

