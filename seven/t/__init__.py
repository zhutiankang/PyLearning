# __init__.py 两个下划线，python通过这个来做文件夹与包的区分

# seven.__init__

# __init__模块的名字就是包名就是seven 不是seven.__init__

# 导入包的时候，__init__里面的代码会自动被执行

# 1. 导入包，模块，变量的时候，代码会自动被执行
# 2. __all__ = ['c5'] 过滤
# 3. 批量导入包

__all__ = ['c5']

# NameError: name 'c6' is not defined

import sys
import io
import datetime