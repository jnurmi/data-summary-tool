from flask import Flask, render_template, jsonify
from faker import Faker

GLOBAL_COUNTER = 0
fake = Faker()

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")


@app.route('/api/getdata', methods=['GET'])
def random_word():
    global GLOBAL_COUNTER
    GLOBAL_COUNTER += 1
    return jsonify({
        'idx': GLOBAL_COUNTER,
        'text': fake.name()
    })


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")
