# 1. 导入模块
# import utils.my_func
#
# utils.my_func.log_separator1()
# utils.my_func.log_separator2()

# from utils import my_func
#
# my_func.log_separator1()
# my_func.log_separator2()
# my_func.log_separator3()

# 注意: 如果要通过 from utils import * 导入包下的所有模块, 需要 __init__.py 文件中添加 __all__=[]
# from utils import *
#
# my_func.log_separator1()
# my_func.log_separator4()
#
# print(my_var.PI)
# print(my_var.NAME)

# 2. 导入模块中的功能
from utils.my_func import log_separator1, log_separator3

log_separator1()
log_separator3()
