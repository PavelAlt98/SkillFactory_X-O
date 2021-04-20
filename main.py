field = [['-']*3 for _ in range(3)]


def show_map(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))


def step_user(f):
    while True:
        coordinate = input('Введите координату:').split()
        if len(coordinate) != 2:
            print('Введите 2 координаты!')
            continue
        if coordinate[0].isdigit() and coordinate[1].isdigit() == False:
            print('Введите числа!')
            continue
        if not(0 <= int(coordinate[0]) < 3 and 0 <= int(coordinate[1]) < 3):
            print('Координаты вне диапазона!')
            continue
        if f[int(coordinate[0])][int(coordinate[1])] != '-':
            print('Клетка занята!')
            continue
        break
    return int(coordinate[0]), int(coordinate[1])


def win(f, user):
    def win_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for j in range(3):
        if win_line(f[j][0], f[j][1], f[j][2], user) or \
            win_line(f[0][j], f[1][j], f[2][j], user) or \
            win_line(f[0][0], f[1][1], f[2][2], user) or \
                win_line(f[0][2], f[1][1], f[2][0], user):
            return True
    return False


count = 0
while True:
    if count % 2 == 0:
        user = 'x'
    else:
        user = 'o'

    show_map(field)
    x, y = step_user(field)
    field[x][y] = user
    if count == 9:
        print('Ничья')
        show_map(field)
    if win(field, user):
        show_map(field)
        print(f"Выиграл {user} !")
        break
    count += 1
