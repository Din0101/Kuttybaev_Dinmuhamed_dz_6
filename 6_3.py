some_str = ["Иванов,Иван,Иванович", "Петров,Петр,Петрович", "Петров,Петр,"]
some_str2 = ["скалолазание,охота", "горные лыжи"]#, "dsc", "dsc"]

with open('users.csv', 'w+', encoding='utf-8') as users:
    for i in some_str:
        users.write(f'{i}\n')
with open('hobby.csv', 'w+', encoding='utf-8') as users:
    for i in some_str2:
        users.write(f'{i}\n')


def dict_from_csv():
    some_dict = {}
    with open('users.csv', encoding='utf-8') as users_csv:
        key_d = users_csv.readlines()
    with open('hobby.csv', encoding='utf-8') as hobby_csv:
        val_d = hobby_csv.readlines()
    for i in range(len(key_d)):
        if len(key_d) < len(val_d):
            some_dict = 1
            return exit(1)
        elif i >= len(val_d):
            some_dict.setdefault(key_d[i].strip().replace(',', ' '))
        else:
            some_dict.setdefault(key_d[i].strip().replace(',', ' '), val_d[i].strip())
    return some_dict


a = dict_from_csv()
print(a)


