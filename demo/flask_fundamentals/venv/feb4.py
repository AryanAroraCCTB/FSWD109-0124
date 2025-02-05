# ------------
# Practice API
# ------------

# Question
# • Create a simple Flask Library API
from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "templates")

# • A Book has id(int), name(str), author_name(str), year_published(int), genre(str)
# Mocking Database
books = [
	{ "id": 1, "name": "B1", "author_name": "A1", "year_published": 2021, "genre": "G1" },
	{ "id": 2, "name": "B2", "author_name": "A2", "year_published": 2022, "genre": "G2" },
	{ "id": 3, "name": "B3", "author_name": "A3", "year_published": 2022, "genre": "G3" },
	{ "id": 4, "name": "B4", "author_name": "A4", "year_published": 2023, "genre": "G4" },
	{ "id": 5, "name": "B5", "author_name": "A5", "year_published": 2023, "genre": "G5" },
	{ "id": 6, "name": "B6", "author_name": "A6", "year_published": 2023, "genre": "G6" },
	{ "id": 7, "name": "B7", "author_name": "A7", "year_published": 2024, "genre": "G7" },
	{ "id": 8, "name": "B8", "author_name": "A8", "year_published": 2024, "genre": "G8" },
	{ "id": 9, "name": "B9", "author_name": "A9", "year_published": 2024, "genre": "G9" },
	{ "id": 10, "name": "B10", "author_name": "A10", "year_published": 2024, "genre": "G10" },
	{ "id": 11, "name": "B11", "author_name": "A11", "year_published": 2025, "genre": "G11" },
	{ "id": 12, "name": "B12", "author_name": "A12", "year_published": 2025, "genre": "G12" },
	{ "id": 13, "name": "B13", "author_name": "A13", "year_published": 2025, "genre": "G13" },
	{ "id": 14, "name": "B14", "author_name": "A14", "year_published": 2025, "genre": "G14" },
	{ "id": 15, "name": "B15", "author_name": "A15", "year_published": 2025, "genre": "G15" }
]
nextId = len(books) + 1

# Default Home Route
@app.route('/')
def home():
	return render_template('library.html')

#   -------
# • Routes:
#   -------
# • GET /books
# • GET /books?order_by=name&order=asc
@app.route('/books', methods=["GET"])
def getBooks():
	orderBy = request.args.get('order_by')
	order = request.args.get('order')  

	sortedBooks = books
	if orderBy and order:
		# Practice this sorting question
		sortedBooks = books

	return sortedBooks

# • GET /books/{id}
@app.route('/books/<id>', methods=["GET"])
def getBookById(id):
	# When the books are in the sorted order
	# actualID = int(id) - 1
	# return books[actualID]

	# Ideal Case: When we don't know the order of the books
	for book in books:
		if book["id"] == int(id):
			return book
		
	# Real Case:
	# return 'SELECT * FROM books where id = int(id)'
		
	return "Error: Book not found", 404

# • POST /books
@app.route('/books', methods=["POST"])
def createBook():
	# Practice: finding the highest id from the list of books without using nextId

	global nextId
	
	newBook = request.json # {'name': 'T1', 'author': 'A298310', 'year_published': 2025, 'genre': 'G23456'}
	newBook["id"] = nextId
	nextId += 1

	books.append(newBook)

	return newBook, 201


# • PUT /books/{id}
@app.route('/books/<id>', methods=["PUT"])
def updateBook(id):
	# One way
	# book = getBookById(id)

	# book["name"] = request.json["name"]
	# book["author_name"] = request.json["author_name"]
	# book["year_published"] = request.json["year_published"]
	# book["genre"] = request.json["genre"]

	# for index, b in books:
	# 	if b["id"] == int(id):
	# 		books[index] = book

	# Another way
	newBook = None
	newBook["id"] = int(id)
	newBook["name"] = request.json["name"]
	newBook["author_name"] = request.json["author_name"]
	newBook["year_published"] = request.json["year_published"]
	newBook["genre"] = request.json["genre"]

	for index, b in books:
		if b["id"] == int(id):
			books[index] = newBook

	return newBook


# • DELETE /books/{id}
@app.route('/books/<id>', methods=["DELETE"])
def deleteBook(id):
	# Practice question

	return "Successfully Deleted"

if __name__ == "__main__":
	print("Sever is Running now...")
	app.run(debug=True)