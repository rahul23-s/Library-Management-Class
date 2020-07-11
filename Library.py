class Library:
    def __init__(self,listofbooks,library_name):
        self.All_books=listofbooks
        self.name= library_name
        self.lendBooks= {}
        self.availableBooks=listofbooks


    def displayBooks(self):
        print("We Have following Books in our Library:\n")
        for book in self.All_books:
            print(book)

    def displayAvailableBooks(self):
        print("Following Books are Available to Lend:")
        for book in self.availableBooks: 
            print(book)        

    def lendBook(self, user , book):
        if book not in self.lendBooks.keys() and book in self.All_books:
            self.lendBooks.update({book : user})
            self.availableBooks.remove(book)
            print("We Have Updated the Lender-Book Database. You can Take the book now. :)")
        elif book not in self.All_books:
            print("Invalid Book name!")
        else:
            print(f"Sorry, The Book you requested for is already alloted to {self.lendBooks[book]}!")
    
    def addBook(self, book):
        self.All_books.append(book)
        print(f"{book} has been Added to the Library. ThankYou for Your Contribution!")        

    def returnBook(self, book):
        if book not in self.lendBooks.keys():
            print("Invalid Book name!")
        elif book in self.lendBooks.keys():    
            self.lendBooks.pop(book)
            print(f"{book} has been Returned to the Library. Database Updated!!")        

        
        

if __name__ == "__main__":
    
        sharma_lib = Library(["Atomic Habits","Python","C Programming","Structure & Interpretation of Computer Programs","Learning Python","Core Java","Rich Dad Poor Dad","Core Java Advanced","C++ Primer","GO Programming Language By Google","Code Complete","The Pragmatic Programmer","Clean Code","Introduction to Algorithms","Data Structure & Algorithm in JAVA","The Lean Startup","Zero To One","The 100$ Startup","The E Myth","Think & Grow Rich","Elon Musk: Tesla, SpaceX"],"Sharma")
        print(f"--------------Welcome To The {sharma_lib.name} Library--------------")
        while True:
            print(f"--------------Choose the Operation to perform:--------------")
            print("1. Display All Books in the Library")
            print("2. Display Available Books")
            print("3. Lend a Book")
            print("4. Add a Books")
            print("5. Return a Book")
            user_choice=""
            user_choice= input()
            if user_choice not in ['1','2','3','4','5']:
                print("Invalid Input. Try Again!")
                continue
            else:
                user_choice= int(user_choice)
            # displaying Books
            if user_choice== 1: 
                sharma_lib.displayBooks()
            
            # displaying non-alloted Books
            if user_choice== 2: 
                sharma_lib.displayAvailableBooks()

            # Lending Book    
            elif user_choice== 3:
                book = input("Enter the Book you want to Lend: ")
                name = input("Enter your Name: ")
                sharma_lib.lendBook(name, book)

            # Adding Book                    
            elif user_choice== 4:
                book= input("Enter the Name of the book:")
                sharma_lib.addBook(book)

            # Returning Book    
            elif user_choice== 5:                
                book= input("Enter the Name of the book:")
                sharma_lib.returnBook(book)
            choice=""
            while choice!= "c" or choice!= "e":
                choice= input("Press |c to continue| or | e to Exit |")    
                if choice == "c":
                    break
                elif choice == "e":
                    exit()
                else:
                    print("Invalid Input. Try Again!")
                    
