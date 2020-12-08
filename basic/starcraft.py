from random import * 


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("f{0}:{1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("f{0}:{1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("f{self.name}:{location} 방향으로 적군을 공격 합니다. [공격력 : {self.damage}]")

    def damaged(self, damage):
        print("f{self.name}:{damage} 데미지를 입었습니다.")
        self.hp -= damage
        print("f{self.name}:{self.hp}입니다.")
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))
  
#마린 
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    #마린은 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소 
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

#탱크 
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False
    # 탱크는 시즈모드가 있으며, 더 높은 파워로 공격 가능, 이동은 불가 
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
    
        #현재 시즈모드가 아닐 때 
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환홥니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        #현재 시즈모드일 때 
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False
    
    
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다. [속도{2}]" \
            .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 ( 해제 상태 )
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True



def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("player: gg")
    print("플레이님이 게임에서 퇴장하셨습니다. ")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_unites = []
attack_unites.append(m1)
attack_unites.append(m2)
attack_unites.append(m3)
attack_unites.append(t1)
attack_unites.append(t2)
attack_unites.append(w1)

for unit in attack_unites:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

for unit in attack_unites:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Tank):
        unit.clocking()

for unit in attack_unites:
    unit.attack("1시")


for unit in attack_unites:
    unit.damaged(randint(5, 21))
