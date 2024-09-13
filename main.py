from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html", title="Моя супер піцерія")


@app.get("/menu-ababagalamaga/")
def menu():
    pizzas = [
        {"name": "Пепероні", "price": 168, "ingredients": "вершковий соус, моцарелла, салямі пікантна, томат чері, перець пепероні, пармезан, базилік"},
        {"name": "Гавайська", "price": 229, "ingredients": "Тісто, неаполітанський соус, сир моцарела, шинка, ананас, кукурудза, куряче філе"},
        {"name": "Грибна", "price": 256, "ingredients": "Тісто, грибний соус, сир моцарела, печериці, сир пармезан, мікрогрін, опеньки консервовані, крем-сир"},
        {"name": "Піца від шефа", "price": 199, "ingredients": "Тісто, неаполітанський соус, сир моцарела, часникова олія з зеленню, соус шпинатний з фетою, ковбаса домашня, мікрогрін"}
    ]
    context = {
        "pizzas": pizzas,
        "title": "Мега меню"
    }
    return render_template("menu.html", **context)


if __name__ == "__main__":
    app.run(debug=True)