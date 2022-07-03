from app import app
from flask import render_template, redirect, url_for, request
import json
import os
import markdown
from app.models.product import Product

@app.route('/')
def index():
    libs = []
    for element in ["requirements.txt"]:
        with open(element, "r") as file:
            lines = file.readlines()
            for line in lines:
                libs.append('<li>' + line.replace('==', ' <span class="badge text-bg-light">') + '</span></li>')
    with open('README.md', "r") as fileMD:
        readmeHtml = markdown.markdown(fileMD.read(), extensions=['markdown.extensions.tables', 'markdown.extensions.fenced_code'])
    return render_template("index.html.jinja", libs = libs , readmeHtml = readmeHtml)

@app.route('/extract', methods=["POST", "GET"])
def extract():
    if request.method == "POST":
        product_id = request.form.get("product_id")
        product = Product(product_id)
        product.extract_name()
        if product.product_name:
            product.extract_opinions().calculate_stats().draw_charts()
            product.export_opinions()
            product.export_product()
        else:
            error = "Ups... coś poszło nie tak"
            return render_template("extract.html.jinja", error=error)
        return redirect(url_for('product', product_id=product_id))
    else:
        return render_template("extract.html.jinja")

@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("app/opinions")]
    return render_template("products.html.jinja", products=products)

@app.route('/author')
def author():
    return render_template("author.html.jinja")

@app.route('/product/<product_id>')
def product(product_id):
    product = Product(product_id)
    product.import_product()
    stats = product.stats_to_dict()
    opinions = product.opinions_to_df()
    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)