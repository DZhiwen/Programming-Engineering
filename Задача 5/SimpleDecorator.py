import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        #выводит в консоль время выполнения декорируемой функции
        start_time = time.time()  # 获取当前时间（秒）Получить текущее время (секунды)
        result = func(*args, **kwargs)  # 调用函数Вызов функции
        end_time = time.time()  # 获取当前时间（秒）Получить текущее время (секунды)
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds\n")
        return result
    return wrapper

# 测试装饰器的第一个函数：计算两个数字的和Функция вычисляет сумму двух чисел a и b, выводит результат в консоль
@time_decorator
def calculate_sum(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

'''
测试装饰器的第二个函数：从文件读取数字，计算和，写入另一个文件
Функция читает из файла input.txt значение двух чисел a и b, записывает результат вычисления в файл output.txt 
'''

@time_decorator
def read_and_write_sum(file_in, file_out):
    with open(file_in, 'r') as f_in:
        numbers = list(map(int, f_in.read().strip().split()))  # 读取文件中的数字Чтение чисел из файла
    if len(numbers) < 2:
        print("The file must contain two numbers")
        return
    a, b = numbers
    with open(file_out, 'w') as f_out:
        f_out.write(str(a + b))  # 计算和并写入文件
    print(f"The sum of {a} and {b} has been written to {file_out}.")


# 调用函数Например:
calculate_sum(523, 175)
read_and_write_sum('input.txt', 'output.txt')
