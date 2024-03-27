data = [i.split(',') for i in open("history_mirror.csv", encoding='utf-8')][1:]
while True:
    inp_st = input()
    if inp_st == 'stop':
        break
    inp_st = inp_st.split(' ')
    if_print = False
    if len(inp_st) == 2:
        for user in data:
            FIO = user[1].split()
            FIO_to_print = f"{FIO[0]} {FIO[1][:1]}.{FIO[2][:1]}."
            if inp_st[0] == FIO[1] and inp_st[1] == FIO[2]:
                print(f"Предсказание для {FIO_to_print} - {user[2][:-1]}")
                if_print = True
    if not if_print:
        print("Вас не нашлось в записях")