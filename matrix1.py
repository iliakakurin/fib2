import random

# Создать матрицу вручную
a = [
     [1,0,5],
     [5,6,1],
     [8,1,3],
     [1,3,4]
     ]

print(a)

print(a[3][2])

# Вывести матрицу на экран построчно
for x in a:
    print(x)
    
# Пробежать по всем элементам матрицы
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(a[i][j])
        
        
        
n = 10
m = 10

# Создать пустую матрицу m*n
b = [ [0]*n ] *m

for x in b:
    print(x)

# Заполнить матрицу случайными значениями
for i in range(m):
    b[i] = random.sample(range(10,100),n)


print(b)
for x in b:
    print(x)
        