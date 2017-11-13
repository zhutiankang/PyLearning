# 默认public
# private 在变量与方法面前加双下划线 __   封装性好，通过方法更改或者获取变量   不要在后面在加双下划线，只有init有，不然仍然不是私有的
# 其实python没事私有变量概念，只是通过改变名字的方式key的，不能直接访问到，点到，可以通过dict查看

# student.__score = -1  通过点  新添加了一个实例变量 与类里面的私有变量不是一个 可以通过dict列表查看
# print(student.__score) 所以不会报错

# 如果没有赋值，而是直接调用print(student.__score) 私有变量，这会报错