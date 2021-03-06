# -*- coding: utf-8 -*-
'''
@File    :   name_function.py    
@Contact :   18898513573
@Author  :   DrewB 
@Time    :   2020/3/13 20:35 
'''
def get_formatted_name(first, last, middle = ''):
    '''生成整洁的姓名'''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last

    return full_name.title()


