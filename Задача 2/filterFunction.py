def kill_some_string(aString, _):#Требуется два аргумента, но лямбда-функция является анонимной функцией?
    return list(filter(lambda x: ' ' not in x and len(x) >= 5 and x[0] != 'a', 
                aString))
"""
filter函数用来过滤，语法filter(fuction, iterable)
Функция filter используется для фильтрации, filter(fuction, iterable)
lambda函数是匿名函数，是一种简洁地创建小型函数的方法
Лямбда-функции являются анонимными функциями и представляют собой краткий способ создания небольших функций.
"""

#Проверить эффект фильтрации 检测过滤效果
strings = ["apple", "Software Engineering", "library", "data"]
filtered_strings = kill_some_string(strings, None)
print(filtered_strings)
