import flask
import sqlite3
import os
import random

flag = os.getenv('FLAG', 'flag{fake_flag}')

db = sqlite3.connect(':memory:', check_same_thread=False)
cursor = db.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('admin', random.randbytes(16).hex()))
cursor.execute('CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, hidden BOOLEAN)')
for product in ['cheese', 'bread', 'milk', 'eggs', 'butter', 'yogurt', 'juice', 'cereal', 'cookies', 'chocolate']:
    cursor.execute('INSERT INTO products (name, hidden) VALUES (?, ?)', (product, False))
cursor.execute('INSERT INTO products (name, hidden) VALUES (?, ?)', (flag, True))
db.commit()

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        cursor.execute(f'SELECT * FROM users WHERE username = "{username}" AND password = "{password}"')
        user = cursor.fetchone()
        if user:
            return flask.redirect('/products')
        else:
            response = "Invalid credentials!"
    return flask.render_template_string('''
        <h1>Login</h1>
        <form action="/" method="post">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Ping</button>
        </form>
        <pre>{{ response }}</pre>
    ''', response=response)

@app.route('/products', methods=['GET', 'POST'])
def products():
    response = ""
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        cursor.execute(f'SELECT * FROM products WHERE name = "{name}" AND hidden = 0')
        product = cursor.fetchone()
        if product:
            response = "Product in stock!"
        else:
            response = "Product not found!"
    return flask.render_template_string('''
        <h1>Find Products</h1>
        <form action="/products" method="post">
            <input type="text" name="name" placeholder="Product Name" required><br>
            <button type="submit">Search</button>
        </form>
        <pre>{{ response }}</pre>
    ''', response=response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
