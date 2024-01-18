class Library:

    def __init__(self,bookList:list) -> None:
        self.bookList = bookList

    def _availableBooks(self):
        return self.bookList

    def getBook(self,bookName:str):
        if bookName in self.bookList:
            self.bookList.remove(bookName)
            return True
        return False

    def returnBook(self,bookName:str):
        if(bookName in self.bookList):
            return False
        else:
            self.bookList.append(bookName)
            return True
         

class Student(Library):
    def __init__(self, first_name:str, last_name:str, student_id:int):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} with student id {self.student_id} has been added"

Library_CSIT = Library(['Math','C', 'C++', 'Python', 'Computer Graphics', 'AI', 'Math II'])

student1 = Student('Raju', 'Sharma', 1)
student2 = Student('Shyam', 'Rai', 2)

available_books =  Library_CSIT._availableBooks()

