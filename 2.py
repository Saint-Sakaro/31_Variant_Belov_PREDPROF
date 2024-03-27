def sort_buble(data, key):
    '''
    Сортировка массива данных по столбцу в алфавитном порядке
    :param data: массив данных (юзеров)
    :param key: ключ по которому сравниваем (столбец)
    :return: Возвращает отсортрованный массив
    '''
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data


data = [i.split(',') for i in open("history_mirror.csv", encoding='utf-8')][1:]
key = 2
sort_data = sort_buble(data, key)
with open('history_mirror.csv', encoding='utf-8', mode='w') as f:
    f.write("date,username,verdict\n")
    k_printed = 0
    for user in sort_data:
        k_printed += 1
        if k_printed <= 4:
            print(f"{user[0]} - {user[1]} - {user[2][:-1]}")
        f.write(f"{user[0]},{user[1]},{user[2]}")
    f.close()