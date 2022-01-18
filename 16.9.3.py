class Client:
    def __init__(self, name, last_name, debet, credit):
        self.name = name
        self.last_name = last_name
        self.debet = sum(debet)
        self.credit = sum(credit)

    def get_balanse(self):
        return self.debet - self.credit

    def __str__(self):
        return f"Клиент - {self.name} {self.last_name}. Баланс: {self.get_balanse()}"

clients = [{"name": "Иван", "last_name": "Петров", "debet": {20, 40, 60}, "credit": {10, 20, 30}}]

for client in clients:
    result = Client(client["name"], client["last_name"], client["debet"], client["credit"])
    print(result)