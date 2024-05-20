import re

login_pattern = re.compile(r'^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$')
password_pattern = re.compile(r'^\w{8,16}$')

accounts = {'shrek@gmail.com': {'password': '12345678', 'f_name': 'Шрэк', 's_name': 'Зеленый', 'social_credit': 999, 'tasks': ['Поспать', 'Поесть']},
            'applebox@mail.ru': {'password': 'apbx0101', 'f_name': 'Яблоко', 's_name': 'Яблочное', 'social_credit': 650, 'tasks': ['Найти коробку', 'Съесть коробку']}}

def login_check(login, password):

    if login_pattern.search(login):
        if password_pattern.search(password):
            return True

    return False


def account_login(login, password):

    if login in accounts.keys():

        if password == accounts[login]['password']:

            return accounts[login]

        else:
            return 'password'

    else:
        return 'login'
