from flask import Flask
app = Flask(__name__)
""" ddddddddddddddddddddddd"""

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


app.run()
