class Investor():
    def __init__(self, name: str, address: str, status: str, id: int = -1):
        self.name = name
        self.address = address
        self.status = status
        self.id = id

    def __str__(self):
        return f'[id: {self.id}, name: {self.name}, address: {self.address}, status: {self.status}]'

    @staticmethod
    def from_dict(dict):
        if dict.get('name') is None or dict.get('status') is None or dict.get('address') is None: # all attributes are required
            raise Exception(f'Can not create Investor object from dict {dict}: missing required attributes')
        else:
            return Investor(dict.get('name'), dict.get('address'), dict.get('status'))
            