st = input("Enter a some string")
number_of_st = []
number = ''
if len(st) != 0:
    for char in st:
        if char.isnumeric():
            number += char
        elif number:
            number_of_st.append(number)
            number = ''
    if number:
        number_of_st.append(number)
    print(*number_of_st, sep=',') if number_of_st else print('No numbers in string')
else:
    print("Enter above 0 chars")
