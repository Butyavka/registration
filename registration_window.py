from tkinter import *
from sql_table import SQL_table
from tkinter import messagebox as mb


class Registration:
    def __init__(self, parent, width, height, title="Регистрация", resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable = (resizable[0], resizable[1])
        self.login_entry = Entry(self.root, justify=CENTER)
        self.password_entry = Entry(self.root, justify=CENTER, show='*')
        self.draw_widgets()

    def draw_widgets(self):
        Label(self.root, text='Регистрация', height=2).grid(row=0, column=0, columnspan=2)
        Label(self.root, text="Логин", width=20).grid(row=2, column=0)
        self.login_entry.grid(row=2, column=1)
        Label(self.root, text="Пароль", width=20).grid(row=3, column=0)
        self.password_entry.grid(row=3, column=1)
        Button(self.root, text="Готово", command=self.registration, width=20).grid(row=5, column=0)
        Button(self.root, text="Отмена", command=self.exit, width=20).grid(row=5, column=1, sticky=E)

    def registration(self):
        SQL = SQL_table(r"C:\Users\Butters\PycharmProject\MyForm\experement.db", "users_base")
        login = self.login_entry.get()
        password = self.password_entry.get()
        if SQL.check_logo(login):
            mb.showinfo("Регистрация", "Пользователь с таким логином уже существует")
        else:
            SQL.registration_login(login, password)
            mb.showinfo("Регистрация", "Вы успешно зарегистрировались")
            self.root.destroy()

    def exit(self):
        choice = mb.askyesno("Отмена", "Отменить регистрацию?")
        if choice:
            self.root.destroy()
