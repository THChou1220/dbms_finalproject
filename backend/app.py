from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = 'gym.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/', methods=['GET'])
def default():
    return jsonify({"message": "Hello!!!"})

if __name__ == '__main__':
    app.run(debug=True)
