from librarian import Librarian
from member import Member

def main():
    lib = Librarian(1, "Admin", "admin@hvrd.in")
    member = Member(101, "User", "user@hvrd.in")

    bookList = [
        ['id001', 'isbn001', 'title001', 'author001', 2],
        ['id002', 'isbn002', 'title002', 'author002', 7],
        ['id003', 'isbn003', 'title003', 'author003', 3],
        ['id004', 'isbn004', 'title004', 'author004', 5],
        ['id005', 'isbn005', 'title005', 'author005', 5],
        ['id006', 'isbn006', 'title006', 'author006', 10],
    ]

    for book in bookList:
        lib.addBook(*book)

    print(f'Please set current Date and Due date before proceeding')
    lib.setCurrentDate(input('Enter new Current Date : '))
    print(f"\nLogged in as: {member.name} (Fines: {sum(member.fines)})")
    lib.setDueDate(input('Enter new due Date : '))

    while True:

        print("1. Search Book\n2. Issue Book \n3. Return Book \n4. Pay Fine\n5. Add Book \n6. List All Books\n7. Modify Current Date\n8. Modify Due Date\n9. Exit")
        choice = input("Choice: ")
        
        if choice == "1":
            member.searchBook(lib, input("ISBN: "))
        elif choice == "2":
            lib.issueBook(input("Rec ID: "), member, input("ISBN: "), lib.getCurrentDate(), lib.getDueDate())
        elif choice == "3":
            lib.processReturn(member, input("ISBN: "), lib.getCurrentDate(), int(input("Days overdue: ")))
        elif choice == "4":
            member.payFine()
        elif choice == "5":
            lib.addBook(input("ID: "), input("ISBN: "), input("Title: "), "Author", int(input("Qty: ")))
        elif choice == "6":
            lib.listAllBooks()
        elif choice == "7":
            newDate = input(f'You are modifying the currentDate now. Present value is {lib.getCurrentDate()}. Enter the new currentDate : ')
            lib.setCurrentDate(newDate)
        elif choice == "8":
            newDate = input(f'You are modifying the dueDate now. Present value is {lib.getDueDate()}. Enter the new dueDate : ')
            lib.setDueDate(newDate)
        elif choice == "9":
            break
        else: 
            continue

if __name__ == "__main__":
    main()
