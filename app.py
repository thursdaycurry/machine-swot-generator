from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
print(PRIVATE_KEY)

@app.route('/')
def home():
    return render_template('index.html')

