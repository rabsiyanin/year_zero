print ("Введите число")
a = int(input())
def my_div(a):
    div = 0
    for i in range (2, a):
        if a % i == 0:
            div = i
    if div == 0:
        return(a)
    else:
        return(div)
print("Наибольший делитель этого числа равен", my_div(a))