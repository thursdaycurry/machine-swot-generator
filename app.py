# For Private Key
import os
from dotenv import load_dotenv
load_dotenv()

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/swot', methods=["POST"])
def swot_post():
    return jsonify({'msg': '등록 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)