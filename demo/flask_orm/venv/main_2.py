from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)

# ERD: ENTITIES(TABLES) RELATIONS(1-1, 1-M, M-1, M-N) DIAGRAM

# AUTHOR can have many BOOKS: AUTHOR.BOOKS = [{}, {}] -> books = db.relationship(Book, backref='author')
# AUTHOR can have a BOOK: AUTHOR.BOOK = {} -> books = db.relationship(Book, backref='author', useList=False)
class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False, unique=True)
	author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
	year = db.Column(db.Integer, nullable=False)

class Author(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)

	books = db.relationship(Book, backref='author')

@app.route('/', methods=["GET"])
def home():
	return 'Server running perfectly fine!'

@app.route('/authors', methods=["GET"])
def getAuthors():
	authors = Author.query.all()

	authorList = []
	for author in authors:
		authorList.append({
			"id": author.id,
			"name": author.name
		})

	return authorList, 200

@app.route('/authors/<id>', methods=["GET"])
def getAuthor(id: int):
	author = Author.query.get(id) 

	return jsonify({
		"id": author.id,
		"name": author.name
	}), 200

@app.route('/authors/<id>/books', methods=["GET"])
def getAuthorsBooks(id: int):
	# First Way
	# SELECT * FROM BOOKS WHERE AUTHOR_ID = author_id
	# books = Book.query.filter(Book.author_id == id).all()

	# Second Way
	author = Author.query.get(id)
	books = author.books # SELECT JOINS

	bookList = []
	for book in books:
		bookList.append({
			"id": book.id,
			"title": book.title,
			"author_id": book.author_id,
			"year": book.year,
		})

	return bookList, 200

@app.route('/authors', methods=["POST"])
def addAuthor():
	data = request.get_json()

	newAuthor = Author(
		name = data["name"]
	)

	db.session.add(newAuthor)
	db.session.commit()

	return jsonify({
		"message": "Author added",
		"data": {
			"id": newAuthor.id,
			"name": newAuthor.name
		}
	}), 201

@app.route('/books', methods=["GET"])
def getBooks():
	books = Book.query.all()

	bookList = []
	for book in books:
		bookList.append({
			"id": book.id,
			"title": book.title,
			"author_id": book.author_id,
			"year": book.year,
		})

	return bookList, 200

@app.route('/books/<id>', methods=["GET"])
def getBook(id: int):
	book = Book.query.get(id)

	return jsonify({
		"id": book.id,
		"title": book.title,
		"author_id": book.author_id,
		"year": book.year,
	}), 200

@app.route('/books/<book_id>/author', methods=["GET"])
def getBooksAuthor(book_id: int):
	book = Book.query.get(book_id)

	# First Way
	author = Author.query.get(book.author_id)

	# Second Way
	author = book.author

	return jsonify({
		"id": author.id,
		"name": author.name
	}), 200

@app.route('/books', methods=["POST"])
def addBook():
	data = request.get_json()

	newBook = Book(
		title=data["title"], 
		author_id=data["author_id"], 
		year=data["year"]
	)

	db.session.add(newBook)
	db.session.commit()

	return jsonify({
		"message": "Book added",
		"data": {
			"id": newBook.id,
			"title": newBook.title,
			"author_id": newBook.author_id,
			"year": newBook.year,
		}
	}), 201

if __name__ == "__main__":
	with app.app_context():
		print(f'Creating DB Tables')
		db.create_all()
	app.run(debug=True)


# MANY     -      MANY 
# FOLLOWER | FOLLOWED
#    x     |    z
#    x     |    a
#    y     |    z
#    z     |    x
#    z     |    b
#    z     |    c