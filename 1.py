data = [i.split(',') for i in open("history_mirror.csv", encoding='utf-8')][1:]
if_first_print_user = False
data_correct_users = []
with open('mirror_error.csv', encoding='utf-8', mode='w') as f:
    f.write("date, username\n")
    for user in data:
        if user[2][:-1] == "Победа над смертью":
            if not if_first_print_user:
                FIO = user[1].split()
                FIO_to_print = f"{FIO[0]} {FIO[1][:1]}.{FIO[2][:1]}."
                print(f"Сообщение было зафиксировано: {user[0]} у пользователя {FIO_to_print}")
                if_first_print_user = True
            f.write(f"{user[0]}, {user[1]}\n")
