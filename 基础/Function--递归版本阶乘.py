def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("请输入一个正整数："))
result = factorial(number)
print("%d的阶乘是：%d" %(number, result))
