class Server:
    def __init__(self):
        self.users = []

    def AddUser(self, name):
        self.users.append(name)

    def __getitem__(self, index):
        return self.users[index]


if __name__ == "__main__":
    server = Server()
    server.AddUser("Vasya")
    server.AddUser("Petya")
    server.AddUser("Kirill")
    print(server[1])