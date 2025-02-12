from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"

db = SQLAlchemy(app)

class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50), nullable=False, unique=True)
	author = db.Column(db.String(50), nullable=False)
	year = db.Column(db.Integer, nullable=False)

@app.route('/', methods=["GET"])
def home():
	return 'Server running perfectly fine!'

@app.route('/books', methods=["GET"])
def getBooks():
	# ---------
	# Filtering
	# ---------
	# books = Book.query.all() # returns all books: SELECT * FROM Book
	# books = Book.query.filter(Book.year > 2020) # SELECT * FROM Book WHERE year < 2020
	# books = Book.query.filter(Book.author == "A1") # SELECT * FROM Book WHERE author = "A1"
	# books = Book.query.filter(Book.author == "A1" & Book.year > 2020) 
	# books = Book.query.filter(Book.author == "A1" | Book.year > 2020) 

	# year = int(request.args.get("year"))
	# author = request.args.get("author")

	# print(f'{year} {type(year)} {author} {type(author)}')

	# books = Book.query.filter(Book.year == year).filter(Book.author == author)
	# books = Book.query.filter((Book.year == year) & (Book.author == author))

	# {{URL}}/books?year=2020
	# books = Book.query.filter(Book.year == year)

	# {{URL}}/books?year_start_at=2020&year_end_at=2025 
	# SELECT * FROM Book WHERE year >= 2020 and year <= 2025
	# yearStartAt = request.args.get("year_start_at")
	# yearEndAt = request.args.get("year_end_at")
	# books = Book.query.filter((Book.year >= yearStartAt) & (Book.year <= yearEndAt))

    # ----------
	# Pagination
	# ----------
	# # LIMIT, OFFSET
	# limit = request.args.get('page_size')
	# offset = request.args.get('page')

	# # page 1 with size 5: 1,2,3,4,5 -> offset: 0 [(1-1) * 5]
	# # page 2 with size 5: 6,7,8,9,10 -> offset: 5 [(2-1) * 5]
	# # page 3 with size 5: 11,12,13,14,15 -> offset: 10 [(3-1) * 5]
	# # offset = (page - 1) * page_size

	# if not limit:
	# 	limit = 5
	
	# if not offset:
	# 	offset = 0

	# if int(limit) > 5:
	# 	return jsonify({
	# 		"message": "page size is over servers capacity"
	# 	}), 400
	
	# limit = int(limit)
	# offset = int(offset)

	# offset = (offset - 1) * limit # offset = (page - 1) * page_size
	# books = Book.query.limit(limit).offset(offset).all()


    # -------
	# SORTING
	# -------
	# ORDER BY
	books = Book.query.order_by(Book.author).all() # default is asc
	books = Book.query.order_by(Book.author.asc()).all()
	books = Book.query.order_by(Book.author.desc()).all()
	# books = Book.query.order_by(Book.id.asc()).limit(limit).offset(offset).all()


	booksList = []
	for book in books:
		booksList.append({
			"id": book.id,
			"title": book.title,
			"author": book.author,
			"year": book.year
		})

	return jsonify(booksList), 200

@app.route('/books/<id>', methods=["GET"])
def getBook(id: int):
	book = Book.query.get(id)

	return jsonify({ 
		"message": "Book Updated", 
		"book": {
			"id": book.id,
			"title": book.title,
			"author": book.author,
			"year": book.year
		} 
	}), 200

@app.route('/books', methods=["POST"])
def addBook():
	data = request.get_json() # Data from the body of the request
	newBook = Book(title=data['title'], author=data['author'], year=data['year'])
	
	db.session.add(newBook)
	db.session.commit()
	
	return jsonify({ 
		"message": "Book added", 
		"book": {
			"id": newBook.id,
			"title": newBook.title,
			"author": newBook.author,
			"year": newBook.year
		} 
	}), 201

@app.route('/books/<id>', methods=["PUT", "PATCH"])
def updateBook(id: int):
	book = Book.query.get(id)

	data = request.get_json() # { "author": "A3", "title": "B1, "year": 2025 }

	if "year" in data:
		book.year = data["year"]
    
	if "title" in data:
		book.title = data["title"]
	
	if "author" in data:
		book.author = data["author"]

	# Extra Efficiency:
	# for key in data:
	# 	book.key = data[f'{key}']

	db.session.commit()

	return jsonify({ 
		"message": "Book Updated", 
		"book": {
			"id": book.id,
			"title": book.title,
			"author": book.author,
			"year": book.year
		} 
	}), 200

@app.route('/books/<id>', methods=["DELETE"])
def deleteBook(id: int):
	book = Book.query.get(id)

	db.session.delete(book)
	db.session.commit()

	return jsonify({
		"message": "Book deleted"
	}), 200

# TODO: batchUpdates, batchCreates, batchDeletes

if __name__ == "__main__":
	with app.app_context():
		print(f'Creating DB Tables')
		db.create_all()
	app.run(debug=True)