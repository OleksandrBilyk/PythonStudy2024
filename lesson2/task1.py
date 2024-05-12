

def notebook():
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todo_list
        return todo_list.copy()

    return add_todo, get_all


add_nb1, get_all_nb1 = notebook()

add_nb1('ddddddd')
add_nb1('ffhhh')

print(get_all_nb1())


def expanded_form(num: int) -> str:
    st = str(num)
    length = len(st) - 1
    res = []

    for i, ch in enumerate(st):
        if ch != '0':
            res.append(ch+'0'*(length-i))
    return ' + '.join(res)


def count_decor(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        func(*args, **kwargs)
        print(f'{count=}')

    return inner


@count_decor
def func1():
    print('func1')


@count_decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
func1()
func2()
