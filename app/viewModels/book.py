class BookViewModel:
	
	def __init__(self, book):
		self.image = book['image']
		self.author = book['author']
		self.title = book['title']
		self.isbn = book['isbn']
	
		
class BookCollection:
	"""书籍集合"""
	
	def __init__(self):
		self.total = 0
		self.books = []
		self.keyword = ''
		
	def fill(self, yushuBook, keyword):
		self.total = yushuBook.total
		self.keyword = keyword
		self.books = [BookViewModel(book) for book in yushuBook.books]
		