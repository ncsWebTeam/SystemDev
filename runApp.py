from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from dataStore.MySQL import MySQL
import datetime
import os
app = Flask(__name__)
app.secret_key = "dajieteg9DSIngai"
app.permanent_session_lifetime = datetime.timedelta(minutes=30)

AUTHORITY_LEVEL = 9

dns = {
    'user': 'root',
    'host': 'localhost',
    'password': '',
    'database': 'System'
}
db = MySQL(**dns)


#----------------ログイン画面処理--------------------STR↓
@app.route("/")
def index(msg=None):
    #ログイン画面表示
    message = request.args.get('msg')
    return render_template("system/systemLogin.html",msg = message, title="ログイン")

@app.route("/systemLoginCheck", methods=["POST"])
def systemLoginCheck():
    print("login")
    #ログイン処理
    # 入力値の取得
    userName = request.form.get("userName")
    password = request.form.get("password")

    print(userName,password)

    return redirect(url_for("home"))
#----------------ログイン画面処理--------------------END↑

#------------------ホーム画面------------------STR ↓
@app.route("/home")
def home():
    return render_template("system/home.html")
#----------------ホーム画面--------------------END↑



#region エラー処理
@app.errorhandler(404) # 404エラーが発生した場合の処理
def error_404(error):
    # print("404エラー")
    return redirect(url_for("index"))

@app.errorhandler(405) # 405エラーが発生した場合の処理
def error_405(error):
    print("405エラー")
    return redirect(url_for("index"))

@app.errorhandler(500) # 500エラーが発生した場合の処理
def error_500(error):
    print("500エラー")
    return redirect(url_for("index"))
#endregion

if __name__ == '__main__':
    # 8080ポートで起動
    app.run()