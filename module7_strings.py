team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


# Использование %: {'team1_num': team1_num, 'name_team1': 'Мастер кода'}
print("В команде %s: '%x участников!'" % ('Мастер кода',team1_num))
print('Итого сегодня в командах участников: "%(team1_num)x и %(team2_num)x".' % {'team1_num': team1_num, 'team2_num': team2_num})

# Использование format():
print("Команда {name_team2} решила задач: '{0}'!".format(score_2, name_team2='Волшебники данных'))
print("{} решили задачи за {} c ".format('Волшебники данных', team2_time))

# Использование f-строк:
print(f'Команды решили: "{score_1} и {score_2} задач".')
print(f'Результат битвы: "{challenge_result}"')
print(f"Сегодня было решено: '{tasks_total} задач, в среднем по {time_avg} секунды на задачу!'.")


