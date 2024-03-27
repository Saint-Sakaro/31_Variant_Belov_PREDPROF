data = [i.split(',') for i in open("history_mirror.csv", encoding='utf-8')][1:]
years = {}
for user in data:
    date = user[0]
    year = date.split('-')[0]
    if years.get(year) == None:
        years[year] = [user]
    else:
        years[year].append(user)
for year in years:
    print(f"В {year} году зеркало было использовано {len(years[year])}.")