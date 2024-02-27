'''
保守会社表示画面
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

#endregion



