import typing as t

from app.src.domain.Account import account

class protfolio():
    def __init__(self, account_id: int, ticker: str, quantity: int, id: int=-1):

        self.account_id = account_id
        self.ticker = ticker
        self.quantity = quantity
        self.id = id
    def __str__(self):
        return f'[id: {self.id}, quantity: {self.quantity}, ticker: {self.ticker}, account_id: {self.account_id} ]'