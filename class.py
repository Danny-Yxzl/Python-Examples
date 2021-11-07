class user():
    def __init__(self) -> None:
        pass
    name = "Danny"
    phone = "13105143702"
    def call(self):
        return self.phone
    class son():
        success = True


login = user()
print(login.son.success)
