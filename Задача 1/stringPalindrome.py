def is_palindrome(a):
    # 检查字符串是否与其反转相同Используйте операцию срезы, чтобы определить, является ли это палиндромом.
    return a == a[::-1]

user_input = input("Введите строку и проверьте, является ли она палиндромом：")

if is_palindrome(user_input):
    print(f"'{user_input}' is palindrome")
else:
    print(f"'{user_input}' is not palindrome")
