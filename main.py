def show_field(f):
    print("  0 1 2")
    for i in range(len(f)):
        print(str(i)+' '+' '.join(f[i]))


def users_input(f):
    while True:
        place = input("Введите координаты :").split()
        if len(place) != 2:
            print("Введите две координаты")
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Введите числа")
            continue
        x,y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print("Вышли из диапозона координат")
            continue
        if f[x][y] != "-":
            print("Клетка занята")
            continue
        break
    return x, y


def win(f, user):
    f_list = []
    for l in f:
        f_list += l
    positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    indecex = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indecex.intersection(set(p))) == 3:
            return True
    return False


field = [["-"]*3 for _ in range(3)]
count = 0
while True:
    if count % 2 == 0:
        user = "x"
    else:
        user = "o"
    show_field(field)
    if count < 9:
        x, y = users_input(field)
        field[x][y] = user
    if count == 9:
        print("Ничья")
    if win(field, user):
        print(f"Выиграл {user}")
        show_field(field)
        break
    count += 1









