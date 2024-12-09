#!/usr/bin/python3

# Init Databases
user_db = {}

class UrTube:
    def __init__(self, name, floors):
        self.name = name

class Video:
    def __init__(self, name, floors):
        self.name = name

class User:
    def __init__(self, nickname, password, password_confirmation, age):
        self.nickname = nickname
        self.password = password
        self.password_confirmation = password_confirmation
        self.age = age
    def data_check(self):
        status = 'OK'
        if self.password != self.password_confirmation:
            status = 'PASSWORD ERROR'
            result = {'status': status, 'nickname': self.nickname, 'password': self.password, 'age': self.age}
            return result

def print_user_status (user):
    message = 'Пользователь успешно зарегистрирован'
    if user['status'] == 'PASSWORD ERROR':
        message = 'Пароли не совпадают'
    return message

user = User(nickname = 'Ivan',password='Qazxsw123', password_confirmation = '321', age=15).data_check()
print (print_user_status(user))
