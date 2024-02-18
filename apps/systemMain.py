from flask import Flask, render_template, request, redirect,  session, send_from_directory ,Blueprint
from dataStore.MySQL import MySQL
import datetime
import os
systemMain = Blueprint("systemMain",__name__)
# app = Flask(__name__)
systemMain.secret_key = "dajieteg9DSIngai"
systemMain.permanent_session_lifetime = datetime.timedelta(minutes=30)

AUTHORITY_LEVEL = 9

dns = {
    'user': 'root',
    'host': 'localhost',
    'password': '',
    'database': 'System'
}
db = MySQL(**dns)
#region データベース
#----------------データベース関係--------------------STR↓
def isLogin(name,password):

    sql = "SELECT password FROM member WHERE name=%s"
    result = db.query(sql=sql,args=(name,))

    #値がかえってこなかったら
    if not result:
        return False
    
    #パスワードが一致していたら
    if result[0][0] == password:
        return True
    
    #一致していなかったら
    return False
#----------------データベース関係--------------------END↑
#endregion

#region 画面
#----------------ログイン画面処理--------------------STR↓
@systemMain.route("/")
def index(msg=None):
    #ログイン画面表示
    message = request.args.get('msg')
    return render_template("system/systemLogin.html",msg = message, title="ログイン")

@systemMain.route("/systemLoginCheck", methods=["POST"])
def systemLoginCheck():
    
    # 入力値の取得
    userName = request.form.get("userName")
    password = request.form.get("password")

    #ログイン処理
    if isLogin(userName,password):
        return redirect("/home")
    else:
        return redirect("index",msg = "ユーザーネームかパスワードが間違っています")
#----------------ログイン画面処理--------------------END↑

#------------------ホーム画面------------------STR ↓
@systemMain.route("/home")
def home():
    return render_template("system/home.html", title="ホーム")
#----------------ホーム画面--------------------END↑
#endregion



