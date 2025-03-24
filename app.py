from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template(
        'home.html',
        title='Danny Desk',
        description='Manage customers, invoicing, inventory and more!')