
class Shoulei:
    def __init__(self,atk):
        self.atk = atk
    def baozha(self,damage_target):
        print("爆炸")
        damage_target.damage(self.atk)

class Damager:

    def damage(self,value):
        print("父类受伤")

class Player(Damager):
    def __init__(self,hp):
        self.hp = hp
    def damage(self, value):
        self.hp -= value
        print("玩家受伤")

class Enemy(Damager):
    def __init__(self,hp):
        self.hp = hp
    def damage(self, value):
        self.hp -= value
        print("敌人受伤")

g01 = Shoulei(100)

e01 = Enemy(200)
p01 = Player(300)

g01.baozha(e01)
g01.baozha(p01)