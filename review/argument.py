def trapezoid_area(base_up, base_down, height):
    return 1/2 * (base_up + base_down) * height


# 位置参数
print(trapezoid_area(1, 2, 3))
# 关键词参数
print(trapezoid_area(base_up=1, base_down=2, height=3))

# right
trapezoid_area(height=3,base_down=2,base_up=1)
trapezoid_area(1,2,height=3)

# wrong Positional argument after keyword argument
# 位置参数不能在关键词参数后面
# trapezoid_area(height=3,base_down=2,1)
# trapezoid_area(base_up=1,base_down=2,3)
