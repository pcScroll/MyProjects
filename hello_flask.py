from flask import Flask
from vsearch import search4letters
from vsearch import search4vowels
app = Flask(__name__)
""" ddddddddddddddddddddddd"""


@app.route('/')
def hello2() -> str:
    return 'Hello22 world from Flask!'


@app.route('/search4')
def do_search() -> set: 
  return str(search4letters('life, the universe, and everything', 'eiru,'))
     

@app.route('/vsearch')
def vsearch() -> set:
    return str(search4vowels('life, the universe, and everything'))


if __name__ == "__main__":
 app.run(debug=True)
