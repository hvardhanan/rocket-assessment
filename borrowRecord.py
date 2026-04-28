from finePolicy import FinePolicy

class BorrowRecord:
    def __init__(self, id, memberId, isbn, issueDate, dueDate, returnDate):
        self.id = id
        self.memberId = memberId
        self.isbn = isbn
        self.issueDate = issueDate
        self.dueDate = dueDate
        self.returnDate = returnDate

    def calculateFine(self, daysOverdue):
        policy = FinePolicy()
        return policy.computeFine(daysOverdue)