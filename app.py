# For Private Key
import datetime

from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
load_dotenv()

MONGODB_ID = os.environ.get("MONGODB_ID")
MONGODB_PW = os.environ.get("MONGODB_PW")

app = Flask(__name__)

client = MongoClient(
    'mongodb+srv://{id}:{pw}@cluster0.5hnlvb6.mongodb.net/?retryWrites=true&w=majority'.format(id=MONGODB_ID, pw=MONGODB_PW))
db = client.dbsparta


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=["POST"])
def login_post():

    key_receive = request.form['key_give']
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    time_now = datetime.datetime.now()

    # find id from DB
    searchedAccount = db.swot_account.find_one(
        {'id': id_receive}, {'_id': False})

    # 1. Break: Check if ID is available
    if searchedAccount is None:
        return jsonify({
            'msg': "아이디가 없노",
            'available': '0'
        })

    # 2. Break: Check if pw in DB matches PW received
    if searchedAccount['pw'] != pw_receive:
        return jsonify({
            'msg': '마 비번 틀리다',
            'available': 0
        })

    loginHistory = searchedAccount['loginHistory']
    loginHistory.append(time_now)

    keyLog = searchedAccount['key']
    keyLog.append(key_receive)

    db.swot_account.update_one(
        {'id': id_receive}, {
            '$set': {
                'key': keyLog,
                'loginHistory': loginHistory
            }
        })
    return jsonify({
        'msg': '로그인 완료',
        'available': 1
    })


@app.route('/register', methods=["GET"])
def register_get():
    return render_template('register.html')


@app.route('/register', methods=["POST"])
def register_post():

    # Setting up new account
    time_now = datetime.datetime.now()
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    doc = {
        'registeredAt': time_now,
        'loginHistory': [time_now],
        'key': [],
        'id': id_receive,
        'pw': pw_receive
    }
    db.swot_account.insert_one(doc)

    return jsonify({
        'msg': '회원이 되신걸 축하드립니다👻 ',
        'available': 1
    })


@app.route('/home', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/isRegistered', methods=["POST"])
def isRegistered():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    searchedAccount = db.swot_account.find_one(
        {'id': id_receive}, {'_id': False})

    # Break: if there is already registered ID
    if searchedAccount:
        return jsonify({
            'msg': "이 아이디는 이미 누가 사용중 ❌",
            'available': 0
        })

    return jsonify({
        'msg': '회원가입 가입 가능하다 ✅',
        'available': 1
    })


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
