class Book:
	def __init__(self, title: str, author: str, year: int, isbn: str):
		self.title = title
		self.author = author
		self.year = year
		self.isbn = isbn 
		self.is_available = True

	def get_info(self) -> str:
		return f"{self.title}, автор - {self.author}, год издания - {self.year}"
	
	def borrow(self) -> str:
		'''Бронирование книги'''
		if self.is_available:
			self.is_available = False
			return f"Книга '{self.title}' выдана"
		else:
			return f"Выдача книги? '{self.title}' невозможна"
	
	def return_book(self) -> str:
		'''Возврат книги'''
		if not self.is_available:
			self.is_available = True
			return f"Книга '{self.title}' возвращена"
		else:
			return f"Книга '{self.title}' уже доступна"
		
		
class EBook(Book):
	def __init__(self, title: str, author: str, year, format: str, isbn: str):
		super().__init__(title,author,year, isbn)
		self.format = format
	def get_info(self) -> str:
		return f"{self.title}, автор - {self.author}, год издания - {self.year}, формат - {self.format}"


#ebook1 = EBook("test_title","test_author",1997, "pdf", "978-3-16-148410-0")
#print(eBook1.get_info())		
