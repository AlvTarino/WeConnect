class wcApp:
    def __init__(self):
        self.users = {}

#register new users
    def create_user(self, user):
        if user.email in self.users.keys():
            return False
        else:
            self.users[user.email] = user
            return True

#login a registered user
    def login(self, email, password):
        if email in self.users.keys():
            user = self.users[email]
            if user.password == password:
                return True
            return False

    def open_user(self, email):
        if email in self.users.keys():
            return self.users[email]
        return None

#updates an already existing business
    def update_business(self):
#deletes business
    def delete_business(self):
