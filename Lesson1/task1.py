st = input("Enter a some string")
number_of_st = []
if len(st) != 0:
    for symbol in st:
        if symbol.isnumeric():
            number_of_st.append(int(symbol))
    print(*number_of_st, sep=',') if number_of_st else print('No numbers in string')
else:
    print("Enter above 0 chars")
