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

# 默认参数
def trapezoid_area2(base_up, base_down, height=3):
    return 1/2 * (base_up + base_down) * height

print(trapezoid_area2(1,2))
print(trapezoid_area2(1,2,height=15))

print('  *',' ** ',' ***',' | ',sep='\n')

# 实际使用场景 很常用

# 这个是在请求网站时header,可甜可不填
# requests.get(url,headers=header)

# 给图片加水印的时候默认的水印质量是100
# img.save(img_new,img_format,quality=100)