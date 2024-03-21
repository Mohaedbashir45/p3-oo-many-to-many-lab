class Book:
    members = []

    def __init__(self, title):
        self.title = title
        self.members.append(self)

    def contracts(self):
        return [contract for contract in Contract.members if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

    def sign_contract(self, author, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid author object")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")

        contract = Contract(author, self, date, royalties)
        return contract

    def total_royalties(self):
        contracts = self.contracts()
        if contracts:
            return sum(contract.royalties for contract in contracts)
        else:
            return 0

class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.members.append(self)

class Contract:
    members = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author) or not isinstance(book, Book):
            raise Exception("Invalid author or book object")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int):
            raise Exception("Invalid royalties")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.members.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.members if contract.date == date]
