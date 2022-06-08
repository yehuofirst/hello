from asyncio import all_tasks
from ctypes.wintypes import HPALETTE
from re import L


class Player():
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        self.__hp = value
    def attack(self, other):
        print("玩家攻击敌人")
        other.damage(self.atk)  
    def damage(self, value):
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()
    def __death(self):
        print("玩家死咯")
        print("游戏结束")
        
class Enemy():
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,value):
        self.__hp = value

    def attack(self, other):
        print("敌人攻击玩家")
        other.damage(self.atk)
    def damage(self, value):
        print("敌人受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()
    def __death(self):
        print("敌人死咯")


p01 = Player(1000,100)
e01 = Enemy(200,10)

p01.attack(e01)
e01.attack(p01)
p01.attack(e01)