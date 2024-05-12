# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com
# (Хеш то що з ліва записувати не потрібно)

try:

    with open('emails.txt', ) as source, open('res.txt', 'w') as res_file:
        for line in source:
            if line.strip().lower().endswith('@gmail.com'):
                print(line.split()[-1], file=res_file)
except Exception as e:
    print(e)

    