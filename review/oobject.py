'''
class CocaCola:
    # 类变量 类属性
    formula = ['caffeine','sugar','water','soda']

coke_for_China = CocaCola()

# 外部新增实例变量  只是增加该对象的实例属性  新对象没有local_logo
coke_for_China.local_logo = '可口可乐'
print(coke_for_China.local_logo)
'''

'''
class CocaCola:
    # 类变量 类属性
    formula = ['caffeine','sugar','water','soda']

    def __init__(self,name):
        # 内部新增实例变量  增加所有对象的实例属性
        self.local_logo = name
        
coke_for_China = CocaCola('可口可乐')

print(coke_for_China.local_logo)
'''

'''
class CocaCola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffeine = 34
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine'
    ]


    def __init__(self, logo_name):
        self.local_logo = logo_name


    def drink(self):
        print('You got {} cal energy!'.format(self.calories))


class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients = [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color'
    ]

coke_a = CaffeineFree('Cocacola-FREE')
coke_a.drink()
'''
# 类修改类变量是全局的，对象修改类变量是局部的
# class TestA:
#     attr = 1
#     def __init__(self):
#         self.attr = 66
#
# obj1 = TestA()
# obj2 = TestA()
#
# print(TestA.__dict__)
# print(obj2.__dict__)
class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()
obj_a.attr = 42
print(obj_b.attr)