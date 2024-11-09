#!/usr/bin/python3

# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.

# Внутри функции реализовать следующую логику:

# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.
# Пункты задачи:

# Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

ALLOW_DOMAINS = ['com','ru', 'net']

def send_email(message, recipient, sender = "university.help@gmail.com"):
    print (message, recipient, sender)
    error_message = "Невозможно отправить письмо с адреса "+sender+" на адрес "+recipient
    if "@" not in recipient:
        return error_message

    recipient_domain = recipient.split('.')[-1]
    if recipient_domain not in ALLOW_DOMAINS:
        return error_message

    sender_domain = sender.split('.')[-1]
    if sender_domain not in ALLOW_DOMAINS:
        return error_message

    if sender == recipient:
        return "Нельзя отправить письмо самому себе!"

    if sender == 'university.help@gmail.com':
        return "Письмо успешно отправлено с адреса "+sender+" на адрес "+recipient+"."
    return "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "+sender+" на адрес "+recipient+"."


print (send_email('Собаку потеряли', 'vasyok1337gmail.com'))
print (send_email('А почему нельзя? Это вообщето-то мой домен, что хочу то и горожу', 'chernousov@interlan.xyz'))
print (send_email("А я в дурке сам с собой говорю",'anton@mail.ru',sender = 'anton@mail.ru'))
print (send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print (send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print (send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print (send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
