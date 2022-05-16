class Account():
    def __init__(self, investor_id:int, balance: float, id:int = -1):
        self.investor_id = investor_id
        self.balance = balance
        self.id = id

    def __str__(self):
       return f'[id: {self.id}, investor_id: {self.investor_id}, balance: {self.balance}]'

        