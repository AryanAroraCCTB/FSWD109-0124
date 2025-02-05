from flask import Flask, request, render_template

# Flask App
app = Flask(__name__, template_folder = "templates")

# Define our routes
@app.route('/', methods=["GET", "POST"])
def home():
	# Request Info
	# print(request)
	# print(request.method, request.scheme, request.server, request.root_path, request.path, request.query_string, request.headers)

	# Important ones
	# print(request.method, request.path, request.query_string, request.json)

	if request.method == "GET":
		print(request.method, request.path, request.query_string)
	
	if request.method == "POST":
		print(request.method, request.path, request.query_string, request.json)
		data = request.json
		name = data["name"]
		print(f'Name is {name}')

	return 'Welcome to my home page'

@app.route('/contact')
def contact():
	print(request.method, request.path, request.query_string)
	print(request.query_string[0]) # name=abc -> n   110
	print(request.query_string[1]) # name=abc -> a   97

	query = request.query_string.decode('utf-8') # "name=abc"
	print(query, type(query))

	# Small exercise
	# Take the query from above and get the key value pairs
	# "name=abc" -> name = "abc"
	return 'Contact Page'

# /post/2
@app.route('/post/<id>')
def postById(id):
	return id

# /post?author=abc&year=2025
@app.route('/post')
def post():
	print(request.method, request.path, request.query_string, request.args)
	author: str = request.args.get('author')
	year: int = request.args.get('year')
	author2: str = request.args.get('author2')
	
	print(author, year, author2)

	return 'List of all posts'


@app.route('/demo')
def demo():
	return render_template('index.html')

@app.route('/style.css')
def demo2():
	return render_template('style.css')

if __name__ == '__main__':
	app.run(debug=True)

