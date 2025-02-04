from flask import Flask, request

# Flask App
app = Flask(__name__)

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


@app.route('/post/<id>')
def postById(id):
	return id

@app.route('/post')
def post():
	print(request.method, request.path, request.query_string, request.args)
	author = request.args.get('author')
	year = request.args.get('year')
	print(author, year)

	return 'List of all posts'

if __name__ == '__main__':
	app.run(debug=True)
