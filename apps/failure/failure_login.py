'''
ログイン処理
担当：kudou
'''

#__pycache__が作成されないようにする
import sys
sys.dont_write_bytecode = True

from flask import render_template, request, redirect, Blueprint ,url_for,session
from dataStore.MySQL import MySQL

failure_login = Blueprint("failure_login",__name__)

#データベースを使うための情報
dns = {
    'user': 'root',
    'host': 'localhost',
    'password': '',
    'database': 'Failure'
}
db = MySQL(**dns)

#region データベース
'''
ログイン管理
'''
def is_login(id,password):

    sql = "SELECT password FROM employee WHERE id=%s"
    result = db.query(sql=sql,args=(id,))

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
@failure_login.route("/failureLogin")
def index(msg=None):
    #メッセージを取得
    message = request.args.get('msg')
    #ログイン画面表示
    return render_template("failure/failure_login.html",err_msg = message, title="ログイン")

@failure_login.route("/failureLoginCheck", methods=["POST"])
def system_login_check():
    
    # 入力値の取得
    id = request.form.get("id")
    password = request.form.get("password")

    #ログイン処理
    if is_login(id,password):
        #ログインが成功したら
        #セッションに名前を登録
        session.permanent = True
        session["faikure_user"] = id
        #ホーム画面に移動する
        return redirect(url_for('failure_history.history'))
    else:
        #失敗したらエラーメッセーとともにログイン画面に戻す
        print(id,password)
        return redirect(url_for('.index', msg="名前かパスワードが間違っています"))

@failure_login.route("/failurLogout")
def logout():
    session.pop('faikure_user', None)
    return redirect(url_for('system_main.index'))
#endregion



