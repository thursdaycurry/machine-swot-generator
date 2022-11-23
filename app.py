# For Private Key
import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_ID = os.environ.get("MONGODB_ID")
MONGODB_PW = os.environ.get("MONGODB_PW")

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://{id}:{pw}@cluster0.5hnlvb6.mongodb.net/?retryWrites=true&w=majority'.format(id=MONGODB_ID, pw=MONGODB_PW))
db = client.dbsparta

print(list(db.fanlog.find({}, {'_id':False})))
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_post():
    key_receive = request.form['key_give']
    print(key_receive)

    return jsonify({'msg': 'done 수정 완료!'})

@app.route('/home', methods=["GET"])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)