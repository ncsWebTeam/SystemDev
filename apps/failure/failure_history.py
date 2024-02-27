'''
ログイン処理
担当：
'''

#__pycache__が作成されないようにする
import sys
sys.dont_write_bytecode = True

from flask import render_template, request, redirect, Blueprint ,url_for,session
from dataStore.MySQL import MySQL

failure_history = Blueprint("failure_history",__name__)

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
@failure_history.route("/failureHistory")
def history():
    #sessionの確認(System用)
    if "system_user" in session:
        #sessionの確認(障害対応用)
        if "faikure_user" in session:
            #ホーム画面を表示する
            return render_template("failure/failure_history.html", title="ホーム")
        else:
            return redirect(url_for('.index', msg="ログインしてください"))
    else:
        return redirect(url_for('system_main.index', msg="ログインしてください"))
    #sessionの確認

#endregion



