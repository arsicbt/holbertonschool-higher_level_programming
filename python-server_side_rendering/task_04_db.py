#!/usr/bin/python3
"""
Flask application for displaying items and products from JSON/CSV
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# --- ROUTES DE BASE ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# --- ITEMS (JSON simple) ---

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except FileNotFoundError:
        items_list = []
    return render_template('items.html', items=items_list)


# --- PRODUCTS (JSON ou CSV avec id optionnel) ---

def get_data_from_db():
    try:
        connexion = sqlite3.connect('products.db')
        cursor = connexion.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        connexion.close()

        # Création d'une liste de dictionnaire
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
        return products

    except sqlite3.Error as e:
        print("Database error")
        return []


@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()
    product_id = request.args.get('id', type=int)
    error = None
    product_list = []

    try:
        # ----------- JSON -----------
        if source == 'json': 
            with open('products.json') as f:
                product_list = json.load(f)

        # ----------- CSV -----------
        elif source == 'csv':
            with open('products.csv', newline='') as f:
                reader = csv.DictReader(f)
                product_list = []
                for row in reader:
                    product_list.append({
                        "id": int(row.get('id', 0)),
                        "name": row.get('name', 'Unknown'),
                        "category": row.get('category', 'N/A'),
                        "price": float(row.get('price', 0))
                    })

        # ----------- DB -----------
        elif source == 'sql':
            product_list = get_data_from_db()

        else:
            error = f"Wrong source", 400

    except FileNotFoundError:
        error = f"Product not found", 404

    # Filtrage par id
    if not error and product_id:
        filtered = [p for p in product_list if p['id'] == product_id]
        if filtered:
            product_list = filtered
        else:
            error = f"Product not found", 404

    return render_template('product_display.html', products=product_list, error=error)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
