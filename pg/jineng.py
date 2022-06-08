"""
封装：将每种影响效果单独做成类
继承：将各种影响效果抽象为shillimpacteffect,
      隔离技能是夫妻与各种效果的变化

多态：各种影响效果再重写shillimpacteffect类中impact中
      释放器调用shillimpacteffect执行各种效果

六大原则：
开闭：增加新（技能/影响效果），不修改释放器代码
单一职责：shillimpacteffect负责 隔离变化
"""

class SkillImpacteffect():
    #技能影响效果
    def inmact(self):
        raise NotImplementedError()

class DamageEffect(SkillImpacteffect):
    def __init__(self,value):
        self.value =value
    def impact(self):
        print("扣你%d血"% self.value)

class LowerDeffenseEffect(SkillImpacteffect):
    def __init__(self,value,time):
        self.value =value
        self.time = time
    def impact(self):
        print("降低%d防御力,眩晕持续%d秒"% (self.value,self.time))
class DizzinessEffect(SkillImpacteffect):
    def __init__(self,time):
        self.time = time
    def impact(self):
        print("眩晕持续%d秒"% self.time)

class SkillDeppoyer:
    #技能释放器
    #加载配置文件{技能名称1:[1,2,3],技能名称2:[1,2,3]....}
    #创建效果对象
    #生成技能（执行效果）
    def __init__(self,name):
        self.name = name
        #加载配置文件
        self.__dict_skill_config = self.__load_config_file()
        #创建效果对象
        self.__effect_objects = self.__create_effect_objects()

        self.name = name
    def __load_config_file(self):
        return {
        "降龙十八掌":["DamageEffect(100)","LowerDeffenseEffect(-10,5)","DizzinessEffect(6)"],
        "六脉神剑":["DamageEffect(200)","LowerDeffenseEffect(-20,5)","DizzinessEffect(5)"]
        }
    def __create_effect_objects(self):
        #根据name创建相应的技能对象
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    #生成技能（执行效果）
    def generate_skill(self):
        for item in self.__effect_objects:
            item.impact()


xlsbz = SkillDeppoyer("降龙十八掌")
xlsbz.generate_skill()


lmsj = SkillDeppoyer("六脉神剑")
lmsj.generate_skill()