
float_num = 3.14 # 定义一个浮点数变量并赋值为3.14
print("浮点数的值为：", float_num) # 输出浮点数的值
type(float_num) # 获取浮点数的类型,此时并没有输出类型信息，只是获取了类型信息
print("浮点数的类型为：", type(float_num)) # 输出显示出浮点数的类型

int_num = int(float_num) # 将浮点数转换为整数，结果为3
print("将浮点数转换为整数后的值为：", int_num) # 输出转换后的整数值
type(int_num) # 获取整数的类型,此时并没有输出类型信息，只是获取了类型信息
print("整数的类型为：", type(int_num)) # 输出显示出整数的类型

"""
int_num = int("11.1") # 尝试将字符串"11.1"转换为整数，这会引发ValueError异常
print("将字符串'11.1'转换为整数后的值为：", int_num) # 这行代码不会被执行，因为前一行会引发异常
"""