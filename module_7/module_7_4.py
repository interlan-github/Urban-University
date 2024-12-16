#!/usr/bin/python3

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

# Конкатенация
print ("В команде Мастера кода участников: "+str(team1_num)+"! ")

# Использование %s
print ("В команде Мастера кода участников: %s! " % (team1_num))

# Использование .format
print ("В команде Мастера кода участников: {}! ".format(team1_num))

# Использование f-строки
print (f"В команде Мастера кода участников: {team1_num}! ")

# Использование %s
print ("Итого сегодня в командах участников: %s и %s!" % (team1_num,team2_num))

# Использование .format
print ("Команда Волшебники данных решила задач: {score_2}! ".format(score_2 = score_2))
print ("Волшебники данных решили задачи за :{}! ".format(team1_time))

# Использование f-строки
print (f"{challenge_result}")
print (f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
