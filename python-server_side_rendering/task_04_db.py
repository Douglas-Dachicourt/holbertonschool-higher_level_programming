from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
        try:
            with open('products.json', 'r') as file:
                data = json.load(file)
                if not id:
                    return render_template('product_display.html', products=data)
                else:
                    for item in data:
                        if str(item["id"]) == id:
                            return render_template('product_display.html', item=item)
                    return "Product not found"
        except FileNotFoundError:
            return "No Json file found"

    elif source == 'csv':
        try:
            products = []
            with open('products.csv', newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(row)
                    #print(products)
                if not id:
                    return render_template('product_display.html', products=products)
                else:
                    for product in products:
                        if product["id"] == id:
                            return render_template('product_display.html', item=product)
                    return "Product not found"
        except FileNotFoundError:
            return "No Csv file found"
    
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()

            if id is None:
                cursor.execute('SELECT * FROM Products')
                rows = cursor.fetchall()
                #print(rows)
                products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
                return render_template('product_display.html', products=products)       
            else:
                cursor.execute('SELECT * FROM Products WHERE id=?', (id,))
                row = cursor.fetchone()
                #print(row)
                if row:
                    item = {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
                    #print(item)
                    return render_template('product_display.html', item=item) 
                else:
                    return "Product not found"

        except sqlite3.Error as e:
            return f"An Error has occured: {e}"
        
        finally:
            conn.close()
    else:
        return "Wrong source"
                
if __name__ == '__main__':
    app.run(debug=True, port=5000)
