

def damage(skill1,skill2):
    damage1 = skill1 *3
    damage2 = skill2 *2 + 10
    return damage1,damage2  #元组


# 序列解包
# damages[0],damages[1] 用序列下标不好，要用有意义的名字解包
# damages = damage(3,6)
# print(damages[0],damages[1])
# print(type(damages))  

# 推荐
skill1_damage,skill2_damage = damage(3,6)
print(skill1_damage,skill2_damage)