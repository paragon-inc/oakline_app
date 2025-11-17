from flask import Flask, render_template, abort

app = Flask(__name__)

# --- PRODUCTS DATA ---

PRODUCTS = [
    {
        "id": "oak-hoodie-black",
        "name": "Oakline Classic Hoodie – Black",
        "price": 39.99,
        "tagline": "Heavyweight, minimal, old-money aesthetic.",
        "description": (
            "550 GSM heavyweight black hoodie with a boxy, relaxed fit. "
            "Features the Oakline tree logo embroidered in an earth-tone thread. "
            "Soft brushed interior, double-stitched cuffs, and premium metal hardware. "
            "Designed to last years, not months."
        ),
        "image_url": "/static/images/black_hoodie.jpeg",
        "in_stock": True,
    }
]


def get_product_or_404(product_id: str):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    abort(404)


# --- ROUTES (PAGES) ---


@app.route("/")
def home():
    featured = PRODUCTS  # we only have one product for now
    return render_template("home.html", products=featured)


@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)


@app.route("/products/<product_id>")
def product_detail(product_id):
    product = get_product_or_404(product_id)
    return render_template("product_detail.html", product=product)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
