class Library:
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)

    def showInfo(self):
        print(f"The Library has {self.nobooks} books and they are")
        for book in self.books:
            print(book)

lib=Library()
lib.addBook("The Beginning after the end")
lib.addBook("Solo Leveling")
lib.showInfo()
print('\n')
lib.addBook("SwordMaster's Youngest Son")
lib.addBook('SSS-Class Revival Hunter')
lib.showInfo()