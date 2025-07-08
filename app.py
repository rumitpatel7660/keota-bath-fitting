from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    # Dynamically list all product images grouped by category
    products_dir = os.path.join(app.static_folder, 'products')
    categories = []
    products_by_category = {}
    for category in sorted(os.listdir(products_dir)):
        category_path = os.path.join(products_dir, category)
        if os.path.isdir(category_path):
            categories.append(category)
            images = [f'products/{category}/{img}' for img in os.listdir(category_path) if img.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
            products_by_category[category] = images
    return render_template('products.html', categories=categories, products_by_category=products_by_category)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True) 