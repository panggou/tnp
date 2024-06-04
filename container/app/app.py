from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create the database and table if they don't exist
def create_table():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products 
                 (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')
    conn.commit()
    conn.close()

create_table()

# Route to display the inventory
@app.route('/')
def inventory():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('SELECT * FROM products')
    products = c.fetchall()
    conn.close()
    return render_template('inventory.html', products=products)

# Route to add a new product
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = request.form['quantity']
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()
    return redirect(url_for('inventory'))

if __name__ == '__main__':
    app.run(debug=True)
