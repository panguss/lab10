while True:
    try:
        n = int(input("Введите натуральное число "))
        if n < 0:
            print('Число должно быть натуральным')
        else:
            break
    except(ValueError):
        print("Необходимо ввести натуральное число")

m = [1, 2, 4, 8, 16, 32, 64]
x = sum(m) + 1
v = []
while 1 <= (x := (x // 2)):
    a, n = divmod(n, x)
    if a > 0:
        v += [x] * a

print(*v)
