import sqlite3


class SQL_table:

    def __init__(self, database, name):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.name = name

    def check_logo(self, login):
        with self.connection:
            self.cursor.execute(f'SELECT login FROM {self.name} WHERE login = "{login}"')
            check_result = self.cursor.fetchone()
            if check_result is None:
                return False
            else:
                return True

    def check_password(self, login, password):
        with self.connection:
            self.cursor.execute(f'SELECT login, password FROM {self.name} WHERE login = "{login}" AND password = "{password}"')
            check_result = self.cursor.fetchone()
            if check_result is None:
                return False
            else:
                return True

    def registration_login(self, login, password):
        with self.connection:
            self.cursor.execute(f'SELECT login FROM {self.name} WHERE login = "{login}"')
            if self.cursor.fetchone() is None:
                self.cursor.execute(f'INSERT INTO {self.name}(login, password) VALUES ("{login}", "{password}")')
                self.connection.commit()
                return True
            else:
                return False


