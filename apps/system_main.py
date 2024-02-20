#__pycache__が作成されないようにする
import sys
sys.dont_write_bytecode = True

from flask import render_template, request, redirect, Blueprint ,url_for,session
from dataStore.MySQL import MySQL
from datetime import timedelta

systemMain = Blueprint("systemMain",__name__)



#データベースを使うための情報
dns = {
    'user': 'root',
    'host': 'localhost',
    'password': '',
    'database': 'System'
}
db = MySQL(**dns)

#region データベース
'''
ログイン管理
'''
def is_login(name,password):

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

#endregion

#region 関数

#endregion

#region 画面
@systemMain.route("/")
def index(msg=None):
    #メッセージを取得
    message = request.args.get('msg')
    #ログイン画面表示
    return render_template("system/system_login.html",err_msg = message, title="ログイン")

@systemMain.route("/systemLoginCheck", methods=["POST"])
def system_login_check():
    
    # 入力値の取得
    user_name = request.form.get("userName")
    password = request.form.get("password")

    #ログイン処理
    if is_login(user_name,password):
        #ログインが成功したら
        #セッションに名前を登録
        session.permanent = True
        session["system_user"] = user_name
        #ホーム画面に移動する
        return redirect(url_for('.home'))
    else:
        #失敗したらエラーメッセーとともにログイン画面に戻す
        return redirect(url_for('.index', msg="名前かパスワードが間違っています"))

@systemMain.route("/home")
def home():
    #sessionの確認
    if "system_user" in session:
        #ホーム画面を表示する
        print(session["system_user"])
        return render_template("system/system_home.html", title="ホーム")
    else:
        return redirect(url_for('.index', msg="ログインしてください"))
    
@systemMain.route("/logout")
def logout():
    session.pop('system_user', None)
    return redirect(url_for('.index'))
#endregion



