# 3.数值类型

# 3.1int整型(常用):任意大小的整数
num = 10000
# 检测数据类型的方法type(
print (type (num))

# 3.2float浮点型:小数
num2= 1.5
print (type (num2))

# 3.3bool布尔型(重点)
# 有固定写法，一个为True(真)，一个为False(假)
# 注意:True和False必须严格区分大小写
# print(type(true)) 报错
# 布尔值可以当作整型对待，True相当于整数1，False相当于整数0
print (True + False) #1+0=1
print (True + 1) #1+1=2

# 3.4complex复数型(了解)
# 固定写法:z=a+bj   a是实部，b是虚部，j是虚数单位
print (type (2+3j))
# ma = 1+2i
# print (ma) 报错，j是固定的叙述单位，不能随意改变
ma=1 +2j
ma2=2+3j
print (ma+ma2) # (1+2)+(2j+3j)

#4.字符串str
#特点:需要加上引号，单引号和双引号都可以，包含了多行内容的时候也可以使用三引号
#name = sixstar #报错，没有引号识别成变量名，sixstar没有被赋值
name = "sixstar"
print (name)
name2 = 'sixstar'
print (name2)
name3 = '''sixstar'''
print (name3)
name4 = """


sixstar"""
print (name4)
# 此处的name4输出结果是一个空行加上sixstar，因为三引号内的内容包含了换行符和三引号注释符存在区别
"""name5 = 666""" # 此处的name5没有被定义出，三引号起到多行注释效果
# print (name5)
