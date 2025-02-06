from flask import Flask, render_template, request
import random

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def homePage():
	return render_template('homePage.html')

@app.route('/hello/<name>')
def helloPage(name: str):
	user = { "username": name, "age": 25, "isLoggedIn": False }
	products = [
		{ "name": "Phone", "price": 10 }, 
		{ "name": "Laptop", "price": 11 }, 
		{ "name": "Watch", "price": 12 }, 
		{ "name": "Tv", "price": 13 }
	]

	num = random.randint(1, 100)
	if num % 2 == 0: 
		# if num is even user is logged in
		user["isLoggedIn"] = True
	else:
		# if num is odd user is not logged in
		user["isLoggedIn"] = False

	return render_template('homePage.html', user=user, number=num, items=products)
	

if __name__ == "__main__":
	print("Sever is Running now...")
	app.run(debug=True)