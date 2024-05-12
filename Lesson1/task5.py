list_num = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def list_work(some_list):
    print(min(some_list))
    some_list = set(some_list)
    some_list = [x for x in some_list]
    print(some_list)
    for i in range(len(some_list)):
        if i % 4 == 0 and i != 0:
            some_list[i-1] = 'X'
    print(some_list)


def square_stars (n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1:
                print('*', end='')
            elif j == 0 or j == n-1:
                print('*', end='')
            else:
                print(' ', end='')
        print()


def multi_table():
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            print(i*j, end='  ')
            j += 1
        i += 1
        print()


while True:
    print("Виберіть потрібну дію:")
    print('''1. Операції зі списком
    2. Вивести квадрат із заданою стороною
    3. Вивести табличку множення
    4. Exit''')

    choose = int(input('Enter a number of operation'))
    match choose:
        case 1:
            list_work(list_num)
        case 2:
            square_stars(10)
        case 3:
            multi_table()
        case 4:
            break

