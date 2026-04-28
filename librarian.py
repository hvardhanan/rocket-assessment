from user import User
from enums import Role
from enums import BookStatus
from borrowRecord import BorrowRecord
from book import Book

class Librarian(User):
    _books = []
    _borrowRecords = []
    _currentDate = ''
    _dueDate = ''

    def __init__(self, id, name, email):
        super().__init__(id, name, email, Role.LIBRARIAN)

    def getCurrentDate(self):
        return self._currentDate
    
    def getDueDate(self):
        return self._dueDate
    
    def setCurrentDate(self, newDate):
        self._currentDate = newDate
    
    def setDueDate(self, newDate):
        self._dueDate = newDate

    def issueBook(self, record_id, member, isbn, issue_date, due_date):
        try:    
            if self.role != Role.LIBRARIAN:
                raise Exception('ACCESS DENIED')

            if sum(member.fines) > 0:
                raise Exception('UNPAID FINES')

            if len(member.active_borrows) >= 3:
                raise Exception('BORROW LIMIT REACHED')

            book = None
            for b in self._books:
                if b.isbn == isbn:
                    book = b
                    break
            
            if not book:
                raise Exception('BOOK NOT FOUND')

            if book.status != BookStatus.AVAILABLE or book.quantity <= 0:
                raise Exception('BOOK UNAVAILABLE')

            record = BorrowRecord(record_id, member.id, isbn, issue_date, due_date, "")
            self._borrowRecords.append(record)
            member.active_borrows.append(record)
            
            book.quantity -= 1
            if book.quantity == 0:
                book.status = BookStatus.ISSUED
                
            print(f"Issued {book.title} to {member.name}")
        except Exception as e:
            print(f'The following error occured during the issueBook flow : {e}')

    def processReturn(self, member, isbn, return_date, days_overdue):
        try:
            if self.role != Role.LIBRARIAN:
                raise Exception('ACCESS DENIED')

            record = None
            for r in member.active_borrows:
                if r.isbn == isbn and r.returnDate == "":
                    record = r
                    break
            
            if record:
                record.returnDate = return_date
                fine = record.calculateFine(days_overdue)
                if fine > 0:
                    member.fines.append(fine)
                    print(f"Fine added: {fine}")

                for b in self._books:
                    if b.isbn == isbn:
                        b.quantity += 1
                        b.status = BookStatus.AVAILABLE
                        break
                
                member.active_borrows.remove(record)
                print("Return processed")
            else:
                raise Exception('NO ACTIVE RECORD FOUND')
        except Exception as e:
            print(f'The following error occured during the processReturn flow : {e}')

    def addBook(self, id, isbn, title, author, quantity):
        try:
            if self.role != Role.LIBRARIAN:
                raise Exception('ACCESS DENIED')
            
            new_book = Book(id, isbn, title, author, quantity)
            self._books.append(new_book)
            print(f"Added {title}")
        except Exception as e:
            print(f'The following error occured during the addBook flow : {e}')

    def listAllBooks(self):
        i = 1
        print(f'S.no  ISBN    --    TITLE    --    AUTHOR    --    STATUS    --    QUANTITY')
        for book in self._books:
            print(f'{i}.  {book.isbn}    --    {book.title}    --    {book.author}    --    {book.status}    --    {book.quantity}')
            i += 1
        if i == 1 : print('NO BOOKS AVAILABLE')
