print("Введите число:")
a=int(input())
print("Введите степень:")
n=int(input())
def my_power(a, n):
    if (n == 0):
        return 1
    return a*my_power(a, n-1)
print("Число в данной степени равно ",my_power(a,n)) 