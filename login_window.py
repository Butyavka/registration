from tkinter import *
from tkinter import messagebox as mb
from registration_window import Registration
from sql_table import SQL_table
import sqlite3


class Window:
    def __init__(self, width, height, title="Вход", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable = (resizable[0], resizable[1])
        self.login_entry = Entry(self.root, justify=CENTER)
        self.password_entry = Entry(self.root, justify=CENTER, show='*')

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        Label(self.root, text="Вход", height=2).grid(row=0, column=0, columnspan=2)
        Label(self.root, text="Логин", width=20).grid(row=2, column=0)
        self.login_entry.grid(row=2, column=1)
        Label(self.root, text="Пароль", width=20).grid(row=3, column=0)
        self.password_entry.grid(row=3, column=1)
        Button(self.root, text="Войти", width=10, command=self.data_base).grid(row=5, column=0)
        Button(self.root, text="Выйти", width= 10, command=self.exit).grid(row=5, column=1, sticky=E)

    def registration_window(self, width, height, title="Регистрация", resizable=(False, False)):
        Registration(self.root, width, height, title, resizable)

    def data_base(self):
        SQL = SQL_table("data_base.db", "users_base")
        login = self.login_entry.get()
        password = self.password_entry.get()
        if SQL.check_logo(login):
            if SQL.check_password(login, password):
                mb.showinfo("Вход", "Вы, успешно вошли!")
            else:
                mb.showerror("Вход", "Неверный пароль")
        else:
            choice = mb.askyesno("Вход", "Пользователя с таким логином не существует. Хотите зарегистрироваться?")
            if choice:
                self.registration_window(400, 400)

    def exit(self):
        choice = mb.askyesno("Выход", "Вы хотите выйти?")
        if choice:
            self.root.destroy()


if __name__ == "__main__":
    window = Window(500, 500)
    window.run()