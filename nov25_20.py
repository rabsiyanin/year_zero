#задание 1

A = int(input('Число A:'))
B = int(input('Число B:'))
if A < B:
    for i in range(A, B + 1):
        print(i)
if A > B:
    for i in range(A, B-1,-1):
        print(i)
if A == B:
    print(B)     

#задание 2
A = int(input('Число А:'))
B = int(input('Число B >> '))
for i in range(A, B + 1):
    if (i // 1000) == i % 10 and (i // 100) % 10 == (i // 10) % 10:
        print(i)  

# Проверка на целочисленность
A = int(input('Число A:'))
A = str(A)

A_reverse = A[::-1]
if A_reverse == A:
  print('Число ' + A + ' - палиндром')
else:
  print('Число ' + A + ' не палиндром')
