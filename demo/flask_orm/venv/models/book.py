# Creating Models
# CREATE TABLE Book (
#   id INT PRIMARY KEY,
#   name VARCHAR(50) UNIQUE,
#   summary TEXT NOT NULL
#   year INT NOT NULL
#   isPopular BOOLEAN NOT NULL DEFAULT
# );
class Book(db.Model):
	id = db.Column(db.Integer, primary_key=True) # BigInteger, SmallInteger
	name = db.Column(db.String(50), unique=True) # Similar to VARCHAR
	summary = db.Column(db.Text, nullable=False) # No size limits 
	year = db.Column(db.Integer, nullable=False)
	isPopular = db.Column(db.Boolean, default=False)
	stars = db.Column(db.Float, nullable=False, default=1.0) # db.Numberic(10, 2)
	firstCopySoldOn = db.Column(db.Date, nullable=True, default=None) # YYYY-MM-DD
	firstCopySoldAt = db.Column(db.DateTime, nullable=True, default=None) # YYYY-MM-DD HH:MM:SS, Time: HH:MM:SS
	status = db.Column(db.Enum("Printing", "In Stock", "Sold Out"), nullable=False, default="Sold Out")