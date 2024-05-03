class User:
    def __init__(self, user_name, mail, password):
        self.user_name = user_name
        self.mail = mail
        self.password = password

    def to_dict(self):
        return {
            "user_name": self.user_name,
            "mail": self.mail,
            "password": self.password
        }
