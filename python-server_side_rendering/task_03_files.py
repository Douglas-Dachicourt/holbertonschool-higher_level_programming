from flask import Flask, render_template, request, jsonify
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
    try:
        with open("items.json", "r") as file:
            data = json.load(file)
            items = data.get('items', [])
    except FileNotFoundError:
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    query_params = request.args

    source = query_params.get('source')
    id = query_params.get('id')

    if source == 'json':
        with open('products.json', 'r') as file:
            data = json.load(file)
            if not id:
                return render_template('product_display.html', data=data)
            else:
                for item in data:
                    if str(item["id"]) == id:
                        return render_template('product_display.html', item=item)
                return "No product found"

    elif source == 'csv':
        products = []
        with open('products.csv', newline="") as file:
            data = csv.DictReader(file)
            for row in data:
                products.append(row)
            if not id:
                return render_template('product_display.html', products=products)
            else:
                for product in products:
                    if product["id"] == id:
                        return render_template('product_display.html', item=product)
                return "No product found"
    else:
        return "Invalid source"
                
if __name__ == '__main__':
    app.run(debug=True, port=5000)
