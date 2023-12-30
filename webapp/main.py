from flask import Flask, render_template, session


app = Flask(__name__)
app.secret_key = 'adfsdfskjadfskjhlfsadhadvsknulvadsbviubgoil'

products = [
    { 'id': 1, 'name': 'Product 1', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 2, 'name': 'Product 2', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 3, 'name': 'Product 3', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 4, 'name': 'Product 4', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 5, 'name': 'Product 5', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 6, 'name': 'Product 6', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 }, 
    { 'id': 7, 'name': 'Product 7', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 8, 'name': 'Product 8', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 9, 'name': 'Product 9', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
    { 'id': 10, 'name':'Product 10', 'img': 'https://vscda.org/wp-content/uploads/2017/03/300x300.png', 'price': 10 },
]

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/<int:product_id>')
def product(product_id): 
    product = next((p for p in products if p['id'] == product_id), None)
    return render_template('product.html', product=product)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        session['cart'].append(product)
    return 'Product added to cart'

@app.route('/cart')
def cart(): 
    cart_item = session.get('cart', [])
    return render_template('cart.html', products=cart_item)

if __name__ == '__main__':
    app.run(debug=True, port=8080)