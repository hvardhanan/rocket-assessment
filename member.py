from user import User
from enums import Role

class Member(User):
    def __init__(self, id, name, email):
        super().__init__(id, name, email, Role.MEMBER)
        self.active_borrows = []
        self.fines = []

    def searchBook(self, librarian, isbn):
        try:
            for b in librarian._books:
                if b.isbn == isbn:
                    print(f"Found: {b.title} - Status: {b.status.name} - Qty: {b.quantity}")
                    return b
            raise Exception("BOOK NOT FOUND")
        except Exception as e:
            print(f'The following error occured during the searchBook flow : {e}')

    def payFine(self):
        total = sum(self.fines)
        if total > 0:
            print(f"Paid fine: {total}")
            self.fines = []
        else:
            print("No fines")
