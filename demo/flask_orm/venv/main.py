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
	books = Book.query.all()

	booksList = []
	for book in books:
		booksList.append({
			"id": book.id,
			"title": book.title,
			"author": book.author,
			"year": book.year
		})

	return jsonify(booksList), 200

@app.route('/books', methods=["POST"])
def addBooks():
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

if __name__ == "__main__":
	with app.app_context():
		print(f'Creating DB Tables')
		db.create_all()
	app.run(debug=True)