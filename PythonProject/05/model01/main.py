# 导入自定义模块
import func

# 使用模块中的功能
print(func.PI)
print(func.NAME)

func.log_separator1()
func.log_separator3()

from func import PI, NAME, log_separator1, log_separator3

# 使用模块中的功能
print(PI)
print(NAME)

log_separator1()
log_separator3()
