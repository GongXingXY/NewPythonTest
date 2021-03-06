# -*- coding: utf-8 -*-
'''
@File    :   string.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2019/12/11 10:28 
'''
# 字符串 String

s1 = 'hello world'
s2 = "hello, world!"
# '''以三个双引号或单引号开头的字符串可以折行
s3 = '''
hello,
world,
'''
print(s1, s2, s3, end=' ')
# 可以在字符串中使用\（反斜杠）来表示转义，
# 也就是说\后面的字符不再是它原来的意义，
# 例如：\n不是代表反斜杠和字符n，
# 而是表示换行；而\t也不是代表反斜杠和字符t，
# 而是表示制表符。所以如果想在字符串中表示'要写成\'，
# 同理想表示\要写成\\。可以运行下面的代码看看会输出什么。
s1 = '\'hello,world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')
# 在\后面还可以跟一个八进制或者十六进制数来表示字符，
# 例如\141和\x61都代表小写字母a，
# 前者是八进制的表示法，后者是十六进制的表示法。
# 也可以在\后面跟Unicode字符编码来表示字符，
# 例如\u9a86\u660a代表的是中文“骆昊”。运行下面的代码，看看输出了什么。

s1 = '\141\142\143\x61\x62\x63'

print(s1)
# 如果不希望字符串中的\表示转义，
# 我们可以通过在字符串的最前面加上字母r来加以说明，
# 再看看下面的代码又会输出什么。

s1 = r'\'hello,world!\''
s2 = r'\n\\hello,world!\\\n'
print(s1, s2, end='')

# Python为字符串类型提供了非常丰富的运算符，
# 我们可以使用+运算符来实现字符串的拼接，
# 可以使用*运算符来重复一个字符串的内容，
# 可以使用in和not in来判断一个字符串是否包含另外一个字符串（成员运算），
# 我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符（切片运算），
# 代码如下所示。

s1 = 'hello' * 3
print(s1)  # hellohellohello
s2 = 'world'
s1 += s2
print(s1) #hellohellohelloworld
print('ll' in s1) #True
print('goold' in s1) #False
print('good' not in s1) #True

str2 = 'abc123456'

# 从字符串中取出指定位置的字符（下标运算）
print(str2[2]) #c
# 从字符串切片（从指定的开始索引到指定的结束索引
print(str2[2:5]) #c12
print(str2[2:]) #c123456
print(str2[2::2])#c246
print(str2[::2]) #ac246
print(str2[::-1]) # 654321cba  反向
print(str2[-3:-1]) # 45

# 在Python中，我们还可以用一些方法来对字符串进行处理
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))
# 获得字符串首字母大写的拷贝
print(str1.capitalize())
# 获得每个单词首字母大写的拷贝
print(str1.title())
# 获得字符串变大写后的拷贝
print(str1.upper())
# 获得字符串变小写后的拷贝
print(str1.lower())
# 从字符串中查找子串所在的位置
print(str1.find('or'))
print(str1.find('shit'))
# 与find类似，但是呢它找不到子串时会引发异常
print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))

#将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
#将字符串以指定的试试靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))

str2 = 'abc123456'
#检查字符串是否由数字构成
print(str2.isdigit())
# 检查字符串是否由字母构成
print(str2.isalpha())
# 检查字符串是否由数字和字母构成
print(str2.isalnum())

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

# 删除空白
favorite_language = ' python '
favorite_language.rstrip() # 删除末尾空白
favorite_language.lstrip() # 删除开头空白
favorite_language.strip() # 删除两端空白


#　格式化输出字符串 3种方法

a, b = 5, 10
print('%d * %d = %d' % (a,b, a*b))
print('{0} * {1} = {2}'.format(a, b, a * b))  # 方法来
print(f'{a} * {b} = {a * b}')  # 3.6之后的语法糖  多用这个吧


