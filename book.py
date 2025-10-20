class book:
	def __init__(self, title: str, author: str, year: int, isbn: str):
		self.title = title
		self.author = author
		self.year = year
		self.isbn = isbn 
	def get_info(self) -> str:
	    return f"{self.title}, автор - {self.author}, год издания - {self.year}"
		
class EBook(book):
	def __init__(self, title: str, author: str, year, format: str, isbn: str):
		super().__init__(title,author,year, isbn)
		self.format = format
	def get_info(self) -> str:
		return f"{self.title}, автор - {self.author}, год издания - {self.year}, формат - {self.format}"
book1 = book("Гарри Поттер и Философский камень", "Дж.К.Роулинг", 1997, "978-3-16-148410-0")		
print(book1.get_info())	

ebook1 = EBook("test_title","test_author",1997, "pdf", "978-3-16-148410-0")
print(ebook1.get_info())		
