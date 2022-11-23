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

import datetime


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_post():
    key_receive = request.form['key_give']
    data_now = datetime.datetime.now()
    print(key_receive, data_now)
    doc = {
        'time': data_now,
        'key': key_receive
    }
    db.swot.insert_one(doc)
    return jsonify({'msg': 'done 수정 완료!'})

@app.route('/signup', methods=["GET"])
def signup():
    return render_template('signup.html')

@app.route('/home', methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/isRegistered', methods=["POST"])
def isRegistered():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']
    searchedAccount = db.swot_account.find_one({'id':id_receive}, {'_id':False})
    print(searchedAccount)
    print(pw_receive)

    # 1. Check if ID doesn't exist in DB
    if not searchedAccount:
        return jsonify({
            'msg': "successfully logged in!",
            'available': '0'
        })

    # 2. Check if ID doesn't match PW
    if searchedAccount['pw'] == pw_receive is None:
        return jsonify({
            'msg': "id and password are not matching..",
            'available': '0'
        })
    #
    # if searchedAccount is None:
    #     return jsonify({
    #         'msg': "You can logged in!",
    #         'possible': 1
    #     })
    # else:
    #     if searchedAccount['pw'] == pw_receive:
    #         return jsonify({
    #             'msg': "successfully logged in!"
    #         })
    #     else :
    #         return jsonify({
    #             'msg': "Password Wrong"
    #     })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)