from root import root
from tkinter import *
from functions import login_check, account_login
from tkinter.messagebox import showinfo, showerror, showwarning

root.grid_columnconfigure(0, minsize=150)
root.grid_columnconfigure(1, minsize=250)
root.grid_rowconfigure(0, minsize=90)
root.grid_rowconfigure(1, minsize=90)

#Entries
login_entry = Entry(root, font=('Arial', 12), width=20)
password_entry = Entry(root, font=('Arial', 12), width=20, show='*')

def logining():
    login_entry.config(fg='black')
    password_entry.config(fg='black')
    login_entry.config(bg='white')
    password_entry.config(bg='white')

    if login_check(login_entry.get(), password_entry.get()):
        login_entry.config(fg='green')
        password_entry.config(fg='green')

        success = account_login(login_entry.get(), password_entry.get())

        if success == 'login':
            showerror(title='Ошибка входа', message='Такого логина не существует')
        elif success == 'password':
            showerror(title='Ошибка входа', message='Пароль не подходит к логину')
        else:
            tasks = ''
            for t in success['tasks']:
                tasks += t + '\n'

            showinfo(title=f'{success["f_name"]} {success["s_name"]}', message=f'Social Credit - {success["social_credit"]}\nTasks:\n{tasks}')

    else:
        if login_entry.get() == '':
            login_entry.config(bg='red')
        else:
            login_entry.config(fg='red')

        if password_entry.get() == '':
            password_entry.config(bg='red')
        else:
            password_entry.config(fg='red')

#Labels
login_label = Label(root,text='Login', font=('Arial', 14), padx=50, bg=root['bg'])
password_label = Label(root, text='Password', font=('Arial', 14), padx=50, bg=root['bg'])

#Btns
accept_btn = Button(root, text='Login', font=('Arial', 16), width=12, command=logining, bg='#FFB54A', relief=GROOVE)
