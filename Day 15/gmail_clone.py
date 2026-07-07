# {username : password, username1 : password1, username2 : password2}


class GMail:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.database = {}

    def add_account(self):
        self.database[self.username] = self.password

    # def add_account_directly(self, username, passsword):
    #     self.database[username] = passsword

    def forget_password(self, new_password):
        self.database[self.username] = new_password

    def print_db(self):
        print(self.database)

gmail = GMail("mani@gmail.com", "123456")
gmail.print_db()
gmail.add_account()
gmail.print_db()

gmail.forget_password("123333")

# gmail.add_account_directly("mani1@gmail.com", "1234567")

gmail.print_db()