class Book:

    def __init__(self,title,author,):
        self.title = title
        self.author = author
        self.is_available = True


    def borrow(self):
       if self.is_available:
        self.is_available = False
        print(f"You have seccessfully borrow '{self.title}'by (self.author).")
       else:
          print(f"sorry , '{self.title}'is currently not available.")

    def return_book(self):
       if not self.is_available:
          self.is_available = True
          print(f"'{self.title}'has been return. Thanks you!")
       else:
          print(f"'{self.title}' was not borrowed.")


    def display_info(self): 
       status = "Available"  if self.is_available else "Checked Out"
       print(f"Title: {self.title}, Author: {self.author}, Status: {status}") 


book1 = Book("The greet seeker", "G. william")
book2 = Book(" Hunter series" , " A. Otoo")
book3 = Book("123 buds" , "W. newton")  


book1.borrow
book1.return_book()
book1.display_info()
                

        