#!/usr/bin/python3
"""
Module that create a basic Flask app
"""


from flask import Flask, render_template, request
import json
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f) # lecture des data json
        items_list = data.get('items', []) # récupération des valeurs liées à la clé 'items'
    return render_template('items.html', items=items_list) # envoie des items

@app.route('/products')
def show_products():
    # Récupération des paramètres URL
    source = request.args.get('source', 'json').lower()  # json par défaut
    product_id = request.args.get('id', type=int)

    product_list = []

    # Lecture des données selon le type
    try:
        if source == 'json': # cas JSON
            with open('products.json') as f:
                data = json.load(f)
                product_list = data.get('items', [])
        elif source == 'csv': # cas CSV
            with open('products.csv', newline='') as f:
                reader = csv.DictReader(f)
                product_list = []
                for row in reader:
                    # Convertir price et id en float/int
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    product_list.append(row)
        else:
            return f"Invalid source '{source}'. Use 'json' or 'csv'.", 400

    except FileNotFoundError:
        return f"File for source '{source}' not found.", 404

    # Filtrage par id si fourni - Partie optionel 
    if product_id:
        filtered = [p for p in product_list if p['id'] == product_id]
        if not filtered:
            return f"Product with id={product_id} not found.", 404
        product_list = filtered

    return render_template('product_display.html', products=product_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
