#__pycache__が作成されないようにする
import sys
sys.dont_write_bytecode = True

from flask import Flask,redirect,url_for
#ページインポート
from apps.system_main import systemMain
from datetime import timedelta

app = Flask(__name__)

#sessionを利用するためのもの
app.secret_key = 'test'
app.permanent_session_lifetime = timedelta(minutes=15) 

#インポートしたページを配列に格納する
appSet = [
    systemMain
]

#ここでページを登録する
for appName in appSet:
    app.register_blueprint(appName)

#region エラー処理
@app.errorhandler(404) # 404エラーが発生した場合の処理
def error_404(error):
    # print("404エラー")
    return redirect(url_for("systemMain.index"))

@app.errorhandler(405) # 405エラーが発生した場合の処理
def error_405(error):
    print("405エラー")
    return redirect(url_for("systemMain.index"))

@app.errorhandler(500) # 500エラーが発生した場合の処理
def error_500(error):
    print("500エラー")
    return redirect(url_for("systemMain.index"))
#endregion


if __name__ == "__main__":
    app.run(debug=True,port=8000)