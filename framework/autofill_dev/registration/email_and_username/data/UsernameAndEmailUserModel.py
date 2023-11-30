class UsernameAndEmailUserModel:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return "Email: {}\nUsername: {}\nPassword: {}\n".format(self.email, self.username,self.password)