from flask import Flask
from vsearch import search4letters
app = Flask(__name__)
""" ddddddddddddddddddddddd"""


@app.route('/')
def hello2() -> str:
    return 'Hello22 world from Flask!'


@app.route('/search4')
def do_search() -> str: 
    return str(search4letters('life, the universe, and everything', 'eiru, !'))


if __name__ == "__main__":
 app.run()
